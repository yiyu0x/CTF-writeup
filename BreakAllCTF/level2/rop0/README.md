![](https://raw.githubusercontent.com/yiyu0x/CTF-writeup/master/BreakAllCTF/level2/rop0/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-12%20%E4%B8%8B%E5%8D%8810.02.17.png)

有兩次輸入機會，第一次可以寫入 bss。第二次(在 func1)則可以在 stack 上產生 bof。
NX 關閉，所以選擇 ROP。要注意的是用 ROPchain 找到的 payload 不能用，猜測應該是兩次輸入的內容都要在 300 這個範圍內。
只好自己串 ROP 來減少長度。
