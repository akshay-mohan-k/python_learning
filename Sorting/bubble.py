list = [5, 8, 1, 6, 9, 2, 4]

def bubble_sort(list):
     n = len(list)
     for i in range(n-2, -1, -1):
          for j in range(0, i+1):
               if(list[j] > list[j+1]):
                    list[j], list[j+1] = list[j+1], list[j]

bubble_sort(list)
print(list)