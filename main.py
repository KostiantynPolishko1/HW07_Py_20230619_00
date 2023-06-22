import random

while True:
    print("0 - EXIT!")
    intN = abs(float(input("\nEnter number of task 1...6: ")))
    intN = int(intN)

    if intN == 0:
        print("\nTHE END!")
        break
    elif intN > 6:
        print("Number is out of range: ")
        continue

    elif intN == 1:     # Task1
        print("\nTask1")
        sizeA = 10
        arr = []

        for i in range(sizeA):
            arr.append(random.randrange(0, 9))
        print("Full array:\t\t\t", arr)
        print("Section, ind 2 -> 8:", arr[2:8])

    elif intN == 2:     # Task2
        print("\nTask2")
        ind = 0
        arr = []
        sizeA = abs(float(input("enter size of arr: ")))
        sizeA = int(sizeA)

        for i in range(sizeA):
            arr.append(random.randrange(1, 20))
        print(arr)

        minVal = arr[0]
        maxVal = arr[0]
        indMin = 0
        indMax = 0

        for i in range(sizeA):
            if minVal > arr[i]:
                minVal = arr[i]
                indMin = i
            if maxVal < arr[i]:
                maxVal = arr[i]
                indMax = i

        if indMin > indMax:
            temp = indMax
            indMax = indMin
            indMin = temp

        print("\nValue: min = {}, max = {}".format(minVal, maxVal))
        print("Index: min = {}, max = {}".format(indMin, indMax))

        print("Section of arr min < x < max:\t", arr[indMin+1:indMax])

    elif intN == 3:     # Task3
        print("\nTask3")
        arr = []

        while True:
            nameCar = input("Enter name of car: ")
            arr.append(nameCar)
            if "honda" == nameCar or "Honda" == nameCar in arr:
                break
            else:
                continue
        print("Honda is best among car " if "honda" or "Honda" in arr else "Honda is absent among car", end='')
        print(arr)

    elif intN == 4:     # Task4
        print("\nTask4")
        sizeA = 5
        arr = []

        for i in range(sizeA):
            arr.append(input("Enter name of fruit: "))
        print("yes apple" if "apple" or "Apple" in arr else "no apple")

    elif intN == 5:     # Task5
        print("\nTask5")
        sizeA = 10
        arr = []

        for i in range(sizeA):
            arr.append(round((random.uniform(0.1, 0.9)), 1))
        print("Full array:\t\t\t", arr)

        ind = 0
        print("Values = 0.2:")
        for i in range(sizeA):
            if arr[i] == 0.2:
                print("\tarr[{}] = {}".format(i, arr[i]))
            else:
                ind += 1

        if ind == sizeA:
            print("No value 0.2")

    elif intN == 6:     # Task6
        print("\nTask6")
        count = 0
        arr = []
        sizeA = abs(float(input("enter size of arr: ")))
        sizeA = int(sizeA)

        for i in range(sizeA):
            arr.append(round((random.uniform(0.1, 9.9999)), random.randrange(1, 4)))
        print("Full array:\t\t\t", arr)

        for i in range(sizeA):
            temp = arr[i] * 10000
            while temp:
                if temp % 10 == 2:
                    count += 1
                temp /= 10
                temp = int(temp)
        print("Qty of digit = \"2\":\t", count)
else:
    print("\tERROR!")