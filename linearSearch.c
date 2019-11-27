//program to demostrate linear search
#include<stdio.h>
//function to search the element x
int search(int arr[], int n, int x)
{
	int i;
	for(i = 0; i < n; i++)
		if(arr[i] == x)
			return i;
	return -1;
}
//main function
int main()
{
	int arr[] = {1,2,3,4,5,6};
	int x = 10;
	int n = sizeof(arr)/sizeof(arr[0]);
	int result = search(arr,n,x);
	(result == -1) ? printf("Element is not present in array") : printf("Element is present at index %d",result);
	return 0;
}

