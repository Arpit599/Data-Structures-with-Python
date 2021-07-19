#Thread 0
flag = [False, False]

while(1):
    flag[0] = True
    turn = 0
    while (turn == 0 and flag[1] == True):
        #thread_stuck
        continue
    #critical section access

    flag[0] = False
    #end

#Thread 1
while(1):
    flag[1] = True
    turn = 1
    while (turn == 1 and flag[0] == True):
        #thread_stuck
        continue
    #critical section
    flag[1] = False
    #end

#Flexible code
while(1):
    flag[t_id] = True
    turn = t_id
    while (flag[t_id] == True and turn == t_id):
        #thread_stuck
        continue
    #critical section access
    flag[t_id] = False
    #end


if currentNode_inUse[0] == currentNode_inUse[1]:
    while lock != 0:
        continue
    lock = 1

    #change the common node here

    lock = 0
    