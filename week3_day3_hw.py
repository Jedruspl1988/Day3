# Exercise #1 
# Reverse the list below in-place using an in-place algorithm. For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
print(words[::-1])



# Exercise #2 <br>
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.Should output:{'a': 5,'abstract': 1,'an': 3,'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def word_count(str):
    words = a_text.lower().split()
    countdic = {}
    for word in words:
        countdic[word] = words.count(word)
    return countdic

print(word_count(a_text))



# Exercise #3

# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

# Hint: Linear Searching will require searching a list for a given number. 

def lsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return "# not in Array"
arr = ['1','20','30','50','80','100','150','200']
x = '50'
print(lsearch(arr,x))