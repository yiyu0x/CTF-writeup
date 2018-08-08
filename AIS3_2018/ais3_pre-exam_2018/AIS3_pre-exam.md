# AIS3_pre-exam_2018 write-up

***詳細payload script都在對應題目的目錄夾下***

# WEB

### warm up 
---

題目 [link](http://104.199.235.135:31331)

點進去直接被跳到 `http://104.199.235.135:31331/index.php?p=7`

用 curl 看也沒收穫 都是顯示`Did you see the flag? `

後來用 curl -I 看也沒啥特別

但是看被跳轉後的那頁發現一個奇怪欄位 Partial-Flag: 0

於是改GET參數 從0一路追到44 把每一次 Partial-Flag 欄位的value取出來就是FLAG

```bash
~ » curl http://104.199.235.135:31331/index.php\?p\=7 -I                                                             yiyuchang@macbook-yiyu
HTTP/1.1 200 OK
Date: Tue, 05 Jun 2018 06:22:04 GMT
Server: Apache/2.2.15 (CentOS)
X-Powered-By: PHP/5.3.3
Partial-Flag: 0
Connection: close
Content-Type: text/html; charset=UTF-8
```

### hidden

題目 [link](http://104.199.235.135:31332)

先看robots.txt

看到 `Disallow: /_hidden_flag_.php`

進去後發現會有一個按鈕顯示顯示 `GET flag in the next page.`

看一下原始碼

```html
<input type="hidden" name="c" value="1"/>
<input type="hidden" name="s" value="3241b876891b9ea67db897e940db6ea9e7e351447546b8da82bbf3693dfe9ebb"/>
```

然後發現每一次點擊按鈕 c的值會加1 s的值會變

但是手動改c會被跳回1 要正確往下的話兩個值都要正確

於是寫script連續發POST request

跑了幾分鐘後也沒線索

然後又在header發現

`Flag: AIS3{NOT_A_VALID_FLAG}`

於是又再跑一次 最後在 17331 發現真實 Flag

提供一下 17331 前幾筆數據 (格式為c,s,header)

```
17328 9dcc11f04d350a593ce36298c6690b7792a3bbfcb2c68a1f6b4ed97241b576e7
AIS3{NOT_A_VALID_FLAG}
17329 98d1bc462e1140a408e7f0f84c87ab322061cce557813aee035fe9d4dc15e554
AIS3{NOT_A_VALID_FLAG}
17330 5c666c2274eb495fab10d45415c12625f2ea248a66b8dcc0a681e4852591854f
AIS3{NOT_A_VALID_FLAG}
```

### sushi

```php
<?php
highlight_file(__FILE__);
$_ = $_GET['🍣'];

if( strpos($_, '"') || strpos($_, "'") )
    die('Bad Hacker :(');
eval('die("' . substr($_, 0, 16) . '");');
?>

```
題目 [link](http://104.199.235.135:31333/)

前面兩個過濾用url encode就繞得過

但是 `die()` 好像繞不過(die = echo + exit) 於是方向朝直接執行函式

查到[這篇](https://stackoverflow.com/questions/12636586/what-is-phpinfo-called-remote-command-execution-related)

> ${phpinfo()} 

丟進去 未顯示內容(被解析成功)

> {${phpinfo()}}

成功

之後用 `?🍣={${exec(ls)}}` 沒東西 

用 `?🍣={${exec(%22ls%22)}}` 還會跑出 `Bad Hacker :(`

後來改用 `?🍣={${system(ls)}}` 出現三個檔案

```
flag_name_1s_t00_l0ng_QAQQQQQQ
index.php
phpinfo.php
```
還試了很久想說要怎麼繞過長度 去讀flag

結果直接讀就出來了

> http://104.199.235.135:31333/flag_name_1s_t00_l0ng_QAQQQQQQ

有時候把事情想的太複雜 少給自己太多方向QQ

法二



".\`ls\`."



原因是"的位置在0 所以if那邊不會跳進去

### perljam

題目 [link](http://104.199.235.135:31334/)

先githack出整個目錄

然後發現一個備份檔(.bak) 

找到這題 [github_link](https://github.com/73696e65/ctf-notes/blob/master/2016-ctf.csaw.io/web-200-i_got_id.md)

改封包

用burp發request 然後改POST 加上boundary

讀/etc/passwd 確定可行之後

![](https://i.imgur.com/BQULWLL.png)

在根目錄找到flag 但是讀不出來(權限問題,一開始還以為是擋cat 但是用head也不行)

然後看到readflag.c看一下就懂了

執行readflag

![](https://i.imgur.com/Gy5wA6r.png)

# REVERSE

### find

> strings find-11660a2662f5578190d4a4eea830a5d9000d44b9366a1b60f0c95550294ff825 | grep AIS3

![](https://i.imgur.com/78KVznh.png)

> strings find-11660a2662f5578190d4a4eea830a5d9000d44b9366a1b60f0c95550294ff825 | grep ais3
![](https://i.imgur.com/ZGncHHw.png)

後來把檔名hex decode變成`7869606878885897415887933177281712082496660557250946215025182688848078960677`

每三個一組在hopper裡面追label

第二個s96那邊找到flag

***後來得知grep AIS3就有flag了***

```
~/Downloads » strings find-11660a2662f5578190d4a4eea830a5d9000d44b9366a1b60f0c95550294ff825 | grep "AIS3{[[a-zA-Z].*}"
AIS3{StrINg$_And_gR3P_I5_U$eFu1}
```

開賽時很急 沒檢查清楚......

### secret

先逆向 發現是亂數比較

然後gdb玩一玩

發現每一次亂數結果會存在rcx

重追的過程發現一次亂數結果居然是一樣的

仔細看逆向後的c code發現是偽亂數

自己寫一個一樣的code產生完亂數 把執行結果pipe給執行檔

記得偽亂數`rand(0)`的產生跟系統有關 產生的時候要用ubuntu

題目說是ubuntu17

但是我用 ubuntu16.04 也產生一樣的 (gcc版本我連看都沒看)

# PWN

### mail

先gdb

info func看見replay

用cyclic塞

找出 offset 是 40

直接讓他跳到`0x0000000000400796`(replay的位置)

寫exploit 收工

### darling

賽後才解出

out of bound漏洞 

有檢查上限沒檢查下限 輸入index讓他跳到

printf的ret address 然後把值蓋成shell function的記憶體位置

關鍵code (comment自己加的 題目沒給):

```c
    scanf("%lld", &pair[idx]);//0x7fffffffe2f0

    for(int i=0; i<8; i++){
      if(code[i] == pair[idx]){
        printf(">> %3lld %16s\n", code[i], parasite[i]);
        break;
      }
    }
    printf("Are you sure ? (yes:1 / no:0) ");//ret --> 0x7fffffffe2c8
    
    //ret --> 0x7fffffffe2c8 --> 這個位置可以追進去printf@plt 然後馬上看stack頂層
    
```
    //0x7fffffffe2f0 - 0x7fffffffe2c8 = 40
    //64-bits --> 40/8 = 5
    //因為一開始輸入1 所以其實是差5個
    //payload
    //先輸入 -5
    //再輸入 0x00000000004007d6  debug  ("%lld") --> 所以是4196310
 
![](https://i.imgur.com/wuKIUk8.png)

# MISC

### welcome

簽到題

### flags

檔名太長 以下用`flags.jpg`代稱

> binwalk flags.jpg


```

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
48932         0xBF24          Zip archive data, at least v1.0 to extract, name: backup/
48997         0xBF65          Zip archive data, encrypted at least v2.0 to extract, compressed size: 24, uncompressed size: 29, name: backup/flag
49106         0xBFD2          Zip archive data, encrypted at least v2.0 to extract, compressed size: 124048, uncompressed size: 148837, name: backup/Avengers_Infinity_War_Poster.jpg
173534        0x2A5DE         End of Zip archive

```

分離

dd if=flags.jpg of=output skip=48932 bs=1

上網找那個檔名的電影海報

造一個一樣的壓縮檔 

backup/Avengers_Infinity_War_Poster.jpg

> zip plaintext.zip "backup/Avengers_Infinity_War_Poster.jpg"

然後明文攻擊 

>pkcrack -C flags.zip -c "backup/Avengers_Infinity_War_Poster.jpg" -P plaintext.zip -p "backup/Avengers_Infinity_War_Poster.jpg" -d decrypted.zip -a

解開後發現是假flag

一直到隔天晚上才發現0 byte那邊真的有圖 

但是strings後也是假flag

最後看很久才發現是摩斯密碼(要放大看 而且解析度很低)

![](https://i.imgur.com/Q5DlkjZ.png)

### svega

以下將檔名代稱為`file.mp3`

先 file 看一下 是mp3檔

找工具 [this](https://m3tar.github.io/2017/08/20/%E9%9F%B3%E9%A2%91%E9%9A%90%E5%86%99-MP3stego-wav%E9%9A%90%E5%86%99-%E9%A2%98%E7%9B%AE/)

指令

Decode -X file.mp3

然後隨便輸入密碼 就會噴出txt(flag)

(唯一用到windows的一題)

# CRYPTO

### pow

proof of work

[挖矿与共识](http://book.8btc.com/books/1/master_bitcoin/_book/8/8.html)

裡面範例code改一改勉強能動

不知道是不是macbook air運算能力太差

每一次都花超過1分鐘才算出來

後來試了將近10次才成功
