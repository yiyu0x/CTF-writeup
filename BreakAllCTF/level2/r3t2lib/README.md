![](https://raw.githubusercontent.com/yiyu0x/CTF-writeup/master/BreakAllCTF/level2/r3t2lib/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-16%20%E4%B8%8B%E5%8D%886.57.59.png)

輸入我們想要的 GOT 位置，它會印出實際上 loading 到 memory 之後的位置

我們可以透過輸入 main 以及它回傳 main 的位置，來得知道 base_libc 的位置

這就在把 base_libc 加上 system 在 libc 中的 offset 就可以知道 system() 在程式中的實際位置

之後只要透過搜集字串 sh 即可 (<gdb> find sh)，會發現 sh 字串甚至不用跑到 libc 就有了

當時在 local 測試發現 `/bin/sh` 可以 work 但是無法在遠端 work

後來只有用 `sh` 字串即可
