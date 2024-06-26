l=['abc','efg','abc']

for str in l:
    reversed_string =''
    for i in range(len(str)-1,-1,-1):
        reversed_string += str[i]
    print(reversed_string)