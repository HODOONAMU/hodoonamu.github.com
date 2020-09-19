#실습 2
value = input('정수를 입력하세요:')

if(value == 'q'):
    print('프로그램을 종료합니다.')
    exit()
elif(value.isdigit() == False):
    #.isdigiti() = 문자열이 숫자인지 아닌지를 판단하는 함수
    #.isalpha() = 문자열이 문자인지 아닌지를 판단하는 함수
    print('올바른 정수가 아닙니다. 프로그램을 종료합니다.')
    exit()
elif(int(value) % 2 == 0):
    print('짝수입니다.')
elif(int(value) % 2 != 0):
    print('홀수입니다.')
