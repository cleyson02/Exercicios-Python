def calculaMaior(num1, num2):
    if num1 > num2:
        return num1
    return num2

print("Digite dois números para saber o maior entre eles.")

while True:
    num1 = int(input("Digite 1o número: "))
    num2 = int(input("Digite 2o número: "))
    break

print (calculaMaior(num1, num2), "é o maior número.")