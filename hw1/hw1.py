import listFileIO as IO

def average(myList):
    avg = 0
    for num in myList:
        avg = avg + num
    return avg/len(myList)

def same_position(list1, list2):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            return True
    return False

def invert(strList):
    return strList[::-1]

if __name__=="__main__":
    print("1- Average:")
    input1 = IO.readIntListFromFile("input1.txt")
    print("INPUT: " + str(input1))
    print("OUTPUT: " + str(average(input1)))

    print("\n2- Same position:")
    input2 = IO.readStringListFromFile("input2.txt")
    input3 = IO.readStringListFromFile("input3.txt")
    input4 = IO.readStringListFromFile("input4.txt")
    print("INPUT: L1=" + str(input2) + " L2=" + str(input3))
    print("OUTPUT: " + str(same_position(input2, input3)))
    print("INPUT: L1=" + str(input2) + " L2=" + str(input4))
    print("OUTPUT: " + str(same_position(input2, input4)))

    print("\n3- Invert:")
    input5 = IO.readStringListFromFile("input5.txt")
    print("INPUT: L=" + str(input5))
    print("OUTPUT: L=" + str(invert(input5)))