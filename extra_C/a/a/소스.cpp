#include <stdio.h>
int N;

int main()
{
	scanf("%d", &N);

	printf("%d \n", N);

	for (int t = N; t >= 0; t--)
	{
		printf("%d ", t);
	}

	return 0;
}