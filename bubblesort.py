sortable = [96,72,51,10,34,9,21]
def bubblesort(sortable):
    for passnum in range(len(sortable)-1,0,-1):
        for i in range(passnum):
            if sortable[i]>sortable[i+1]:
                temp = sortable[i]
                sortable[i] = sortable[i+1]
                sortable[i+1] = temp

bubblesort(sortable)
print(sortable)
