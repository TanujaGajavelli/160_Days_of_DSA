class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	ind=0
    	for i in range(len(arr)):
    	    if(arr[i]!=0):
    	        arr[ind]=arr[i]
    	        ind+=1
    	while(ind<len(arr)):
    	    arr[ind]=0
    	    ind+=1
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
