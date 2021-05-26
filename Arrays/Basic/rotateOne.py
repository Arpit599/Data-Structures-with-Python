def rotate( arr, n):
    temp = arr.pop()
    arr.insert(0, temp)
    return arr
    
#  Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1

if __name__ == "__main__":
    main()