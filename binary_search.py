
def test(test_case_name, list1, list2, expected_output):
    actual_output = binary_search(list1, list2)
    if(actual_output == expected_output):
        print('\033[92m', "Success:", test_case_name)
    else:
        print('\033[91m', "Failure:", test_case_name, "\nexpected", expected_output, "actual", actual_output, )

def test_case_1():
    word1_list = [8, 11, 13, 19, 32, 45]
    word2_list = [1, 24, 25, 33, 34, 56]
    output = 1
    test("test_case_1", word1_list, word2_list, output)


def test_case_2():
    word1_list = [8, 11, 13, 32, 45]
    word2_list = [1, 24, 25, 33, 34, 56]
    output = 1
    test("test_case_2", word1_list, word2_list, output)

def test_case_3():
    word1_list = [8, 11, 13, 19, 32, 45]
    word2_list = [1, 24, 33, 34, 56]
    output = 1
    test("test_case_3", word1_list, word2_list, output)

def test_case_4():
    word1_list = [8, 11]
    word2_list = [1, 24, 33, 34, 56]
    output = 7
    test("test_case_4", word1_list, word2_list, output)

def test_case_5():
    word1_list = [8, 11, 13, 32, 45]
    word2_list = [1, 24, 34, 56]
    output = 2
    test("test_case_5", word1_list, word2_list, output)

def test_case_6():
    word1_list = [-8, 11, 13, 32, 45]
    word2_list = [-1, 24, 94, 56]
    output = 7
    test("test_case_6", word1_list, word2_list, output)


def binary_search(list1, list2):
    print(list1)
    print(list2)
    min_value = 1000000000
    for list1_current_value in list1:
        left = 0
        right = len(list2)
        while left <= right:
            mid = (left + right)//2
            mid_element = list2[mid]
            diff = abs(list1_current_value - mid_element)
            min_value = min(diff, min_value)
            if mid_element > list1_current_value:
                right = mid - 1
            else:
                left = mid + 1
            print(list1_current_value, left, right, mid, mid_element, diff)
    return min_value

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()