def cube_append(arb_list):
    apnd_list = list()
    for num in range(len(arb_list)):
        cubed_num = pow(num, 3)
        apnd_list.append(cubed_num)
    return apnd_list


arbitary_list = [1, 2, 4, 4, 3, 5, 6]
print("List after cubing each elements and appending to another list : ")
final_list = cube_append(arbitary_list)
print(final_list)