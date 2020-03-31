import numpy as np

grid =np.array([[1,2,3,4,5,6,7,8,9],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]])

def getRowKeys(k):
    l =[]
    print(k)
    start = (k//9) * 9
    print(start)
    for i in range(start,start + 9):
        l.append(i)
    l.remove(k)
    return l

def getColKeys(k):
    l =[]
    start = k%9
    for i in range(start,81,9):
        l.append(i)
    l.remove(k)
    return l

def getBoxKeys(k):
    l=[]
    start = (((k//9)//3)*27) + (((k%9)//3)*3)
    for i in range(start,start + 27,9):
        for j in range(i,i+3):
            l.append(j)
    l.remove(k)
    return l

print(getRowKeys(40))
print(getColKeys(40))
print(getBoxKeys(40))