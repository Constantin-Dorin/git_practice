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