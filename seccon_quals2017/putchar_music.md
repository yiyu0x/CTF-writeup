![](https://i.imgur.com/B51DJ9w.png)

source code
```c
main(t,i,j){unsigned char p[]="###<f_YM\204g_YM\204g_Y_H #<f_YM\204g_YM\204g_Y_H #+-?[WKAMYJ/7 #+-?[WKgH #+-?[WKAMYJ/7hk\206\203tk\\YJAfkkk";for(i=0;t=1;i=(i+1)%(sizeof(p)-1)){double x=pow(1.05946309435931,p[i]/6+13);for(j=1+p[i]%6;t++%(8192/j);)putchar(t>>5|(int)(t*x));}}
```

排版
```c
main(t,i,j){
	unsigned char p[]="###<f_YM\204g_YM\204g_Y_H #<f_YM\204g_YM\204g_Y_H #+-?[WKAMYJ/7 #+-?[WKgH #+-?[WKAMYJ/7hk\206\203tk\\YJAfkkk";
	for(i=0;t=1;i=(i+1)%(sizeof(p)-1)){
		double x=pow(1.05946309435931,p[i]/6+13);
		for(j=1+p[i]%6;t++%(8192/j);)
			putchar(t>>5|(int)(t*x));
	}
}
```
整理一下
```c
#include <stdio.h>
#include <math.h>
int main(int t,int i,int j){
   unsigned char p[]="###<f_YM\204g_YM\204g_Y_H #<f_YM\204g_YM\204g_Y_H #+-?[WKAMYJ/7 #+-?[WKgH #+-?[WKAMYJ/7hk\206\203tk\\YJAfkkk"; 
   for(i=0;t=1;i=(i+1)%(sizeof(p)-1)){ 
      double x=pow(1.05946309435931,p[i]/6+13); 
      for(j=1+p[i]%6;t++%(8192/j);) 
         putchar(t>>5|(int)(t*x));
   }
}
```
執行以後是斷斷續續的聲音

題目提示 Please answer the flag as SECCON{MOVIES_TITLE}

google: putchar music

第一個結果 (https://youtu.be/L9KLnN0GczI)

聽一聽 想了又想

MOVIES_TITLE有兩個字節

猜電影通常是非常有名的電影

然後又是這種(影片音樂)懷舊電子訊音樂

直覺想到STAR WAR (而且又是兩個字節)

通靈解題XD
