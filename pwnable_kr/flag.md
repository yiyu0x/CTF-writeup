
先執行

印出:
`I will malloc() and strcpy the flag there. take it.`

用gdb追一下

```
gdb-peda$ start
I will malloc() and strcpy the flag there. take it.
[Inferior 1 (process 24142) exited normally]
Warning: not running or target is remote
```

追不出東西

> strings flag

發現結尾是`UPX!`(有加殼)

> upx -d flag 

用gdb追一下就看到flag了

![](https://i.imgur.com/UOCFqbw.png)
