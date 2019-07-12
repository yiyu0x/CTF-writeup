from pwn import *

#r = process('./pwntools')
r = remote('140.110.112.31', 2116)
print r.recvuntil('magic :)\n')
r.send(str(p32(127174655)))
print r.recvuntil('prove yourself.\n')
for i in range(1000):
	eq = r.recvuntil('?')
	print eq
	ans = eval(eq.split('=')[0])
	print ans
	r.sendline(str(ans))
print r.recvuntil('hacker!\n')
r.interactive()
