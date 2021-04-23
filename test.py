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


def reversed_list(lst1,lst2):
  index1 = 0
  index2 = len(lst2) - 1
  result = []

  for ls in lst1:
    if lst1[index1] == lst2[index2]:
      result.append(1)
      index1 += 1
      index2 -= 1
  count = 0
  for nr in result:
    if nr == 1:
      count += 1
  if count == len(lst1):
    return True
  else:
    return False

def every_other_letter(word):
  i = 0
  end = len(word)
  result = []
  while i < end:
    result.append(word[i])
    i += 2
  return "".join(result)


def reverse_string(word):
  dimensiune = len(word) -1
  output = []
  while dimensiune >= 0:
    output.append(word[dimensiune])
    dimensiune -= 1
  
  return "".join(output)

def max_key(my_dictionary):
  top_value = 0
  return_key = 0
  for key, value in my_dictionary.items():
    if value > top_value:
      return_key = key
  return return_key


max_key = {1:10, 2:3, 4:5}

for key, value in max_key.items():
  print(value)

