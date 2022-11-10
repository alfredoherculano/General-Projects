# a function that takes a list and a target as parameters
# multiple variables: middle, start, end, steps (the amount of times it takes to go through the list)
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(lst, element):
    middle = 0
    start = 0
    end = len(lst)
    steps = 0

    while start <= end:
        print('Steps', steps, ':', str(lst[start:end + 1]))

        steps += 1
        middle = (start + end) // 2

        if element == lst[middle]:
            return middle
        elif element < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 13

binary_search(my_list, target)