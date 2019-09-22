def BinarySearch(sequence,value,left_val,right_val):
    #BinarySearch searchs value in the sequence[left_val:right_val], sequence is sorted

    if (right_val - left_val) == 0:
        return (False)

    middle_val = (left_val + right_val) // 2
    if sequence[middle_val] == value:
        return (True)

    elif value > sequence[middle_val]:
        return(BinarySearch(sequence,value,middle_val+1,right_val))

    else:
        return(BinarySearch(sequence,value,left_val,middle_val))

s = [1,2,3,4,5,6]
print(BinarySearch(s,3,1,5))
