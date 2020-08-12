# Capitalizing first letter of each word 
name = input("Give a name: ")
name_list = name.split()
name_len = len(name_list)
new_name_list = []
for i in range(0, name_len):
    cap = name_list[i].capitalize()
    new_name_list.append(cap)
print(" ".join(new_name_list))