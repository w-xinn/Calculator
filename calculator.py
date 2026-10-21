isCalculating = True
while isCalculating:
    try:
        num_1 = float(input("请输入第一个数：").strip())
        operator = input("请选择运算符(+ - * /):").strip()
        num_2 = float(input("请输入第二个数：").strip())
        result = 0.0

        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "*":
            result = num_1 * num_2
        elif operator == "/":
            # 当除数为 0 时给出提示。
            if num_2 == 0:
                print("除数不能为0！")
                continue    

            result = num_1 / num_2
        else:
            print("请选择正确的运算符！")
            continue

        print(result)

        while True:
            choice = input("是否继续运算？(Y/N)")
            if choice.upper() == "N":
                isCalculating = False
                break
            elif choice.upper() == "Y":
                break
            else:
                print("请输入有效的选项！")
                continue
    except ValueError:
        print("输入格式错误，请输入有效的数字！")