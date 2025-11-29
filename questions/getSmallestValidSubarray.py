
def getSmallestValidSubarray(arr, k):
    n = len(arr)
    pos = [0]*(n+1)

    for k,v in enumerate(arr):
        pos[v] = k

    ans = float("inf")

    for start in range(1,n-k+2):
        end = start + k -1

        left = float("inf")
        right = float("-inf")

        for v in range(start, end+1):
            p = pos[v]
            if p < left:
                left = p
            if p > right:
                right = p

    ans = min(ans, right-left+1)
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(getSmallestValidSubarray(arr, k))