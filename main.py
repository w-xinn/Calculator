import history
import operation



def main():
    calculating = True  # 程序进入计算状态

    calc = history.History()

    calc.load_history()  # 加载历史计算记录

    while calculating:
        while True:
            try:
                num_1 = float(input("请输入第一个数：").strip())
                break
            except ValueError:
                print("输入格式错误，请输入有效的数字！")

        while True:
            operator = input("请选择运算符(+ - * /):").strip()
            if operator not in ["+", "-", "*", "/"]:
                print("请选择正确的运算符！")
                continue
            break

        while True:
            try:
                num_2 = float(input("请输入第二个数：").strip())
                if operator == "/" and num_2 == 0:
                    print("除数不能为0！")
                    continue    
                break
            except ValueError:
                print("输入格式错误，请输入有效的数字！")
        
        result = operation.calculate(num_1, num_2, operator)

        # 保存计算记录并打印    
        print(f"{num_1} {operator} {num_2} = {result}")  
        calc.add_history(num_1, num_2, operator, result)

        while True:
            choice = input("是否继续运算？(Y=继续，N=退出，H=历史)")
            if choice.upper() == "N":
                calculating = False
                break
            elif choice.upper() == "Y":
                break
            elif choice.upper() == "H":
                calc.show_history()

            else:
                print("请输入有效的选项！")

        calc.save_history()

if __name__ == "__main__":
    main()

