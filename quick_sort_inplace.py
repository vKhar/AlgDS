import random
ulist = [ random.randint(1,20) for i in range(40) ]
def partition(li, lb, ub):
    #left 0:left -> <= pivot invariants
    #left+1:right -> > pivot
    # right: -> unchecked
    pivot=li[lb]
    left=lb
    for right in range(lb+1,ub):
        if li[right] <= pivot:
            left+=1
            li[left],li[right] = li[right],li[left]
    li[lb],li[left]=li[left],li[lb]
    return left
def quick_sort(ulist,lb,ub):
    if ub <= lb:
        return ulist
    pivot=partition(ulist,lb,ub)
    quick_sort(ulist,lb,pivot)
    quick_sort(ulist,pivot+1,ub)
    return ulist
#list=[2,1,1,1,1]
print(ulist)
print(quick_sort(ulist,0,len(ulist)))
