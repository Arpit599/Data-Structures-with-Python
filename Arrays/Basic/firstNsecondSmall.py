import sys

def minAnd2ndMin( a, n):
    smallest, secondSmallest = sys.maxsize, sys.maxsize
    for i in range(n):
        if(a[i] < smallest):
            secondSmallest = smallest
            smallest = a[i]
        elif(a[i] > smallest and a[i] < secondSmallest):
            secondSmallest = a[i]
            
    if secondSmallest != sys.maxsize:
        return [smallest, secondSmallest]
    else:
        return [-1, -1]

def main():

    T = int(input("Enter the number of test cases: "))

    while(T > 0):
        n = int(input("Enter the size of array: "))
        a = [int(x) for x in input("Enter the array: ").strip().split()]
        
        product = minAnd2ndMin(a, n)
        if product[0]==-1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])
        T -= 1

if __name__ == "__main__":
    main()
