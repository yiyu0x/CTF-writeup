![](https://raw.githubusercontent.com/yiyu0x/CTF-writeup/master/BreakAllCTF/level2/oob3/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-12%20%E4%B8%8B%E5%8D%8810.01.01.png)

利用 bof 把 printf GOT 蓋掉 ， 蓋成 admin_shell 的位置。

為何不蓋 return address ？ 

因為 bss 段的位置非常低， return address 在 0x7fff... ， 而且 array 有檢查不能超過三

所以只能找比 user 這個 array 還要低的位置來覆蓋， printf('PIN') 就是一個好選擇

要蓋 GOT 前提是 RELRO 不能打開 ， 或是開 Partial 才有辦法寫 GOT ， 這題確實也是 Partial 
