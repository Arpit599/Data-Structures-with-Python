def findMax(n, m,a, b, k):

    list = [0] * (n + 1)
    length = len(a)
    #print("Length of a " + str(length))
    for i in range(m):
        index = i % length
        lowerbound = a[index]
        upperbound = b[index] + 1
        
        list[lowerbound] += k[index]
        list[upperbound] -= k[index]
        
    max = list[0]
    for i in range(1, n):
        list[i] += list[i-1]
        if(max <= list[i]):
                max = list[i]
        #print(list)
    return max

n = 5
a = [0, 1, 2]
b = [1, 4, 3]
k = [100, 100, 100]

m = len(a)
		
print("Maximum value after","'m' operations is", findMax(n, m, a, b, k))