import subprocess
import tkinter


def open_file(event):
    file_pth = r"doge.jpg"
    subprocess.run(['start', file_pth], shell=True)


root = tkinter.Tk()
btn = tkinter.Button(root, text="open", command=lambda: open_file(None))
btn.pack()
root.mainloop()
