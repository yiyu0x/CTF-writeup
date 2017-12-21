![](https://i.imgur.com/Ns0Xo9u.png)

提交頁面http://sha1.pwn.seccon.jp/

SHA1碰撞 並且要符合 2017KiB < file,file2 < 2018KiB

SHA碰撞非常有名 google成功碰撞後有提供兩個pdf檔 (https://shattered.io/)

```單位換算
1KB = 1,000 Byte
1MB = 1,000 KB
1GB = 1,000,000 KB
1TB = 1,000,000,000 KB

1KiB = 1,024Byte
1MiB = 1,024KiB
1GiB = 1,024MiB = 1,048,576 KiB
1TiB = 1,024GiB = 1,073,741,824 KiB
```

驗證一下

 yiyu ⮀ SHA1 ⮀ shasum shattered-1.pdf
 
38762cf7f55934b34d179ae6a4c80cadccbb7f0a  shattered-1.pdf

 yiyu ⮀ SHA1 ⮀ shasum shattered-2.pdf
 
38762cf7f55934b34d179ae6a4c80cadccbb7f0a  shattered-2.pdf

確認檔案存在碰撞

yiyu ⮀ SHA1 ⮀ du -k shattered-1.pdf
416     shattered-1.pdf

pdf1 is 422,435 byte

we need: 

more then `2065408 byte`

less then `2066432 byte`

middle is `2065920 byte`


2065920-422,435=1643485 byte

```
yiyu ⮀ SHA1 ⮀ dd if=/dev/zero of=ctf bs=1 count=1643485
1643485+0 records in
1643485+0 records out
1643485 bytes transferred in 3.409297 secs (482060 bytes/sec)
yiyu ⮀ SHA1 ⮀ cat ctf >> shattered-1.pdf
yiyu ⮀ SHA1 ⮀ cat ctf >> shattered-2.pdf
```

提交:

![](https://i.imgur.com/lRpuiet.png)
