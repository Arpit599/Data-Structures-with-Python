def findFirstIndex(arr, x, low, high, first):
    mid = int((high + low)/2)
    #Base Case
    if(low <= high):
        if(arr[mid] == x) and (mid < first):
            first = mid
        if(arr[mid] >= x):
            first = findFirstIndex(arr, x, low, mid - 1, first)
        if(arr[mid] < x):
            first = findFirstIndex(arr, x, mid + 1, high, first)
    return first

def findLastIndex(arr, x, low, high, last):
    mid = int((high + low)/2)
    #Base Case
    if(low <= high):
        if(arr[mid] == x) and (mid > last):
            last = mid
            last = findLastIndex(arr, x, mid + 1, high, last)
        if(arr[mid] > x):
            last = findLastIndex(arr, x, low, mid - 1, last)
        if(arr[mid] <= x):
            last = findLastIndex(arr, x, mid + 1, high, last)
    return last
    
def find(arr, n, x):
    low = 0
    high = n - 1
    #Initialized with these for satisfying the conditions in the functions above
    first, last = n + 1, -1
    first = findFirstIndex(arr, x, low, high, first)
    last = findLastIndex(arr, x, low, high, last)

    if(first == n + 1) or (last == n + 1):
        return [-1, -1]
    else:
        return [first, last]

def findFirstIndex(arr, x, low, high, first):
    mid = int((high + low)/2)
    #Base Case
    if(low <= high):
        if(arr[mid] == x) and (mid < first):
            first = mid
        if(arr[mid] >= x):
            first = findFirstIndex(arr, x, low, mid - 1, first)
        if(arr[mid] < x):
            first = findFirstIndex(arr, x, mid + 1, high, first)
    return first

def findLastIndex(arr, x, low, high, last):
    mid = int((high + low)/2)
    #Base Case
    if(low <= high):
        if(arr[mid] == x) and (mid > last):
            last = mid
            last = findLastIndex(arr, x, mid + 1, high, last)
        if(arr[mid] > x):
            last = findLastIndex(arr, x, low, mid - 1, last)
        if(arr[mid] <= x):
            last = findLastIndex(arr, x, mid + 1, high, last)
    return last
    
def find(arr,n,x):
    # code here
    low = 0
    high = n - 1
    first, last = n + 1, -1
    first = findFirstIndex(arr, x, low, high, first)
    last = findLastIndex(arr, x, low, high, last)

    if(first == n + 1) or (last == n + 1):
        return [-1, -1]
    else:
        return [first, last]

#  Driver Code 
t = int(input())
for _ in range(0, t):
    l = list(map(int, input().split()))
    n = l[0]
    x = l[1]
    arr = list(map(int, input().split()))
    ans = find(arr, n, x)
    print(*ans)
