#include <stdio.h>
int T;

int main() {
	int num[10];
	int sum;

	freopen("È¦¼ö.txt", "r", stdin);
	scanf("%d", &T);
	int n = 0;


	for (int tc = 1; tc <= T; tc++) {

		sum = 0;

		for (int t=0; t < 10; t++) {
			scanf("%d", &num[t]);
	}	

		for (int i = 0; i < 10; ++i) {

			if (num[i]%2==1) {
				sum += num[i];
			}
		}

		printf("#%d %d \n", tc, sum);

	}

	
}