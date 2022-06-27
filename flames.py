
from itertools import count
from turtle import left, right
from unittest import result

from cv2 import split


a = input("enter boy name:" )
b = input("enter girl name:" )


list_first = list(a.lower())
list_second = list(b.lower())

j = 0
for i in list_first:
    if i in list_second:
        k=list_first.index(i,j)
        
        list_first.insert(k + 1 ,"x")
        j = k + 1

for i in list_first:
    if i in list_second:
        
        list_first.remove(i)
        list_second.remove(i)
       
str_first= "".join(list_first)
result_first = str_first.replace("x","") 
# print(result_first)
# ------------------------------------------------------------------------------------------------------

list_first_r= list(a.lower())
list_second_r = list(b.lower())

z = 0
for i in list_second_r:
    if i in list_first_r:
        k_r=list_second_r.index(i,z)
        
        list_second_r.insert(k_r + 1 ,"x")
        z = k_r + 1
        
for i in list_second_r:
    if i in list_first_r:
        
        list_second_r.remove(i)
        list_first_r.remove(i)
       
str_first_r= "".join(list_second_r)
result_first_r = str_first_r.replace("x","") 
# print(result_first_r)

final_string_len = len(result_first + result_first_r)
print(final_string_len)
list_flames =["friend","love","affection","marriage","enemy","sibilings"]


while len(list_flames) > 1:
    split_index = (final_string_len % len(list_flames) - 1)
    
    if split_index >= 0:
        right = list_flames[split_index +1 :]
        left = list_flames[: split_index]
        
        list_flames = right + left
    
    else:
        list_flames = list_flames[ : len(list_flames) - 1]
        
print("relationship:",list_flames[0])