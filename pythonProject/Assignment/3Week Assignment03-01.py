#실습 3-1
result = 0
for x in range(0, 11):
    if(x % 2 != 0):
        result = result + x
        #print(f'{result} = {result} + {x}')
print(result)