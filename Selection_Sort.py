def selection_sort(l):
    start = 0
    for start in range(len(l)):
        min_pos = start
        for i in range(start,len(l)):
            if l[min_pos] > l[i]:
                min_pos = i

        (l[start],l[min_pos]) = (l[min_pos],l[start])


arr = [12, 11, 13, 5, 6]
selection_sort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
