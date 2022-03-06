def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 

DecimalToBinary(33)

def number_pow_two(n):
    count = 0
    st = str(bin(n))
    st = st[2:]

    for i in range(0,len(st)):
        if(st[i] == '1'):
            count += 1
        
    if(count == 1):
        print(count -1)
    else:
        print(count - 1)
print()
number_pow_two(33)











# import math
# num = int(input('Enter your number:'))
# def number_pow_two(num):
#         answer = math.log(num, 2)
#         counter += 1
#         if math.log(num, 2) == 0:
#             break
#