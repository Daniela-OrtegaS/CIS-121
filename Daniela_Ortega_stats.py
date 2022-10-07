import statistics

def mean(numbers):

    total = 0
    for number in numbers:
        total += number

    result = total/len(numbers)
    return result

def median(numbers):
    result = statistics.median(numbers)
    return result

def mode(numbers):
    result = statistics.multimode(numbers)
    return result



