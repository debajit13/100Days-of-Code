//program to implement selection sort
#include<stdio.h>

void swap(int *xp, int *yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

void printArray(int arr[], int SIZE)
{
	int i;
	for(i = 0; i < SIZE; i++)
		printf("%d\n",arr[i]);
}

void selectionSort(int arr[],int n)
{
	int i,j,min_idx;
	for(i = 0; i < n-1; i++)
	{
		//find the minimum element in unsorted array
		min_idx = i;
		for(j = i+1; j < n; j++)
			if(arr[j] < arr[min_idx])
				min_idx = j;
				
		//swap the found minimum element with the first element		
		swap(&arr[min_idx],&arr[i]);
	}
}

int main()
{
	int arr[] = {6,5,4,3,2,1};
	int n = sizeof(arr)/sizeof(arr[0]);
	selectionSort(arr,n);
	printf("Sorted Array : \n");
	printArray(arr,n);
	return 0;
}
