isCalculating = True
while isCalculating:
    while True:
        try:
            num_1 = float(input("请输入第一个数：").strip())
            break
        except ValueError:
            print("输入格式错误，请输入有效的数字！")

    while True:
        operator = input("请选择运算符(+ - * /):").strip()
        if(operator not in ["+", "-", "*", "/"]):
            print("请选择正确的运算符！")
            continue
        break

    while True:
        try:
            num_2 = float(input("请输入第二个数：").strip())
            if (operator == "/" and num_2 == 0):
                print("除数不能为0！")
                continue    
            break
        except ValueError:
            print("输入格式错误，请输入有效的数字！")
    
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    elif operator == "/":
        result = num_1 / num_2
    print(f"{num_1} {operator} {num_2} = {result}")

    while True:
        choice = input("是否继续运算？(Y/N)")
        if choice.upper() == "N":
            isCalculating = False
            break
        elif choice.upper() == "Y":
            break
        else:
            print("请输入有效的选项！")
            