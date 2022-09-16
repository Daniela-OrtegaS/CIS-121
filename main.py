# Daniela Ortega
# 9/16/22


number = 1
upper_bound = (int(input("Please enter an upper bound for a check")))
suma=0
perfect = 0
deficient = 0
abundant = 0


while number <= upper_bound:
    x = 1
    suma = 0
    while x< number:
        if number % x == 0:
            suma = suma+x
        x+=1

    if suma == number :
        perfect+=1
    elif suma < number:
        deficient+=1
    elif suma > number:
        abundant +=1

    number += 1

print("between 1 and", upper_bound, "there are", perfect," perfect numbers", deficient," deficient numbers", abundant,"abundant numbers")













