class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        res = set(arr)
        maxe = max(res)
        res.remove(maxe)
        if len(res) >= 1:
            return max(res)
        else:
            return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
