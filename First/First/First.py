from math import pi
import sys
import numpy as nm


#print ("hello world!")
def computeAvg(a,b,c) :
    return (a + b + c)/3

def doComplexMath() :
    num1 = 3 + 4j
    num2 = 6 + 3.5j
    res = num1 * num2
    return res

def mapTest(mylist) :
    ys = map(lambda x: x * 2, mylist)
    result = []
    for elem in ys:
        result.append(elem)
    return result

def quicksort(arr, i, j):
    if i < j:
        pos = partition(arr, i, j)
        quicksort(arr, i, pos - 1)
        quicksort(arr, pos + 1, j)

def partition(arr, i, j):
    pivot = arr[j]
    small = i - 1
    for k in range(i, j):
        if arr[k] <= pivot:
            small += 1
            swap(arr, k, small)
    
    swap(arr, j, small + 1)
    print("Pivot = " + str(arr[small + 1]))
    printArray(arr)
    return small + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i] #just exchange data in positions i and j

def printArray(arr):
    print(' '.join(str(i) for i in arr))

def main(): 
    arr = [9, 4, 8, 3, 1, 2, 5] 
    print("Initial Array :", printArray(arr)) 
    quicksort(arr, 0, len(arr) - 1)
    
    # fruits = ['apples', 'oranges', 'bananas', 'plums', 'pineapples']
    # print(fruits)
    # pfruits = fruits[2:4]
    # print(pfruits)
    # for fr in pfruits :
    #     print(fr)
    # del fruits[2]
    # fruits.remove('oranges')
    # fruits.append('kiwi')
    # pfruits.append('blood oranges')
    # print(fruits + pfruits)
    # print("\n")
    # s1 = ('john', 'starkey', 12341, 3.5)
    # print(s1[3])

    
    # snum = "25.5"
    # num5 = float(snum)
    # print(num5 + 1.1)

    #msg = """Hello there. How are you?""";
    #print("'How' is found starting in the following position: " + str(msg.lower().find('how')))
    #print(msg[13:16])

    #print("Result = ", computeAvg(5,8,9))
    #print("result complex = ", doComplexMath())

if __name__ == "__main__":
    sys.exit(int(main() or 0))