from utils import tuple_with_max_sum

def test_tuple_with_max_sum_stand():
    assert tuple_with_max_sum([(1, 2), (3, 4), (0, 10)]) == (2, (0, 10))

def test_tuple_with_max_sum_variate():
    assert tuple_with_max_sum([(5, 5), (2, 9), (7, 1)]) == (1, (2, 9))

def test_tuple_with_max_sum_empty():
    assert tuple_with_max_sum([]) is None

def test_tuple_with_max_sum_single_tuple():
    assert tuple_with_max_sum([(42, 58)]) == (0, (42, 58))

def test_tuple_with_max_sum_negative_numbers():
    assert tuple_with_max_sum([(-1, -2), (-3, -4), (-2, -1)]) == (0, (-1, -2))