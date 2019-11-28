//program to demostrate insertion sort
#include<stdio.h>
//function to print array
void printArray(int arr[], int SIZE)
{
	int i;
	for(i = 0; i < SIZE; i++)
		printf("%d\n",arr[i]);
}
//function of insertion sort
void insertionSort(int arr[], int n)
{
	int i,j,key;
	for(i = 1; i < n; i++)
	{
		key = arr[i];
		j = i - 1;
		
		while(j>=0 && arr[j]>key)
		{
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
	}
}
//main function
int main()
{
	int arr[] = {2,1,5,4,3};
	int n = sizeof(arr)/sizeof(arr[0]);
	insertionSort(arr,n);
	printf("Sorted elements :\n");
	printArray(arr,n);
	return 0;
}
