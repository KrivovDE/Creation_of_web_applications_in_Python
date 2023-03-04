

nums_1 = [5, 2, 1, 8, 4]
nums_2 = [5, 2, 1, 8, 4]
nums_3 = [5, 2, 1, 8, 4]


def bubble_sort_1(_nums):
    for i in range(len(nums_1)):
        for j in range(len(nums_1) - 1):
            if nums_1[j] > nums_1[j+1]:
                nums_1[j], nums_1[j+1] = nums_1[j+1], nums_1[j]


bubble_sort_1(nums_1)
print(nums_1)


# оптимизация 1
def bubble_sort_2(_nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums_2) - 1):
            if nums_2[i] > nums_2[i + 1]:
                nums_2[i], nums_2[i + 1] = nums_2[i + 1], nums_2[i]
                swapped = True


bubble_sort_2(nums_2)
print(random_list_of_nums_2)


# оптимизация 2
def bubble_sort_3(our_list):
    has_swapped = True

    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            if our_list[i] > our_list[i+1]:
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
        num_of_iterations += 1



bubble_sort_3(random_list_of_nums_3)
print(random_list_of_nums_3)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("bubble_sort_3(random_list_of_nums_3)", setup="from __main__ import bubble_sort_3"))



