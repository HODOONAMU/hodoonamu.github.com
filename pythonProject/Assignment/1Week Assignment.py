



while True:
    print('a 값을 입력하시오:')
    a = input()
    a = int(a)
    if a == 9999:
        print('계산기를 종료합니다.')
        break
    else:
        print('b 값을 입력하시오')
        b = input()
        b = int(b)

        result = a + b
        print(a, "+", b, "=", result)
        result = a - b
        print(a, "-", b, "=", result)
        result = a * b
        print(a, "*", b, "=", result)
        result = a / b
        print(a, "/", b, "=", result)