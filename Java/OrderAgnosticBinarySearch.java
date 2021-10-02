package BinarySearchCode;

public class OrderAgnosticBinarySearch {
    public static void main(String[] args) {
        int[] arr = {99,88,77,66,34,28,19,15,9,-1,-20,-30};
        int target = 66;
        int ans = orderAgnosticBS(arr,target);
        System.out.println(ans);
    }
    static int orderAgnosticBS(int[] arr, int target){
        int start = 0;
        int end = arr.length - 1;

        // find whether array is in sorted ascending or sorted descending order
        boolean isAscending = arr[start] < arr[end];

        while(start <= end){
            // here we will not do int mid = (start + end) / 2;
            // might be possible that (start + end) exceeds the range of int in java
            // so better way is as below to find middle element
            int mid = start + (end-start) / 2;
            // if element is equal to target element then return that index of element
            if(arr[mid] == target){
                return mid;
            }

            if(isAscending) {
                if (target < arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                if (target < arr[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        // if element not found then return -1
        return -1;
    }
}

/*
Time Complexity 
Best Case :- O(1)
Worst Case :- O(log n)
*/