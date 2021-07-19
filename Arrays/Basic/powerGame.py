# arr = [0] * 10

# def getFreq(x, n):
#     # code here
#     for i in range(1, n + 1):
#         num = pow(x, i)
#         while(num > 0):
#             res = num % 10
#             arr[res] += 1
#             num = int(num / 10)

#     return arr 

# #  Driver Code Starts
# if __name__ == '__main__':
#     tc = int(input("Enter the number of test cases: "))
#     while tc > 0:
#         x, n = list(map(int, input("Enter x and n: ").strip().split()))

#         ans = getFreq(x, n)
#         for x in ans:
#             print(x,end=" ")
#         tc -= 1

arr = []
tempArr = [0] * 10
def getFreq(x, n):
    # code here
    arr = []
    for i in range(1, n + 1):
        num = pow(x, i)
        while(num > 0):
            res = num % 10
            arr.append(res)
            num = int(num / 10)
    arr.sort()        
    for i in arr:
        tempArr[i] += 1
    return tempArr 

#  Driver Code Starts
if __name__ == '__main__':
    tc = int(input("Enter the number of test cases: "))
    while tc > 0:
        x, n = list(map(int, input("Enter x and n: ").strip().split()))

        ans = getFreq(x, n)
        for x in ans:
            print(x, end=" ")
        tc -= 1