#faulty calculator

num1 = int(input("write your first number: "))
num2 = int(input("Write your second number: "))
oper = input("Enter operator: ")
calculator = {"+": num1 + num2, "-": num1 - num2, "*": num1 * num2, "/": num1 / num2}
FaultyCalculator = {"+": "77", "*": "555", "/": "4"}
if num1 == 45 and num2 == 3:
    print(FaultyCalculator[oper])
elif num1 == 56 and num2 == 9:
    print(FaultyCalculator[oper])
elif num1 == 56 and num2 == 6:
    print(FaultyCalculator[oper])
else:
    print(calculator[oper])