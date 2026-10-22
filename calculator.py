isCalculating = True
history = []  # 记录历史计算结果

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
    history.append(f"{num_1} {operator} {num_2} = {result}")

    while True:
        choice = input("是否继续运算？(Y=继续，N=退出，H=历史)")
        if choice.upper() == "N":
            isCalculating = False
            break
        elif choice.upper() == "Y":
            break
        elif choice.upper() == "H":
            print("===== 计算历史 =====")

            for index, record in enumerate(history, start=1):
                print(f"{index}: {record}")
        else:
            print("请输入有效的选项！")
