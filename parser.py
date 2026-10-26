import operation


def tokenize(expression):
    """拆分算式"""
    tokens= []
    number = ""

    for char in expression:
        char = char.strip()
        if char in ["+", "×", "÷", "(", ")"]:
            if number:
                tokens.append(number)
                number = ""
            tokens.append(char)
        elif char == "-":
            if not tokens or tokens[-1] in ["+", "×", "÷", "(", ")"]:
                number += char
            else:
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
def parse(expression: str) -> float | str:
    """将算式解析成后缀表达式，并计算后缀表达式的结果"""
    if len(expression) == 0:
        return ""

    holding_stack = []
    output = []
    solve_stack = []

    # 运算符及其优先级
    priority = {
        "+": 1,
        "-": 1,
        "×": 2,
        "÷": 2,
    }

    tokens = tokenize(expression)

    if not validate(tokens):
        return "Error"

    for token in tokens:
        # token如果是数值，则直接压入output
        if is_number(token):
            output.append(float(token))
        # token如果是运算符
        elif token in ["+", "-", "×", "÷"]:
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
        if token in ["+", "-", "×", "÷"]:
            num_2 = solve_stack.pop()
            num_1 = solve_stack.pop()
            result = operation.calculate(num_1, num_2, token)
            solve_stack.append(result)
        else:
            solve_stack.append(token)

    return solve_stack[0]

def is_number(token):
    """判断是否为数值"""
    try:
        float(token)
        return True
    except ValueError:
        return False

def validate(tokens: list) -> bool:
    """检查表达式是否合法"""
    left_parenthesis_count = 0
    right_parenthesis_count = 0

    if len(tokens) == 1 and tokens[0] in ["+", "-", "×", "÷", ")"]:
        return False

    for i in range(len(tokens)):
        # 第一个位置
        if i == 0:
            # token 只能是数字或者(
            if not (is_number(tokens[i]) or tokens[i] == "("):
                return False
            elif tokens[i] == "(":
                left_parenthesis_count += 1
                if not (is_number(tokens[i + 1]) or tokens[i + 1] == "("):
                    return False
        # 最后一个位置
        elif i == len(tokens) - 1:
            # token 只能是数字或者 )
            if not (is_number(tokens[i]) or tokens[i] == ")"):
                return False
            elif tokens[i] == ")":
                right_parenthesis_count += 1
        # 其他位置
        else:
            if is_number(tokens[i]):
                if tokens[i + 1] not in ["+", "-", "×", "÷", ")"]:
                    return False
            elif tokens[i] in ["+", "-", "×", "÷"]:
                if not (is_number(tokens[i + 1]) or tokens[i + 1] == "("):
                    return False
            elif tokens[i] == "(":
                left_parenthesis_count += 1
                if not (is_number(tokens[i + 1]) or tokens[i + 1] == "("):
                    return False
            elif tokens[i] == ")":
                right_parenthesis_count += 1
                if right_parenthesis_count > left_parenthesis_count:
                    return False
                elif tokens[i + 1] not in ["+", "-", "×", "÷", ")"]:
                    return False

    if right_parenthesis_count != left_parenthesis_count:
        return False

    return True
