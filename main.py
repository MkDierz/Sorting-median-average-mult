def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return array


def getInput():
    try:
        print("array format")
        print("'1, 2, 3, ...' or '1 2 3 ...'")
        print("Input an array : ")
        inputval = input("")
        if any(("," in inputval) for i in inputval):
            print("using comma delimited")
            inputval = inputval.split(",")
            inputval = list(filter(None, inputval))
            for i in range(0, len(inputval)):
                inputval[i] = int(inputval[i])
            return inputval
        elif any((" " in inputval) for i in inputval):
            print("using space delimited")
            inputval = inputval.split(" ")
            inputval = list(filter(None, inputval))
            for i in range(0, len(inputval)):
                inputval[i] = int(inputval[i])
            return inputval
    except:
        print("!! INPUT ERROR TRY AGAIN !!")
        getInput()


def averageutil(array):
    average = 0
    for item in array:
        average += item
    average /= len(array)
    return average


def medianutil(array):
    length = len(array)
    if len(array) == 0:
        median_address = int(round(length / 2, 0))
        median_value = array[median_address]
    else:
        median_address = int(round(length / 2, 0))
        median_value = array[median_address] + array[median_address - 1]
        median_value /= 2
    return median_value


def multutil(array):
    mult = 0
    for item in array:
        if mult == 0:
            mult = item
        else:
            mult *= item
    return mult


def main():
    inputval = getInput()
    print("the input is",inputval)
    # print(inputval)
    sorted_input = sort(inputval)
    average = averageutil(inputval)
    median = medianutil(sorted_input)
    mult = multutil(sorted_input)
    print("sorted Input :", str(sorted_input))
    print("average :", average)
    print("median :", median)
    print("all number multiplied :", mult)


if __name__ == '__main__':
    main()
