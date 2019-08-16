def can_divide(numbers, divisor):
    # result = []
    # for number in numbers:
    #     if number% divisor ==0:
    #         result.append(number)

    # if result == []:
    #     result.append(-1)

    # return sorted(result)


    answer = [number for number in numbers if not number % divisor]
    answer = sorted(answer) if answer else [-1]

    return answer




if __name__ == '__main__':
    print(can_divide([20, 3, 5, 7], 5))
    print(can_divide([4, 3, 2, 1], 1))
    print(can_divide([7, 11, 13], 3))