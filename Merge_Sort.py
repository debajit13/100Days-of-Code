def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)
    while i+j < m+n:

        if i == m:
            C.append(B[j])
            j = j+1

        elif j == n:
            C.append(A[i])
            i = i+1

        elif A[i] <= B[j]:
            C.append(A[i])
            i = i+1

        elif A[i] > B[j]:
            C.append(B[j])
            j = j+1

        return(C)


def mergeSort(D,left,right):
    if right - left <= 1:
        return(D[left:right])

    if right - left > 1:
        mid = (left + right) // 2

        L = mergeSort(D,left,mid)
        R = mergeSort(D,mid,right)

        return(merge(L,R))
