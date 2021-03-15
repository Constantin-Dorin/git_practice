<<<<<<< HEAD
def delete_starting_evens(lst):
    elemente = range(len(lst))
    output = []
    for index in elemente:
        if lst[index] % 2 == 0:
            continue
        else:
            output = lst[index:]
            break
    return output


lista = [4, 8, 10, 11, 12, 15]

print(delete_starting_evens(lista))
=======
#This is a practice file
>>>>>>> faa932103a0a85344653b43b46b39721351977fa
