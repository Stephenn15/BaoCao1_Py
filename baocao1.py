import tkinter as tk

# Hàm thực hiện phép tính
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))  # Tính toán biểu thức
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Khởi tạo ứng dụng GUI
win = tk.Tk()
win.title("Calculator")
win.geometry("300x400")

expression = ""
input_text = tk.StringVar()

# Phần hiển thị đơn giản
input_field = tk.Entry(win, textvariable=input_text, font=('arial', 18), justify='right')
input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10)

# Tạo các nút bấm
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(win, text=button, width=10, height=3, command=lambda: btn_equal())
    elif button == "C":
        btn = tk.Button(win, text=button, width=10, height=3, command=lambda: btn_clear())
    else:
        btn = tk.Button(win, text=button, width=10, height=3, command=lambda b=button: btn_click(b))
    
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

win.mainloop()
