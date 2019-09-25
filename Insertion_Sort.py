def insertion_sort(l):
    for sliceEnd in range(len(l)):
        pos = sliceEnd
        while pos > 0 and l[pos] < l[pos-1]:
            (l[pos],l[pos-1]) = (l[pos-1],l[pos])
            pos = pos - 1


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
