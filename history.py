calculation_history = []

def add_history(num_1: float, num_2: float, operator: str, result: float) -> str:
    """保存计算记录，并返回保存的记录"""
    record = f"{num_1} {operator} {num_2} = {result}"
    calculation_history.append(record)
    return record

def show_history() -> None:
    """查看历史记录"""
    print("===== 计算历史 =====")

    if not calculation_history:
        print("暂无历史记录。")
        return

    for index, record in enumerate(calculation_history, start=1):
        print(f"{index}: {record}")