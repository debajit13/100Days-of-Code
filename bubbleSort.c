//program to demostrate bubble sort algorithm
#include<stdio.h>
void swap(int *xp,int *yp)
{
	int temp;
	temp = *xp;
	*xp = *yp;
	*yp = temp;
}
//function to implement print the array
void printArray(int arr[],int SIZE)
{
	int i;
	for(i = 0; i < SIZE; i++)
		printf("%d\n",arr[i]);
}
//function to implement bubble sort algorithm
void bubbleSort(int arr[],int n)
{
	int i,j;
	for(i = 0; i < n-1; i++)
		for(j = 0; j < n-i-1; j++)	
			if(arr[j] > arr[j+1])
				swap(&arr[j],&arr[j+1]);
}
//main function
int main()
{
	int arr[] = {2,5,1,3,6};
	int n = sizeof(arr)/sizeof(arr[0]);
	bubbleSort(arr, n);
	printf("Sorted Array: \n");
	printArray(arr,n);
	return 0;
}
