# Intro to Programming for Public Policy
# Spring 2019
# - all sections -
# Homework 1 - due on GitHub by Monday 4/15 at midnight CST
# Instructions: Write the code for your answer beneath each question, and make sure that it
#               runs, uses good Python style and correctly answers the question.  The style
#               guide can be found here: https://www.python.org/dev/peps/pep-0008/
#
#               NOTE: Unless explicitly stated, you must always use Python code to get your
#               answer.  For example, if the question is: a = 4, b = 5, what is a + b?  Then
#				simply writing 9 is incorrect, while print(a + b) is correct.
#
#               NOTE: It is expected you will use outside sources for help answering these
#               questions.  Please refer to the syllabus for citation rules!

#General citation: I discussed this homework with a non-Harris friend who programs in languages other than Python

# QUESTION 1: Use the following dictionary:

#https://stackoverflow.com/questions/4868904/what-is-the-origin-of-foo-and-bar
my_dict = {'foo':[1,2,3,4],
		   'bar':['a', 'b', 'c'],
		   'baz':['a', tuple([0, 0, 100]), set(['a', 'a', 'b', 'b']), [], True and False, 1==4]}

# a) Find and display the number of elements in the list under the 'foo' key.
print(len(my_dict['foo'])) 
#citation https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# b) Find how many elements are in the object under the 'baz' key, at index location 2.  In comments explain why.
temp_list = my_dict['baz']
len(temp_list[2])
#test:
len(set(['a', 'a', 'b', 'b'])) #confrmed
#index location 2 is: set(['a', 'a', 'b', 'b']). It takes list ['a', 'a', 'b', 'b'], and outputs a set (list of uniqu values)
#therfore while the internal list has 4 elements, the set of that list has only 2 elements

# c) Extract just the last two elements from the list under the 'baz' key.  In comments, explain why the result
#    is the values you see.
temp_list1 = my_dict['baz']
print(temp_list1[4:])

#Python evaluates the statement before printing, this is why we see [False, False], which is the answer to
# the two logical statements that are the last two elemens from the list under the 'baz' key

# d) Replace the first two elements in the object under the 'bar' key with 'dog' and 'cat'.
temp_list2 = my_dict['bar']
temp_list2[0] = 'dog'
temp_list2[1] = 'cat'
my_dict['bar'] = temp_list2
my_dict #check that it worked

# e) Under the 'baz' key, at index location 1, replace the first two elements in the object with 'dog' and 'cat'.
#    In comments, explain the result.
temp_list3 = my_dict['baz']
t = temp_list3[1]
t = list(t) #change to a list so that it can be edited
t[0] = 'dog'
t[1] = 'cat'
t = tuple(t) #change back into a tuple
temp_list3[1] = t
my_dict['baz'] = temp_list3
my_dict #check that it worked
#becaue the object under 'baz' key at indec location 1 was a tuple and thus imutable
#I had to convert the tuple into a list before editing it.

# f) Assign the value 'd' to index location 3 in the object under the 'bar' key.
list.append(my_dict['bar'], 'd')
#check that is worked
my_dict
#citation: https://www.programiz.com/python-programming/methods/list/append

# g) Find the mean and sum of the values under the 'foo' key.
import numpy
numpy.sum(my_dict['foo'])
numpy.mean(my_dict['foo'])

# QUESTION 2: Use the following string:
my_string = 'Hello how are  you?  do you like coffee?  because if youre going to write code, you pretty much have to.'

# a) Fix the missing apostrophe in "youre"
my_string = str.replace(my_string,"youre", "you're") #sucess
#Citation: https://docs.python.org/3/library/stdtypes.html#string-methods

# b) This string has some double spaces in it.  Write one solution that turns them into single spaces that only applies
#    to this sentence, and one solution that is generalized to remove double spaces from any string.
my_string = str.replace(my_string,"  ", " ")

def spacefixer(string):
	print(str.replace(string, "  ", " "))
spacefixer(my_string) #apply the new function

# c) Split this string into a list of unique sentences.
str.rsplit(my_string, sep = "?")
#citation: https://docs.python.org/3/library/stdtypes.html

# d) Two sentences are missing capitalization at the start.  Write two solutions, one that fixes only this string, and
#    one that is generalized to fix missing capitalization at the start of sentences for any string containing them.
my_string = str.replace(my_string,"do", "Do")
my_string = str.replace(my_string,"because", "Because")


sep = "?"
my_split = [u for x in my_string.split(sep) for u in (x, sep)]
my_split = my_split[:-1]
string = ""
for v in my_split:
	v = v.strip() #get rid of leading space
	v = v.capitalize() #capitalize the first letter in ea string
	if v == "?":
		string = string + v
	else:
		string = string + " " + v
print(string)

#yay!!!!!
#citation:
#https://www.programiz.com/python-programming/methods/string/join
#cite https://stackoverflow.com/questions/10443400/remove-leading-and-trailing-spaces/10443548
#cite https://www.geeksforgeeks.org/string-capitalize-python/
#https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators

# QUESTION 3: Use the following list:

my_list = [1, 2, 3, 8, 9, 101, 102, 45, 73, 1000]

# a) Loop over the values in this list, and print a sentence saying which value is at each index location.
#    e.g. "55 is at index 4" followed by "10 is at index 5" and so on.

my_string = "{} is at index {}"
for index, value in enumerate(my_list):
	print(my_string.format(value, index))
#done

# b) Print the sum, mean, median, max and min values of the list.  The first time, loop over each value one at a time
#    and use conditional statements to figure out the answers.  The second time use the NumPy library.

#sum
print(sum(my_list))
#citation: https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
#mean
print(sum(my_list) / len(my_list))

#median

def my_median(my_list):
	my_list = sorted(my_list) #sort increasing
	list_len = len(my_list)
	half_len1 = int((list_len - 1)/2)
	half_len2 = int((list_len + 1)/2)
	if list_len < 1:
		return None
	elif list_len % 2 == 0:
		return (my_list[half_len1] + my_list[half_len2]) / 2
	else:
		return my_list[half_len1]
print(my_median(my_list))
#citation:
#https://www.science-emergence.com/Articles/How-to-find-the-median-of-a-list-in-python/
#or https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python

#max
max = 0
for i in my_list:
	if i > max:
		max = i
print(max)

#min
min = 1000000
for i in my_list:
	if i < min:
		min = i
print(min)

#useing NumPy, already installed above
print(numpy.sum(my_list))
print(numpy.mean(my_list))
print(numpy.median(my_list))
print(numpy.max(my_list))
print(numpy.min(my_list))

# c) In a way that generalizes to any list of numbers, print the number of entries that are greater than or equal to 100.
greater_than_100 = []
for number in my_list:
	if number >= 100:
		list.append(greater_than_100, number)
print(len(greater_than_100))
