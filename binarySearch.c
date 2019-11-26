//program to demostrate binary search
#include<stdio.h>

int bsearch(int arr[], int l, int r, int x)
{
	if(r >= l)
	{
		int mid = l + (r - l) / 2;
	
		if(arr[mid] == x)
			return mid;
		
		if(arr[mid] > x)
			return bsearch(arr, l, mid-1, x);
		
		if(arr[mid] < x)
			return bsearch(arr, mid+1, r, x);
	}	
	return -1;
}

int main()
{
	int arr[] = {1,2,3,4,5,6};
	int x = 7;
	int n = sizeof(arr)/sizeof(arr[0]);
	int result = bsearch(arr,0,n-1,x);
	(result == -1) ? printf("Element is not present in array") : printf("Element is present at index %d",result);
	return 0;
}
