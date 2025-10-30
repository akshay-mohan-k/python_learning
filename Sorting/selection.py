list = [6, 8, 1, 4, 10, 18]

def selection_sort(list):
    n = len(list)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if(list[j] < list[min_index]):
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

selection_sort(list)
print(list)