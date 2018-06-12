
#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 

int main(){

	int number;
 	srand(0);
 	for(int i=0;i<86;i++){
 		number = rand()%2018;
 		printf("%d\n",number);
 	}
}

	