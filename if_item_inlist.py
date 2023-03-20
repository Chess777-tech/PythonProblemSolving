def is_group_num(group_data, n):
    for value in group_data:
        if n == value:
            return True 
    return False

print(is_group_num([1,2,3,4,5,6,77], 77))
print(is_group_num([1,2,3,4,5,64], 65))