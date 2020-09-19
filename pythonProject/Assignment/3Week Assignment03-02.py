#실스브 3-2
x = 100
result = 0
while x < 201:
    if(x % 2 == 0):
        result = x + result
        print(result,',', x)
    x = x + 1