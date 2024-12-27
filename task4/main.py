import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def Save():
    try:
        content = text.get("1.0", tk.END).strip()
        saveTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newContent = f"{saveTime} 保存数据如下：\n{content}"
        with open("note.txt", "w", encoding="utf-8") as file:
            file.write(newContent)
        text.delete("1.0", tk.END)
        text.insert(tk.END, newContent)
        messagebox.showinfo("提示", "文件保存成功！")
    except Exception as e:
        messagebox.showerror("错误", f"保存文件失败：{e}")

def Read():
    try:
        with open("note.txt", "r", encoding="utf-8") as file:
            content = file.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, content)
        messagebox.showinfo("提示", "文件读取成功！")
    except FileNotFoundError:
        messagebox.showwarning("警告", "文件不存在！请先保存内容。")
    except Exception as e:
        messagebox.showerror("错误", f"读取文件失败：{e}")



app = tk.Tk()
app.title("简易记事本")

text = tk.Text(app, width=50, height=20, font=("Arial", 12))
text.pack(padx=10, pady=10)

frame = tk.Frame(app)
frame.pack(pady=5)

saveButton = tk.Button(frame, text="保存文件", command=Save, width=15)
saveButton.grid(row=0, column=0, padx=5)

readButton = tk.Button(frame, text="读取文件", command=Read, width=15)
readButton.grid(row=0, column=1, padx=5)

app.mainloop()
