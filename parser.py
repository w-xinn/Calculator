import operation


def tokenize(expression):
    """拆分算式"""
    tokens= []
    number = ""

    for char in expression:
        if char in ["+", "-", "x", "÷", "(", ")"]:
            if number:
                tokens.append(number)
                number = ""
            tokens.append(char)
        else:
            number += char

    if number:
        tokens.append(number)

    return tokens

# 参考教程：
# YouTube: DIY Programming Language #1: The Shunting Yard Algorithm
# https://www.youtube.com/watch?v=unh6aK8WMwM&t=488s
# 观看时间：2026-10-24
# 用于实现本项目的表达式解析器
def parse(expression: str) -> float:
    """将算式解析成后缀表达式，并计算后缀表达式的结果"""
    holding_stack = []
    output = []
    solve_stack = []

    # 运算符及其优先级
    priority = {
        "+": 1,
        "-": 1,
        "x": 2,
        "÷": 2,
    }

    expression = tokenize(expression)

    for token in expression:
        # token如果是数值，则直接压入output
        if token.isdigit():
            output.append(float(token))
        # token如果是运算符
        elif token in ["+", "-", "x", "÷"]:
            # holding_stack栈内有元素
            while holding_stack:
                # 如果栈顶是 ( ，不比较，当前运算符直接压入holding_stack
                if holding_stack[-1] == "(":
                    break
                # 如果栈顶是运算符则比较当前运算符和栈顶运算符之间的优先级
                else:
                    # 当前运算符优先级 > 栈顶元素优先级，直接入栈
                    if priority[token] > priority[holding_stack[-1]]:
                        break
                    # 当前运算符优先级 <= 栈顶元素优先级，弹出栈顶运算符压入output，再入栈
                    else:
                        output.append(holding_stack.pop())

            holding_stack.append(token)
        # token如果是左括号(，直接压入holding_stack
        elif token == "(":
            holding_stack.append(token)
        # token如果是右括号)，则不压入holding_stack，不断弹出holding_stack栈顶元素压入output，直到遇到左括号，并且丢弃左括号
        elif token == ")":
            while holding_stack[-1] != "(":
                output.append(holding_stack.pop())

            holding_stack.pop()

    # 弹出holding_stack中的元素压入output中
    while holding_stack:
        output.append(holding_stack.pop())

    for token in output:
        if token in ["+", "-", "x", "÷"]:
            num_2 = solve_stack.pop()
            num_1 = solve_stack.pop()
            result = operation.calculate(num_1, num_2, token)
            solve_stack.append(result)
        else:
            solve_stack.append(token)

    return solve_stack[0]
