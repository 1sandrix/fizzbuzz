def fizzbuzz(maximum=100):
    output = []

    for number in range(1, maximum + 1):
        if number % 3 == 0:
            output.append("Fizz")
        else:
            output.append(number)

    return output