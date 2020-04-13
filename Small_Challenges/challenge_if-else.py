initial_list = ['1', 2.4, 1, 'Hello World!', 2, 5, 400, 5.6890,
                 3.1415, 'It is fine', 4, 20, 49, 51.3]

#output: a dictionary of lists
#each value should be a list containing only one data type,
#if the data type is integer, sort odds and evens into different lists

#A Solution:

string_list = []
even_int_list = []
odd_int_list = []
float_list = []

for x in initial_list:
    if isinstance(x, str):
        string_list.append(x)
    elif isinstance(x, int):
        if x % 2 == 0:
            even_int_list.append(x)
        else:
            odd_int_list.append(x)
    elif isinstance(x, float):
        float_list.append(x)

my_dict = {'strings': string_list, 'evens': even_int_list, 
            'odds': odd_int_list, 'floats': float_list}


#w/o a for loop:
if isinstance(initial_list[0], str):
        string_list.append(initial_list[0])
#etc
#and repeat


