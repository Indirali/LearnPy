import tkinter as tk

#生成一个根窗口
app = tk.Tk()
#标题
app.title("Hello World")
#label组件
theLabel = tk.Label(app, text='我的第二个窗口程序')
theLabel.pack()

app.mainloop()