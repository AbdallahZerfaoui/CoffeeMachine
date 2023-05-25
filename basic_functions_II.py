def sum_product(list1, list2):
    result: float = 0
    for elem1, elem2 in zip(list1, list2):
        result += elem1 * elem2
    return result