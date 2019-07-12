
![](https://raw.githubusercontent.com/yiyu0x/CTF-writeup/master/BreakAllCTF/level2/luck/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-12%20%E4%B8%8B%E5%8D%889.59.50.png)

透過 read 字串到 buf 變數產生的 bof 去覆蓋 v6, v7, v6

將 random 覆蓋成 0 ， 之後再輸入 0 就可以保證相等

要注意的是 pwntools 的 p32 是使用 kwargs ， 所以負數要使用 p32(-1, sign='signed') 而不是 p32(-1, 'signed')
