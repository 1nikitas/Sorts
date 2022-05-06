def bubble_sort(mas):      # O(n^2)
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(mas)-1):
            if mas[i] > mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
                swapped = True

def selection_sort(mas):   # O(n^2)
    for i in range(len(mas)):
        lowert_value_index = i
        for j in range(i+1, len(mas)):
            if mas[j] > mas[lowert_value_index]:
                lowert_value_index = j
        mas[i], mas[lowert_value_index] = mas[lowert_value_index], mas[i]

def insertion_sort(mas):  # O(n^2)
    for i in range(1, len(mas)):
        item_insert = mas[i]
        j =  i - 1
        while j >= 0 and mas[j] > item_insert:
            mas[j+1] = mas[j]
            j-=1
        mas[j+1] = item_insert

def heapify(mas, heap_size, root_index):# O(n*log(n))   #двоичная куча
    largest = root_index
    left_child, right_child = (2*root_index)+1, (2*root_index)+2

    if left_child < heap_size and mas[left_child] > mas[largest]:
        largest = left_child

    if right_child < heap_size and mas[right_child] > mas[largest]:
        largest = right_child

    if largest != root_index:
        mas[root_index], mas[largest] = mas[largest], mas[root_index]
        heapify(mas, heap_size, largest)

def heap_sort(mas):
    n = len(mas)

    for i in range(n, -1, -1):
        heapify(mas, n, i)

    for i in range(n-1, 0, -1):
        mas[i], mas[0] = mas[0], mas[i]
        heapify(mas, i, 0)


def main():
    mas = [1,432,24,246,25,2]
    # bubble_sort(mas)
    # selection_sort(mas)
    # insertion_sort(mas)
    heap_sort(mas)
    print(mas)
if __name__ == '__main__':
    main()