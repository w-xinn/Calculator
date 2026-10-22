import json


class History:
    def __init__(self):
        self.calculation_history = []

    def add_history(self, num_1: float, num_2: float, operator: str, result: float) -> None:
        """保存计算记录，并返回保存的记录"""
        record = {
            "num_1": num_1,
            "operator": operator,
            "num_2": num_2,
            "result": result
        }
        self.calculation_history.append(record)

    def show_history(self) -> None:
        """查看历史记录"""
        print("===== 计算历史 =====")

        if not self.calculation_history:
            print("暂无历史记录。")
            return

        for index, record in enumerate(self.calculation_history, start=1):
            print(f"{index}: {record['num_1']} {record['operator']} {record['num_2']} = {record['result']}")


    def save_history(self):
        with open("data/history.json", "w", encoding="utf-8") as f:
            json.dump(self.calculation_history, f, indent=2, ensure_ascii=False)

    def load_history(self):
        """加载历史记录"""
        try:
            with open("data/history.json", "r", encoding="utf-8") as f:
                self.calculation_history = json.load(f)
        except FileNotFoundError:
            print("文件不存在！")