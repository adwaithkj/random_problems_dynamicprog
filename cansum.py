# Question. Find whether from a given array list, if it is possible to obtain a given targetsum
# Repetitions are allowed from the array list


def cansum(targetsum, arr, dict1):
    if targetsum in dict1:
        return dict1[targetsum]
    if targetsum < 0:
        return False
    if targetsum == 0:
        return True

    for i in arr:
        sum = targetsum - i
        if cansum(sum, arr, dict1) == True:
            dict1[targetsum] = True
            return True
    dict1[targetsum] = False
    return False


# targetsum = input("Enter the Target Sum =>")

# arr = (input("Enter the array list seperated by spaces=>"))
# arr = arr.strip().split(" ")

# arr = list(map(int, (arr)))
# print(f" The entered list is {arr} and the target sum is {targetsum}")

targetsum = 300

arr = [7, 14]
dict1 = {}
print(cansum(targetsum, arr, dict1))
