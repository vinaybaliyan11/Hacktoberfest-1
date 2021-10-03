/*import java.util.Arrays;

public class MergeSort {
	public static void main(String[] args) {
		int[] arr1= {1,4,8,10,13,17};
		int[] arr2= {2,3,5,7,9,11,12};
		int arr3[]=mergerSort(arr1,arr2);
		System.out.println(Arrays.toString(arr3));
	}

	public static int[] mergerSort(int[] arr1, int[] arr2) {
		int[] arr=new int[arr1.length+arr2.length];
		int i=0,j=0,k=0;
		
		while(i<arr1.length && j<arr2.length)
		{
			
			if(arr1[i]<=arr2[j])
			{
				arr[k]=arr1[i];
				i++;k++;
			}
			else 
			{
				arr[k]=arr2[j];
				j++;k++;
			}
		}
		while(i<arr1.length)
		{
			arr[k]=arr1[i];
			i++;k++;
			
		}
		while(j<arr2.length) 
		{
			arr[k]=arr2[j];
			j++;k++;
		}
		return arr;
	}

}*/
public class solution {
       public static void merge(int []arr,int l,int m,int r){
        int n1 = m - l + 1;
        int n2 = r - m;
  
        /* Create temp arrays */
        int L[] = new int[n1];
        int R[] = new int[n2];
  
        /*Copy data to temp arrays*/
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];
  
        /* Merge the temp arrays */
  
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;
  
        // Initial index of merged subarray array
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
  
        /* Copy remaining elements of L[] if any */
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
  
        /* Copy remaining elements of R[] if any */
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
public static void mergeSort(int []arr,int l,int r){
  
    if(l<r)
    {
       
            // Find the middle point
            int m =l+ (r-l)/2;
  
            // Sort first and second halves
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
  
            // Merge the sorted halves
            merge(arr, l, m, r);
        
    }
}
 
	public static void mergeSort(int[] input){
         if(input.length==1 || input.length==0)
        return;
        
		mergeSort(input,0,input.length-1);
     
       
	}
}

