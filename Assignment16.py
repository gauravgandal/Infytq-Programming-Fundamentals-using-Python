def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1
        for y in range(index,len(num_list)):
            if x+num_list[y]==n:
                count+=1
    return count
num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))