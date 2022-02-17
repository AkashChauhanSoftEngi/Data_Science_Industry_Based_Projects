def str_list_func(str1):
    list1 = str1.split()
    for i in range(len(list1)):
        l = list(list1[i])
        
        if(len(l) == 1):
            continue
        else:
            first = l[0]
            last = l[-1]
            temp = first
            first = last
            last = temp
            l[0] = first
            l[-1] = last
        
        delimeter1 = ""
        list1[i] = delimeter1.join(l)
            
    
    delimeter2 = " "
    str1 = delimeter2.join(list1)
    
    return str1
        
        
print(str_list_func('I am learning Python at CloudxLab'))
