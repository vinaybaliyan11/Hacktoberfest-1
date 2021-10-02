#include <iostream>
#include <cstring>
using namespace std;

bool isPermutation(char input1[], char input2[]) {
    // Write your code here
  int arr[256] = {0};
    int i=0,j=0;
    long c=0;
    if(strlen(input1)!=strlen(input2))
        return false;
    
  while(input1[i]!='\0' && input2[j]!='\0')
  {
      int z = input1[i];
      arr[z]++;
      int a = input2[j];
      arr[a]++;
      i++;
      j++;
  }
    for(int i=97;i<=122;i++)
    {
        if(arr[i]%2==0 && arr[i]!=0)
            c=c+(arr[i]/2);
        
    }

    if(c==i)
        return true;
    else
        return false;
}

int main() {
    int size = 1e6;
    char str1[size];
    char str2[size];
    cin >> str1 >> str2;
    cout << (isPermutation(str1, str2) ? "true" : "false");
}
