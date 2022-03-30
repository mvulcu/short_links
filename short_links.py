import pyshorteners
from tkinter import*
from tkinter import messagebox
import pyperclip

root = Tk()
root.title("URL shortener")
root.geometry("400x260")
root["bg"] = "#01577D"
Label(root, text="Hi there,\n you can shorten your link here!", font="Calibri 15 bold", bg="#01577D",
      fg="#EDC339").pack(pady=5)
Label(root, text="your link:", font="Calibri 11 bold", bg="#01577D", fg="#EDC339").pack(pady=5)
link = Entry(root, width=40)
link.pack()

Label(root, text="short link", font="Calibri 11 bold", bg="#01577D", fg="#EDC339").pack(pady=5)
res = Entry(root, width=40)
res.pack()

def copytoclipboard():
    url = res.get()
    pyperclip.copy(url)

def short():
    try:
        a = link.get()
        s = pyshorteners.Shortener().tinyurl.short(a)
        res.insert(0, s)
    except:
        messagebox.showerror("ERROR", "Incorrect link")


Button(root, text="submit", command=short, font="Calibri 11 bold", bg="#01577D", fg="#EDC339").pack(pady=10)
Button(root, text="copy", command=copytoclipboard, font="Calibri 11 bold", bg="#01577D", fg="#EDC339").pack(pady=5)
root.mainloop()
