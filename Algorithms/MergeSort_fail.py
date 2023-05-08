def MergeSort(ar, left, right):
    if left < right:
        mid = int((left + right) / 2)
        print(left, right)
        if left == right - 1:
            if ar[left] > ar[right]:
                ar[left], ar[right] = ar[right], ar[left]
        else:
            MergeSort(ar, left, mid)
            MergeSort(ar, mid + 1, right)
            i = 1
            j = 0
            leftar = ar[left:mid+1]
            rightar = ar[mid+1:right+1]
            finalar = []
            finalar.append(leftar[i])
            while i < len(leftar) or j < len(rightar):
                if leftar[i] > finalar[-1]:
                    finalar.append(leftar[i])
                    i += 1
                elif rightar[j] > finalar[-1]:
                    finalar.append(rightar[j])
                    j += 1

            while i < len(leftar):
                finalar.append(leftar[i])
                i += 1
            while j < len(rightar):
                finalar.append(rightar[i])
                j += 1
                
            ar = finalar

import random
ar = [random.randint(1, 1000) for aa in range(100)]
MergeSort(ar, 0, len(ar) - 1)
print(ar)
