class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)//3
        res={}
        final=[]
        for i in arr:
            if(i in res):
                res[i]+=1
            else:
                res[i]=1
        for i,count in res.items():
            if(count>n):
                final.append(i)
        final.sort()
        return final


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
