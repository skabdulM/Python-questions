#1. Reverse a List:
def reverse_list(lst):
    return lst[::-1]

#2. Find Duplicates in a List:
def findDuplicates(lst):
    return [x for x in set(lst) if  lst.count(x)> 1]

#3. Remove Duplicates from a List:
def removeDuplicates(lst):
    return [x for x in lst if  lst.count(x)== 1]

#4. Find Intersection of Two Lists:
def findIntersection(lst1,lst2):
    result=[]
    for x in lst2:
        if x in lst1:
            result.append(x)
    return result

#5. Flatten a Nested List:
def flattenList(lst):
    result = []
    for x in lst:
        for y in x:
            result.append(y)
    # return [item for sublist in nested_list for item in sublist] anmother short way
    return result

#6. Find the Second Largest Number in a List:
def findSecLargest(lst):
    result = list(set(lst))
    result.sort()
    return result[-2]

#7. Rotate a List:    
def rotateList(lst,n):
    x = lst[n:] + lst [:n]
    return x

#8. Find the Difference Between Two Lists:
#Write a function to find the elements that are in one list but not in the other.
def findUniqueInLst(lst1,lst2):
    return [x for x in lst1 if x not in lst2]

#9. Find the Largest Element in a List:
#Write a function to find the largest element in a list without using the max() function.
def largestNo(lst):
    y = lst[0]
    for x in lst:
        if x > y:
            y = x
    return y
    
#12. Find Pairs with a Given Sum:
def twoSum( nums, target):
    i = 0
    while i < len(nums):
        for j in range( len(nums)):
            if i==j :
                break
            if nums[i]+nums[j] == target:
                return [j , i]
                i = len(nums)+1
                break
        i= i+1
            
#Given a list and a pivot element, partition the list such that all elements less than the pivot come before the pivot, and all elements greater come after it.
def partitionList(lst,pivot):
    temp1=[]
    temp2=[]
    for x in lst:
        if x<pivot:
            temp1.append(x)
        else:
            temp2.append(x)
    #temp1.extend(temp2)
    #extra sort for easy understanding
    #temp1.sort()
    #temp2.sort()
    return temp1+[pivot]+temp2

#leetcode q Given an integer x, return true if x is a palindrome , and false otherwis
def isPalindrome( x):
    temp = str(x)
    temp2 = temp[::-1]
    ab= Tru e
    for i in range(len(temp)):
        if temp[i]!=temp2[i]:
            ab = False
            return ab
    return ab

reversedlist = reverse_list([1,2,4,6])
duplicates = findDuplicates([1,3,2,2,4,6,6])
removeduplicates = removeDuplicates(["hello","world","thing","hello"])
intersectionoflist = findIntersection([1,2,3,4,5],[2,4,6,89,56])
flattenlist = flattenList([["hello","world","thing","hello"],["hello","world","thing","hello"],[2,4,6,89,56]])
secondLargest = findSecLargest([12,3,4,5])
listrotate = rotateList([12,3,4,5,6,8,9],4)
diffbetlist = findUniqueInLst([1,2,3,4,5,89,65],[2,4,6,89,56])
maxNo = largestNo([1,3,2,2,4,6,6,89])
sumoftwo = twoSum([1,3,2,2,4,6,6,89],9)
partitionedList = partitionList([1,2,8,55,65,15,45,3,89,6,3],9)
palindrome = isPalindrome(10)

print("reversed list: ", reversedlist)
print("found duplicates: ", duplicates)
print("removed duplicates: ",removeduplicates)
print("Intersection of lists are : ",intersectionoflist)
print("Flattened list : ",flattenlist)
print("second largest no in list : ",secondLargest)
print("Rotated list : ",listrotate)
print("elements that are in one list but not in the other : ",diffbetlist)
print("Max element in list : ",maxNo)
print("Index of the elements : ",sumoftwo)
print("Partition of list : ",partitionedList)