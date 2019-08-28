def isfull():
    return (rear+1)%len(Q) == front

def isEmpty():
    return front == rear

def enQueue(item):
    global rear
    if isfull() :
        print("큐 풀")
    else :
        rear = (rear+1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("비울게 없음")
    else:
        front = (front + 1) % len(Q)
        return Q[front]

def Qpeek():
    if isEmpty() :
        print("큐 빔")
    else:
        return Q[(front+1) % len(Q)]

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