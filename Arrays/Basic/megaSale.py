def maxProfit( a, n, m):
    sum = 0
    a.sort()
    count = 0
    for i in range(n):
        if((count < m) and a[i] < 0):
            count += 1
            sum += abs(a[i])
    return sum

N=5
M=10
a = [1, -2, -3, -4, 5]

maxProfit(a, n, m)