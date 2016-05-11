def sort_by_value(alist,max_val):
    sorted_list = [max_val]
    for i in alist:
        if i >= sorted_list[-1]:
            sorted_list.append(i)
        else:
            result = dyn_binary_search(i,sorted_list)
            if type(result) != type(tuple()):
                sorted_list.insert(result,i)
            else:
                sorted_list.insert(result[1]+1,i)
    sorted_list.remove(max_val)
    return sorted_list

def dyn_binary_search(elem,sorted_list):
    firsts = [0]
    lasts = [len(sorted_list)-1]
    while firsts[-1] <= lasts[-1]:
        mid = (firsts[-1] + lasts[-1]) //2
        if elem == sorted_list[mid]:
            return mid
        elif elem <= sorted_list[mid]:
            lasts.append(mid-1)
        else:
            firsts.append(mid+1)
    return firsts[-1],lasts[-1]
