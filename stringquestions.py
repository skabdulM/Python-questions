from collections import Counter

#1. Reverse a String
def reverseStr(str):
    return str[::-1]

#2. Check if a String is a Palindrome
def palindromeCheck(str):
    return str == str[::-1]

#3. Count Vowels in a String
def checkVowels(str):
    vowels = "aeiouAEIOU"
    i = 0 
    for each in str:
        if each in vowels:
            i=i+1
    return i

#4. Find the Longest Word in a Sentence
def longestWordCheck(str):
    a = str.strip().split()
    longestWord ="" 
    for each in a:
        if len(each)>len(longestWord):
            longestWord = each
    return longestWord

#5. Check if Two Strings are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

#6. Count the Occurrences of a Character in a String
def countOccurrences(str, char):
    return str.count(char)

#7. Find All Substrings of a String
def find_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    return substrings

#8. Capitalize the First Letter of Each Word
def capitalizeWord(str):
    return str.capitalize()

#9. Remove Duplicate Characters from a String
def removeDuplicate(str):
    temp= []
    for each in str:
        if each not in temp:
            temp.append(each)
    
    return ''.join(temp)

#10. Find the Most Frequent Character in a String
def mostFrequent(str):
    counter = Counter(str)
    return counter.most_common(1)[0][0]

reversedString = reverseStr("my string")
palindrome = palindromeCheck("txt")
vowel = checkVowels("this is a vowel check")
longestWord = longestWordCheck(" this is a to check the longest words")
anagram = are_anagrams("listen", "silent")
substrings = find_substrings("abcs")
capitalizedWord = capitalizeWord("when it\'s raining") 
duplicateRemove = removeDuplicate("when it\'s raining") 
frequentChar = mostFrequent("it\'s raining") 

print("reversed string: "+ reversedString)
print("It is a palindrome: " , palindrome)
print("No of vowels: ",vowel)
print("Longest word in this string: ",longestWord)
print("Is it anagram string: ",anagram)
print("Count the no of occurrences of the character: ",countOccurrences("hello world","l"))
print("substring check: ",substrings)
print("Capitalized word: ",capitalizedWord)
print("removed duplicate : ",duplicateRemove)
print("Most frequent Character: ",frequentChar)


