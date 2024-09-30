def guessTheDataStructure(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    i = 0
    while i < len(lines):
        isQueue = True
        isStack = True
        isPriorityQueue = True

        queue = []
        stack = []
        priorityQueue = []

        n = int(lines[i])
        i += 1

        for _ in range(n):
            command, value = lines[i].split()
            value = int(value)
            if command == "1":
                queue.append(value)
                stack.append(value)
                priorityQueue.append(value)
            elif command == "2":
                if isQueue:
                    if queue and value == queue[0]:
                        queue.pop(0)
                    else:
                        isQueue = False
                if isStack:
                    if stack and value == stack[-1]:
                        stack.pop()
                    else:
                        isStack = False
                if isPriorityQueue:
                    if priorityQueue and value == max(priorityQueue):
                        priorityQueue.pop(
                            priorityQueue.index(max(priorityQueue)))
                    else:
                        isPriorityQueue = False

            i += 1

        if isPriorityQueue and not isStack and not isQueue:
            print("priority queue")
        elif isQueue and not isStack and not isPriorityQueue:
            print("queue")
        elif isStack and not isQueue and not isPriorityQueue:
            print("stack")
        elif not isQueue and not isStack and not isPriorityQueue:
            print("impossible")
        else:
            print("not sure")


fileName = "HW3_Q4_input.txt"
guessTheDataStructure(fileName)
