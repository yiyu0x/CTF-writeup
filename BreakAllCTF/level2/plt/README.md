![](https://raw.githubusercontent.com/yiyu0x/CTF-writeup/master/BreakAllCTF/level2/plt/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-12%20%E4%B8%8B%E5%8D%8810.01.44.png)

NX 打開，寫 shellcode 進 bss 也無法執行，於是使用 ROP。

system@plt 可以直接使用 ， 缺少一個參數，控制 rdi 即可 (x64 calling convension)

ROPgadget 可以輕鬆幫助我們找到 pop rdi ret ; 

要注意在 gdb 中要先 set follow-fork-mode child

debug 時才不會因為 system 打開新的 process 而 attach 脫落
