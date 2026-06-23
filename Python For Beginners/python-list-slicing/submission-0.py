from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:

    prim1=my_list[-1]
    prim2=my_list[-2]
    prim3=my_list[-3]
    return [prim3,prim2,prim1]

# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
