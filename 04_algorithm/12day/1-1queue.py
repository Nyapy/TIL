def isfull():
    if rear == SIZE-1:
        return True
    else:
        return False

def isEmpty():
    if front == rear:
        return True
    else:
        return False

def enQueue(item):
    global rear
    if isfull() :
        print("큐 풀")
    else :
        rear +=1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("비울게 없음")
    else:
        front +=1
        return Q[front]

def Qpeek():
    if isEmpty() :
        print("큐 빔")
    else:
        return Q[front+1]
SIZE = 100

Q = [0]*SIZE
front, rear = -1, -1

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())