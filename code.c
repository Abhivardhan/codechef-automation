#include<stdio.h>
#include<stdbool.h>

int main(void) {
	
	while(true) {
		int num;
		scanf("%d",&num);
		
		if(num == 42) {
			break;
		} else {
			printf("%d\n", num);
		}
	}
}
