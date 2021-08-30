from tkinter import *


class Cryptography:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Cryptography")
        self.frame.geometry("415x450+400+150")

        self.title = Label(text="Cryptography", font="arial 25 bold")
        self.title.grid(row=0, column=0, columnspan=3)

        self.encrypt = Label(text="Encryption", font="arial 18 bold")
        self.encrypt.grid(row=1, column=0)

        self.t1 = Text(width=25, height=10)
        self.t1.grid(row=2, column=0)

        self.b1 = Button(text="Process", font="arial 13 bold", command=self.encryptor)
        self.b1.grid(row=3, column=0)

        self.t2 = Text(width=25, height=10)
        self.t2.grid(row=4, column=0)

        self.decrypt = Label(text="Decryption", font="arial 18 bold")
        self.decrypt.grid(row=1, column=1)

        self.t3 = Text(width=25, height=10)
        self.t3.grid(row=2, column=1)

        self.b2 = Button(text="Process", font="arial 13 bold", command=self.decrypter)
        self.b2.grid(row=3, column=1)

        self.t4 = Text(width=25, height=10)
        self.t4.grid(row=4, column=1)

        self.frame.mainloop()

    def encryptor(self):
        if len(self.t1.get("1.0", END)) != 1:
            message = self.t1.get("1.0", END)
            encMessage = ''
            for i in message:
                i = chr(ord(i) + 5)
                encMessage = encMessage + i
            self.t2.insert("1.0", encMessage)

    def decrypter(self):
        if len(self.t3.get("1.0", END)) != 1:
            message = self.t3.get("1.0", END)
            decMessage = ''
            for i in message:
                i = chr(ord(i) - 5)
                decMessage = decMessage + i
            self.t4.insert("1.0", decMessage)


crypt = Cryptography()
