import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox, Toplevel
import os
import json


FILE_TEXT= "text.json"
contenier = []

if os.path.exists(FILE_TEXT):
    try:
        with open(FILE_TEXT, "r", encoding="utf-8") as file:
            contenier = json.load(file)
    except json.JSONDecodeError:
        contenier = []


def savecontenier():
    global contenier
    text = entry.get().strip()
    if not text:
        messagebox.showwarning("Error", "Введите текст для сохранения")
        return
    contenier.append(text)

    try:
        with open(FILE_TEXT, "w", encoding="utf-8") as file:
            json.dump(contenier, file, ensure_ascii=False, indent=2)
        messagebox.showinfo("Успешно", "Текст сохранен")
    except Exception as e:
        messagebox.showerror("Error", f"Не удалось сохранить файл: {e}")


def deletecontenier():
    global contenier 
    try:
        num = int(entry.get()) -1 
    except ValueError:
        messagebox.showwarning("Error", "Введите номер для удаления")
        return
    if 0 <= num < len(contenier) :
        contenier.pop(num)
        try:
            with open(FILE_TEXT, "w", encoding="utf-8") as file:
                json.dump(contenier, file, ensure_ascii=False, indent=2)
            messagebox.showinfo("Успешно", "Текст удалён")
        except Exception as e:
            messagebox.showerror("Error", f"Не удалось удалить текст: {e}")
    else:
        messagebox.showwarning("Error", "Номер не существует")
    

def printlist():
    win = Toplevel()
    win.title("Список задач")

    listbox = Listbox(win, width=50, height=10)
    listbox.pack(fill="both", expand=True)

    for i, task in enumerate(contenier, 1):
        listbox.insert("end", f"{i}. {task}")


root = tk.Tk()
root.title("ToDo List")
root.geometry("300x450")
root.configure(bg="#B5EBFD")
root.resizable(False, False)


label = tk.Label(text="Напишите задачу ", font="Arial, 18", bg="#B5EBFD", fg="black")
label.place(x=50, y=50)

entry = tk.Entry( font="Arial, 14", fg="#DB38FF",width=19)
entry.place(x=50, y=100)


button_take = tk.Button(text="Добавить в список в файл", command=savecontenier, font="Arial, 10", height=3, width=25, bg="#8DA1FD", fg="white")
button_take.place(x=50, y=150)

button_delet = tk.Button(text="Удалить из файла", command=deletecontenier,font="Arial, 10", height=3, width=25, bg="#8DA1FD", fg="white")
button_delet.place(x=50, y=250)

button_list = tk.Button(text="Показать список", command=printlist,font="Arial, 10", height=3, width=25, bg="#8DA1FD", fg="white")
button_list.place(x=50, y=350)


root.mainloop()


