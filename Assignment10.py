def create_largest_number(number_list):
    num=""
    number_list=sorted(number_list)
    for x in range(-1,-len(number_list)-1,-1):
        num+=str(number_list[x])
    return int(num)
number_list=[23,45,67]
