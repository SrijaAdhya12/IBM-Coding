import bisect
def getNumberOfPairs(arr,lowerlimit, upperlimit):
    arr.sort()
    n = len(arr)
    count = 0
    for i in range(n):
        low = lowerlimit -  arr[i]
        upper = upperlimit - arr[i]

        left = bisect.bisect_left(arr, low)
        right = bisect.bisect_right(arr, upper) -1

        if left <= right:
            count += (right-left+1)

    return count


arr = [4,6,8,15]
lowerlimit = 18
upperlimit = 28
print(getNumberOfPairs(arr,lowerlimit,upperlimit))

