def is_ascending(list):
    if len(list) == 1:
        return True
    else:
        if list[0] < list[1]:
            return is_ascending(list[1:])
        else:
            return False



list = [1,3,2,4,5,6,7]
print(is_ascending(list))
