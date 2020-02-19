def range_validation(data, min, max):
    if len(data) > min and len(data) < max:
        return True
    else:
        print("Input wrong")
        return False


def type_validation(actual_type, desired_type):
    if actual_type == desired_type:
        return True
    else:
        print("Input wrong")
        return False


def max_length_validation(length, max):
    if length < max:
        return True
    else:
        print("Input wrong")
        return False