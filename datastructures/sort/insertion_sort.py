
def insertion_sort(input_list):
    size = len(input_list)

    for i in range(1, size):
        anchor = input_list[i]
        j = i - 1
        while j>=0 and anchor < input_list[j]:
            input_list[j+1] = input_list[j]
            j = j - 1
        input_list[j+1] = anchor


inp_list = [555, 2, 4, 6, 8, 22, 55, 77, 4]
insertion_sort(inp_list)
print(inp_list)