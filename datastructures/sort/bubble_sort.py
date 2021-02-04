

def bubble_sort(input_list):
    size = len(input_list)
    swapped = False
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if input_list[j] > input_list[j+1]:
                tmp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = tmp
                swapped = True
        if not swapped:
            break


inp_list = [555, 2, 4, 6, 8, 22, 55, 77, 4]
bubble_sort(inp_list)
print(inp_list)