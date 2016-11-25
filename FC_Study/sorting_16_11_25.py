def bubble_sort(wanted_list):
    """
    Python bubble sort implementation.
    :param wanted_list: The list you want to sort.
    :return: Sorted list.
    """
    list_length = len(wanted_list)

    # Ascending sorting
    for i in range(list_length - 1):
        for j in range(i + 1, list_length): # 9, 10, 1, 2
            if wanted_list[i] > wanted_list[j]:
                tmp_value = wanted_list[i]
                wanted_list[i] = wanted_list[j]
                wanted_list[j] = tmp_value
                # original way of swap. You can use just 'a, b = b, a' way actually.

    return wanted_list
    # If you want, you don't need to return anything.
    # Because Python uses 'call by assignment'.

    # Big O of bubble sort: n ** 2



def quick_sort(wanted_list, middle=None):
    start = 0
    if middle:
        end = middle
    else:
        end = len(wanted_list)

    """

    :param wanted_list:
    :return:
    """


    def make_partitions(start, end):
        pivot = wanted_list[start]
        low = start + 1
        high = end

        while low <= high:
            while wanted_list[low] <= pivot and low <= end:
                low += 1

            while wanted_list[high] >= pivot and high >= start+1:
                high -= 1

            if low <= high:
                wanted_list[low], wanted_list[high] = wanted_list[low], wanted_list[high]


        wanted_list[start], wanted_list[high] = wanted_list[high], wanted_list[start]

        return high


    # 1. 탈출 조건
    if start >= end:
        return

    quick_sort(start, middle - 1)
    quick_sort(middle, end)


    # 2. 재귀식
