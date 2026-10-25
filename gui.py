import tkinter as tk
import operation
import parser


def validate_input(value):
    """检查输入的字符是否合规"""
    allowed = "0123456789+-x÷.()"
    return all(char in allowed for char in value)

def create_buttons(parent, text, row, column):
    """创建按钮"""
    if text == "=":
        button = tk.Button(parent, text="=", command=calculate_result, font=("Arial", 20), width=6, height=2)
    elif text == "C":
        button = tk.Button(parent, text="C", command=clear_display, font=("Arial", 20), width=6, height=2)
    elif text == "⌫":
        button = tk.Button(parent, text="⌫", command=delete, font=("Arial", 20), width=6, height=2)
    else:
        button = (tk.Button(parent, text=text, command=lambda: button_click(text), font=("Arial", 20), width=6, height=2))
    button.grid(row=row, column=column)

def button_click(value):
    """非功能按键点击效果"""
    display.insert(tk.END, value)

def calculate_result():
    """计算算式结果"""
    expression = display.get()

    try:
        result = parser.parse(expression)
    except Exception:
        result = "Error"

    display.delete(0, tk.END)
    display.insert(tk.END, result)

def clear_display():
    """清空数值"""
    display.delete(0, tk.END)

def delete():
    """退格"""
    display.delete(len(display.get()) - 1, tk.END)

if __name__ == '__main__':
    window = tk.Tk()  # 创建窗口
    window.title("计算器")  # 设置窗口标题
    window.iconbitmap("calculator.ico")  # 设置窗口图标
    window.geometry("454x580")  # 设置窗口大小
    window.resizable(False, False)  # 禁止调整窗口大小

    display_frame = tk.Frame(window)  # 数据展示区
    display_frame.pack(fill="x", padx=10, pady=10)  # 沿 x 轴填充，左右各留 10 像素

    button_frame = tk.Frame(window)  # 按钮区
    button_frame.pack()

    validate_command = window.register(validate_input)

    display = (tk.Entry(display_frame,
             font=("Arial", 50),
             justify="right",
             validate="key",
             validatecommand=(validate_command, "%P")))
    display.pack(fill="x", padx=10, pady=10)

    buttons = [
        ["(", ")", "C", "⌫"],
        ["7", "8", "9", "÷"],
        ["4", "5", "6", "x"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"]
    ]

    for row, button_row in enumerate(buttons):
        for column, text in enumerate(button_row):
            create_buttons(button_frame, text, row, column)

    window.mainloop()
