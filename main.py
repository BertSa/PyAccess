import os
import tkinter as tk
from tkinter import font

from windowwww import copy_to_clip


class Main:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Py Access")
        self.window.geometry("300x150")
        my_font = font.Font(family='Helvetica', size=15, weight='bold')
        self.text_message = tk.StringVar()
        self.text_message.set("")
        self.label_message = tk.Label(self.window, textvariable=self.text_message)
        self.btn_quit = tk.Button(self.window, text="Quitter", command=self.window.quit)
        self.btn_keyboard = tk.Button(self.window, text="Keyboard", command=self.keyboardfn)
        self.btn_usb_access = tk.Button(self.window, text="USB Access", command=self.usb_access)
        self.btn_copy_token_gh = tk.Button(self.window, text="Copy Token GH", command=copy_to_clip)

        self.btn_quit["fg"] = "red"
        self.btn_quit["font"] = my_font
        self.btn_keyboard["fg"] = "blue"
        self.btn_keyboard["font"] = my_font
        self.btn_usb_access["fg"] = "green"
        self.btn_usb_access["font"] = my_font
        self.btn_copy_token_gh["fg"] = "grey"
        self.btn_copy_token_gh["font"] = my_font

        self.btn_keyboard.pack()
        self.btn_usb_access.pack()
        self.btn_copy_token_gh.pack()
        self.btn_quit.pack()
        self.window.mainloop()

    def keyboardfn(self):
        self.label_message.pack_forget()
        os.system("sudo /opt/scripts/keyboardfn.sh")
        self.changeText("Done!")
        self.label_message.pack()

    def usb_access(self):
        self.label_message.pack_forget()
        code_returned = os.system("sudo /opt/scripts/usbAccess.sh")
        if code_returned == 256:
            self.changeText("USB non connecter!")
        elif code_returned == 0:
            self.changeText("Done!")
        else:
            self.changeText("ERROR!")
        self.label_message.pack()

    def changeText(self, msg):
        print(msg)
        self.text_message.set(msg)


if __name__ == "__main__":
    Main()
