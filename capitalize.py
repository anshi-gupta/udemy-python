# Capitalizing first letter of each word 
name = input("Give a name: ")
name_list = name.split()
name_len = len(name_list)
result = name.title()

##new_name_list = []
##for i in range(0, name_len):
##    cap = name_list[i].capitalize()
##    new_name_list.append(cap)
##print(" ".join(new_name_list))

for i in range(name_len):
    if name_list[i][0].isdigit() == True:
        alnum_str = name_list[i]
        result = result.replace(alnum_str.title(), alnum_str)
print(result)