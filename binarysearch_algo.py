def binary_search(list, val):
        list_size=len(list)-1
    
        index0=0
        indexN=list_size
    
        while index0 <= indexN:
            midval = (index0 + indexN) // 2
        
            if list[midval] == val:
                return midval
        
            if val > list[midval]:
                index0 = midval + 1
            else:
                indexN = midval - 1
        
        if index0 > indexN:
            return None
        

list1 = [2,7,19,34,53,72]

print(binary_search(list1, 72))
print(binary_search(list1, 11))
print(binary_search(list1, 19))