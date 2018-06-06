```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}
int main(int argc, char* argv[]){
	if(argc<2){
		printf("usage : %s [passcode]\n", argv[0]);
		return 0;
	}
	if(strlen(argv[1]) != 20){
		printf("passcode length should be 20 bytes\n");
		return 0;
	}
	if(hashcode == check_password( argv[1] )){
		system("/bin/cat flag");
		return 0;
	}
	else
		printf("wrong passcode.\n");
	return 0;
}
```

argv[1]的長度要等於20bytes才能通過檢查

然後argv[1]會被轉成int，每5bytes讀出來做加總

加總結果要等於 0x21DD09EC(568134124)

### 思路

把 568134124 切成五段(滿足20bytes，也比較好控制加總)

但是 568134124/5 除不盡

一開始我用 568134124 - 4 = 568134120

568134120 + 4 = 568134124

```
./col `python -c "print '\x7a\x42\x77\x08'*4 + '\x04\x00\x00\x00' "`
```

乍看起來很合理 但是一直沒成功

查了才知道 4 的 hex 0x4 在丟的過程 (\x04\x00\x00\x00) 會被截斷 (\x00是截斷符號！) [stack_overflow](https://stackoverflow.com/questions/2547349/what-does-x-mean-in-c-c)

所以重新湊了一下

0x21DD09EC - 0x01010101*4 = 0x1dd905e8

0x1dd905e8 + 0x01010101*4 --> 轉little endian --> '\xe8\x05\xd9x\1d' + '\x01\x01\x01\x01'*4

```
./col `python -c "print '\xe8\x05\xd9\x1d' + '\x01\x01\x01\x01'*4" `
```
使用這種方式塞payload時要注要系統python的版本，print的用法不同
