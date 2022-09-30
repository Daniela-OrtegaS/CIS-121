
import statistics

def mean(numbers):

    total = 0
    #for number in range(0,len(numbers)):
        #Loop para que sea desde el primer valor hasta el ultimo con "len"

    for number in numbers:
        total+=number

    result = total/len(numbers)

    return result


def median(numbers):
    result = statistics.median(numbers)
    return result