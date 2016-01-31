#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
	int *pvec = (int*)  malloc(sizeof(int)*1000000);
	int i,y;
	for (i = 0; i < 1000000; i++)
		pvec[i] = 1;
	pvec[0] = 0;
	pvec[1] = 0;
	for (i = 0; i < 1000; i++) {
		if(pvec[i]==0)
			continue;
		y = 2;
		while(i*y<1000000)
			pvec[i*y++] = 0;
	}
	int curr,currp,ok;
	double tmp;
	for(i = 0; i < 1000000; i++) {
		if(pvec[i]) 
			printf("%d\n",i);
	}
	return 0;
	for (i = 9; i < 1000000; i = i + 2) {
		if(pvec[i]) continue;
		curr = i;
		currp = 2;
		ok = 0;
		while (curr - currp > 0) {
			tmp = sqrt(((curr-currp)/2));
			if(tmp - floor(tmp) < 0.00001) {
				ok = 1;
				break;
			}
			while(pvec[++currp]!=1)
				printf("%d\n",currp);
		}
		if(ok==0) {
			printf("broke in %d\n",i);
			break;
		}
	}
	return 0;
}
