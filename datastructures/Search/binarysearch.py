
def binarysearch(list_item, search_item):
    left_index = 0
    right_index = len(list_item) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list_item[mid_index]
        if mid_number == search_item:
            return mid_index

        if search_item > mid_number:
            left_index = mid_index + 1
        elif search_item < mid_number:
            right_index = mid_index - 1


def binarysearch_recursion(list_item, search_item, left_index, right_index):
    mid_index = (left_index + right_index) // 2
    mid_item = list_item[mid_index]
    if mid_item == search_item:
        return mid_index

    if search_item > mid_index:
        left_index = mid_index + 1
    elif search_item < mid_index:
        right_index = mid_index -1

    return binarysearch_recursion(list_item, search_item, left_index, right_index)


input_list = [1, 3, 5, 6, 8, 9, 13, 17, 22]
print(binarysearch_recursion(input_list, 13, 0, len(input_list)-1))
