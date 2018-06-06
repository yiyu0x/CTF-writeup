```c
#include <stdio.h>
int main(){
	unsigned int random;
	random = rand();	// random value!
	unsigned int key=0;
	scanf("%d", &key);
	if( (key ^ random) == 0xdeadbeef ){
		printf("Good!\n");
		system("/bin/cat flag");
		return 0;
	}
	printf("Wrong, maybe you should try 2^32 cases.\n");
	return 0;
}
```

偽亂數，自己找一台ubuntu產生一下亂數

然後跟`0xdeadbeef` XOR 一下

```
>>> 0xdeadbeef ^ 1804289383
3039230856
```

收工
