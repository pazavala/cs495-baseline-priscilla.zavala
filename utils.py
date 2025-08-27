# Have a collection of tuples. Returns index and tuple with max sum.

def tuple_with_max_sum(tuples):
    # check if empty tuple
    if not tuples:
        return None
    
    max_index, max_tuple = 0, tuples[0]
    max_sum = sum(tuples[0])
    
    for index, tuple in enumerate(tuples[1:], start=1):
        current_sum = sum(tuple)
        if current_sum > max_sum:
            max_sum = current_sum
            max_tuple = tuple
            max_index = index
    
    return max_index, max_tuple