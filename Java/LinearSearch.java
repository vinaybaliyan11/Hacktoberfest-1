import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scan=new Scanner(System.in);
		System.out.println("Enter the size");
		int n=scan.nextInt();
		int[] ar=new int[n];
		int i,k=-1,s;
		System.out.println("Enter the elements in array");
		for(i=0;i<n;i++)
		    ar[i]=scan.nextInt();
		System.out.println("Enter the element to search");
		s=scan.nextInt();
		for(i=0;i<n;i++){
		    if(ar[i]==s){
		        k=i;
		        break;
		    }
		}
		if(k!=-1)
		System.out.println(s+" is present at index "+k);
		else
		System.out.println(s+" is not present");
	}
}