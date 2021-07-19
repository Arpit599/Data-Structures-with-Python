
#Function to generate binary numbers from 1 to N using a queue.
def generate(N):
    # code here
    queue = []
    queue.append("1")
    res = []
    
    while(1):
        ele = queue.pop(0)
        res.append(ele)
        ele1 = ele + "0"
        ele2 = ele + "1"
        queue.append(ele1)
        queue.append(ele2)
        if(len(res) == N):
            break
    return res
        
        
#  Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
