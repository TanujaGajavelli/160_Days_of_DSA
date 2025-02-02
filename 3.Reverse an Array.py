class Solution:
    def reverseArray(self, arr):
        for i in range(len(arr) // 2):
            tmp = arr[i]
            arr[i] = arr[len(arr) - i - 1]
            arr[len(arr) - i - 1] = tmp
        return arr
import sys

def main():
    # Read the number of test cases
    tc = int(sys.stdin.readline())

    while tc > 0:
        # Read the array elements as a string
        str_arr = sys.stdin.readline().split()

        # Convert the string array to an integer array
        arr = [int(x) for x in str_arr]

        # Create a Solution object
        obj = Solution()

        # Reverse the array
        obj.reverseArray(arr)

        # Print the reversed array
        for i in range(0, len(arr)):
            print(arr[i], end=" ")
        print()
        print("~")

        # Decrement the test case count
        tc -= 1
