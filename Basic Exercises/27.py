def common_elements(list1,list2):
    set1=set(list1)
    set2=set(list2)
    return set1 & set2

print("Common Elements:",common_elements([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))