def calculate(num_1: float, num_2: float, operator: str) -> float:

    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "×":
        result = num_1 * num_2
    elif operator == "÷":
        result = num_1 / num_2

    return result