def range_validation(data, min, max):
    if len(data) >= min and len(data) <= max:
        return True
    else:
        print("Input wrong")
        exit()


def type_validation(actual_type, desired_type):
    if actual_type == desired_type:
        return True
    else:
        print("Input wrong")
        exit()


def length_validation(length, desired_length):
    if length == desired_length:
        return True
    else:
        print("Input wrong")
        exit()