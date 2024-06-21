def simpleCal(num, ope, num1):

    if ope == "*":
        result = num*num1
    elif ope == "-":
        result = num - num1
    elif ope == "/":
        result = num / num1
    elif ope == "+":
        result = num + num1
    return result


def main():

    userinput = input("enter here")
    arr = userinput.split()
    for i in range(len(arr)):
        if arr[i] not in ("*", "/", "-", "+"):
            arr[i] = int(arr[i])

    for i in range(1, len(arr), 2):
        if i == 1:
            res = simpleCal(arr[i-1], arr[i], arr[i+1])
        else:
            res = simpleCal(res, arr[i], arr[i+1])
    print(res)


if __name__ == "__main__":
    main()
