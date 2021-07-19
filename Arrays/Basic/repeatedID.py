def uniqueId(a, n):
    list = [-1] * 10
    newList = []
    for i in range(n):
        if(list[int(a[i])] == -1):
            list[int(a[i])] += 1
            newList.append(a[i])
    return newList

N = 5
a = [8, 8, 6, 2, 1]

print(uniqueId(a, N))