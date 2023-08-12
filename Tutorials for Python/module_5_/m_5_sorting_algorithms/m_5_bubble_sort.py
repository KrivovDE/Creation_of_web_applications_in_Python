nums_1 = [5, 2, 1, 8, 4] * 10
nums_2 = [5, 2, 1, 8, 4] * 10
nums_3 = [5, 2, 1, 8, 4] * 10


def bubble_sort_1(_nums):
    for i in range(len(_nums)):
        for j in range(len(_nums) - 1):
            if _nums[j] > _nums[j + 1]:
                _nums[j], _nums[j + 1] = _nums[j + 1], _nums[j]


# bubble_sort_1(nums_1)
# print(nums_1)

#
# # оптимизация 1
def bubble_sort_2(_nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(_nums) - 1):
            if _nums[i] > _nums[i + 1]:
                _nums[i], _nums[i + 1] = _nums[i + 1], _nums[i]
                swapped = True


#
#
# bubble_sort_2(nums_2)
# print(nums_2)
#
#
# # оптимизация 2
def bubble_sort_3(_nums):
    has_swapped = True
    num_of_iterations = 0
    while has_swapped:
        has_swapped = False
        for i in range(len(_nums) - num_of_iterations - 1):
            if _nums[i] > _nums[i + 1]:
                _nums[i], _nums[i + 1] = _nums[i + 1], _nums[i]
                has_swapped = True
        num_of_iterations += 1


#
#
# bubble_sort_3(nums_3)
# print(nums_3)
#
#

if __name__ == "__main__":
    import timeit

    print(timeit.timeit("bubble_sort_1(nums_1)", globals=globals()))
    print(timeit.timeit("bubble_sort_2(nums_2)", globals=globals()))
    print(timeit.timeit("bubble_sort_3(nums_3)", globals=globals()))
