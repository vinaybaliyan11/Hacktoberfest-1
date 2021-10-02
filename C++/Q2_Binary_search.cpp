#include <bits/stdc++.h>
using namespace std;
int search(int arr[], int l, int h, int key)
{
    if (l > h) return -1;
    int mid = (l+h)/2;
    if (arr[mid] == key) return mid;
    if (key >= arr[mid] && key <= arr[h])
        return search(arr, mid+1, h, key);
    return search(arr, l, mid-1, key);
}
int main()
{
    int arr[] = {1,2,3,4, 5, 6, 7, 8, 9};
    int n = sizeof(arr)/sizeof(arr[0]);
    int key = 6;
    int i = search(arr, 0, n-1, key);
    if (i != -1)
    cout << "Index: " << i << endl;
    else
    cout << "Key not found";
}
