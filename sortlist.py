#2. Sort a list
#Create a function in Python that accepts two parameters. The first will be a list
#  of numbers. The second parameter will be a string that can be one of the following
#  values: asc, desc, and none.

#If the second parameter is "asc," then the function should return a list with the
#  numbers in ascending order. If it's "desc," then the list should be in descending
#  order, and if it's "none," it should return the original list unaltered.

to_be_sorted = [6, 7, 8, 1, 2, 3, 5, 4]

def sort_list(list, type_sort):
    try:
        working_list = list.copy()
        if type_sort == 'asc':
            working_list.sort()
            return working_list
        elif type_sort == 'desc':
            working_list.sort(reverse=True)
            return working_list
        elif type_sort == 'none':
            return working_list
        else:
            print('Not a valid sort type.')
    except:
        print("Not a valid input. Use a list.")


##demo
print(sort_list(to_be_sorted, 'asc'))
print(sort_list(to_be_sorted, 'desc'))
print(sort_list(to_be_sorted, 'none'))
print(sort_list(to_be_sorted, 'chicken'))
print(sort_list('chicken', 'chicken')) 
