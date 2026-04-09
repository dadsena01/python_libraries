from collections import deque

train = deque(["truck", "car", "bike"])
train.append("plane")
train.appendleft("boat")
train.pop()
train.pop()
train.append("ship")
print(train)

num = deque(["1", "2", "3"])
print(num)
num.append("4")
print(num)
num.appendleft("0")
print(num)
num.popleft()
print(num)
num.pop()
print(num)


dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)
print(dq)
dq.rotate(-2)
print(dq)


list = deque(maxlen=3)
list.extend([1, 2, 3])
list.append(4)
print(list)
