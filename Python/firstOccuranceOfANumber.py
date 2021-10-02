def firstoccurance(arr,si,x):
    #function returns first index of an element in an array
    if  si==len(arr):
        return -1
    if x==arr[si]:
        return si
    induction=firstoccurance(arr,si+1,x)
    return induction
arr=[int(x) for x in input().split()] #input array
s=int(input()) #s is the element to be searched
print(firstoccurance(arr,0,s))
        