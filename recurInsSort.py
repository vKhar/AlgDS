def recIns(array):
    if len(array) <= 1:
        return array
    else:
        last = array[-1]
        sorted_array = recIns(array[:-1])
        i = len(sorted_array)-1
        while i >= 0 and sorted_array[i] > last:
            i-=1
    return sorted_array[:i+1]+[last] + sorted_array[i+1:]



        


    


        





