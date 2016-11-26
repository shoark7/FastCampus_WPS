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


def quick_sort(wanted_list):
    """
    Quick sort implementation with Python.
    :param wanted_list: The list you want to sort.
    :return: sorted list. If you want, you can change it to return nothing.
    """
    START = 0
    END = len(wanted_list)-1


    # def get_pivot():
    #     MIDDLE = len(wanted_list) // 2
    #     value_list = [wanted_list[START], wanted_list[MIDDLE], wanted_list[END]]
    #
    #     for i in range(3 - 1):
    #         for j in range(2 - i):
    #             if value_list[j] > value_list[j+1]:
    #                 value_list[j], value_list[j+1] = value_list[j+1], value_list[j]
    #
    #     wanted_list[START], wanted_list[MIDDLE] = wanted_list[MIDDLE], wanted_list[START]

    def make_partitions(start, end):
        pivot = wanted_list[start]
        low = start + 1
        high = end

        while low <= high:
            while low < end and wanted_list[low] <= pivot:
                low += 1

            while high > start and wanted_list[high] >= pivot:
                high -= 1

            if low > high:
                break
            wanted_list[high], wanted_list[low] = wanted_list[low], wanted_list[high]

        wanted_list[high], wanted_list[start] = wanted_list[start], wanted_list[high]

        return high

    def sort(start, end):
        if start >= end:
            return

        middle = make_partitions(start, end)
        sort(start, middle - 1)
        sort(middle + 1, end)


    # get_pivot()
    sort(START, END)
    return wanted_list