# https://www.geeksforgeeks.org/problems/second-largest3735/1

def getSecondLargest(arr):
        # Code Here
        first = arr[0]
        second = -1
        for i in arr:
            if i > first:
                first = i
        
        
        for i in arr:
            if i > second and i < first:
                second = i

        return second

print(getSecondLargest([12, 35, 1, 10, 34, 1]))