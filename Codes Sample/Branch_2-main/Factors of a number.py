def factors(num):
    output_list=[]
    for i in range(1,1000):
        if num%i==0:
            output_list.append(i)
        else:
            continue
    else:
        pass
    return output_list