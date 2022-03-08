def set_intersection(set1,set2):
    s1=set1
    s2=set2
    a=s1.intersection(s2)
    return a    

set1={1,2,3,4,5,6,7}
set2={5,6,7,8,9}
A=set_intersection(set1,set2)
print(A)