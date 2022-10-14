def clenData(data):
    temp = []
    for i in data:
        if i.isdigit():
            temp.append(int(i))
    return temp


def openFile(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()

    data= clenData(data)

    return data

data = openFile("randomValues.txt")
print(data)

def findMin(index, current_min,data):
    if len(data) == 0:
        print("this list is empty")
    if len(data) == 1:
        return data[0]

    min = data[index]

#reviso si es menor o igual que mi primer index.
    if min <= current_min:
        current_min = min

    # [1,2,3,4]
    # 0  1 2 3

    if index >= len(data)-1:
        return current_min
    # estoy revisando si no llego al final de mi lista. El final de la lista es siempre "len(Data)-1"
    else:
        return findMin(index+1, current_min, data)
    #Si no es mi primer valor, mi index se mueve al siguiente.
print(findMin(0, data[0],data))


def findMax(index, current_max, data):
    if len(data) == 0:
        print("this list is empty")
    if len(data) == 1:
        return data[0]
    max = data[index]

    if max >= current_max:
        current_max = max

    if index >= len(data) - 1:
        return current_max
    else:
        return findMax(index + 1, current_max, data)
print(findMax(0, data[0],data))


def Extrema(data, calculate_Min = True, calculate_Max = True):
    if calculate_Min == True and calculate_Max == True:
        return[findMin(0,data[0],data),findMax(0,data[0],data)]
    elif calculate_Min == False and calculate_Max == False:
        return["Nothing was done"]

    elif calculate_Min == False:
        return[findMax(0, data[0],data)]
    elif calculate_Max == False:
        return[findMin(0,data[0], data)]
#tiene que darme los dos valores porque estoy asumiendo que los dos son verdad
print(Extrema(data))
#tiene que darme solo max  porque estoy diciendo que min es falso
print(Extrema(data,False))
#debe decirme que no hizo nada
print(Extrema(data,False,False))
print(Extrema(data,calculate_Max=False))
# file = open("randomValues.txt", "r")
# data = file.read().splitlines()
# randomValues = []
# for line in data:
#     if line.isdigit():
#         randomValues.append(line)
# print(randomValues)

#for recursion functions necesito una base function de lo que quiero que pase y saber adonde quiero parar. `
#recursion es mas lento que un loop. en recursin uso memory mas de una vez