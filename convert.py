import sys

n1 = input('変換したい値: ')
if not n1.isdecimal():
    print('整数を入力してください')
    sys.exit()
N1 = int(n1)

base1 = input('変換したい値の進数(1..16): ')
if not base1.isdecimal():
    print('整数を入力してください')
    sys.exit()
Base1 = int(base1)

if Base1 <= 1 or Base1 >= 16:
    print('数値の範囲がオーバーしています')
    sys.exit()

base2 = input('変換したい値の進数(2..16): ')
if not base2.isdecimal():
    print('整数を入力してください')
    sys.exit()

Base2 = int(base2)
if Base2 < 2 or Base2 > 16:
    print('数値の範囲がオーバーしています')
    sys.exit()


def convert(N1, Base1, Base2):
    result = ''

    if Base1 == 10:
        while N1 > 0:
            if N1 % Base2 == 10:
                result = 'A' + result
            elif N1 % Base2 == 11:
                result = 'B' + result
            elif N1 % Base2 == 12:
                result = 'C' + result
            elif N1 % Base2 == 13:
                result = 'D' + result
            elif N1 % Base2 == 13:
                result = 'E' + result
            elif N1 % Base2 == 13:
                result = 'F' + result
            else:
                result = str(N1 % Base2) + result
            N1 //= Base2
        return result
    result = 0
    for i in range(len(n1)):
        result += int(n1[i]) * (Base1 ** (len(n1) - i - 1))
    return convert(result, 10, Base2)
    
print(convert(N1, Base1, Base2))