from tkinter import *


class Calculator:
    def __init__(self):
        self.frame = Tk()
        self.frame.title('Calculator')
        self.frame.geometry('231x290+500+200')
        self.value = StringVar('')
        self.operation = str()
        self.num1 = int()
        self.num2 = int()
        self.input = Entry(self.frame, width=18, borderwidth=11, font='arial 14 bold', state=DISABLED,
                           textvariable=self.value)
        self.input.grid(row=0, column=0, columnspan=10)

        self.operation_label = Label(text=' ', font='arial 11 bold')
        self.operation_label.grid(row=0, column=4)
        self.nine = Button(text='9', font='arial 14 bold', width=3, height=2,
                           command=lambda: self.click_button(self.nine))
        self.nine.grid(row=1, column=0)

        self.eight = Button(text='8', font='arial 14 bold', width=3, height=2,
                            command=lambda: self.click_button(self.eight))
        self.eight.grid(row=1, column=1)

        self.seven = Button(text='7', font='arial 14 bold', width=3, height=2,
                            command=lambda: self.click_button(self.seven))
        self.seven.grid(row=1, column=2)

        self.mod = Button(text='mod', font='arial 14 bold', width=3, height=2,
                          command=lambda: self.click_button(self.mod))
        self.mod.grid(row=1, column=3)

        self.clear = Button(text='C', font='arial 14 bold', width=3, height=2,
                            command=lambda: self.click_button(self.clear))
        self.clear.grid(row=1, column=4)

        self.six = Button(text='6', font='arial 14 bold', width=3, height=2,
                          command=lambda: self.click_button(self.six))
        self.six.grid(row=2, column=0)

        self.five = Button(text='5', font='arial 14 bold', width=3, height=2,
                           command=lambda: self.click_button(self.five))
        self.five.grid(row=2, column=1)

        self.four = Button(text='4', font='arial 14 bold', width=3, height=2,
                           command=lambda: self.click_button(self.four))
        self.four.grid(row=2, column=2)

        self.multiply = Button(text='X', font='arial 14 bold', width=3, height=2,
                               command=lambda: self.click_button(self.multiply))
        self.multiply.grid(row=2, column=3)

        self.divide = Button(text='/', font='arial 14 bold', width=3, height=2,
                             command=lambda: self.click_button(self.divide))
        self.divide.grid(row=2, column=4)

        self.three = Button(text='3', font='arial 14 bold', width=3, height=2,
                            command=lambda: self.click_button(self.three))
        self.three.grid(row=3, column=0)

        self.two = Button(text='2', font='arial 14 bold', width=3, height=2,
                          command=lambda: self.click_button(self.two))
        self.two.grid(row=3, column=1)

        self.one = Button(text='1', font='arial 14 bold', width=3, height=2,
                          command=lambda: self.click_button(self.one))
        self.one.grid(row=3, column=2)

        self.addition = Button(text='+', font='arial 14 bold', width=3, height=2,
                               command=lambda: self.click_button(self.addition))
        self.addition.grid(row=3, column=3)

        self.subtract = Button(text='-', font='arial 14 bold', width=3, height=2,
                               command=lambda: self.click_button(self.subtract))
        self.subtract.grid(row=3, column=4)

        self.zero = Button(text='0', font='arial 14 bold', width=3, height=2,
                           command=lambda: self.click_button(self.zero))
        self.zero.grid(row=4, column=0)

        self.percentage = Button(text='%', font='arial 14 bold', width=3, height=2,
                                 command=lambda: self.click_button(self.percentage))
        self.percentage.grid(row=4, column=1)

        self.equal = Button(text='=', font='arial 14 bold', width=11, height=2,
                            command=lambda: self.click_button(self.equal))
        self.equal.grid(row=4, column=2, columnspan=14)
        self.frame.mainloop()

    def click_button(self, btn):
        if self.operation_label['text'] == '=':
            self.value.set('0')
            self.operation_label.config(text='')
        if btn == self.clear:
            self.value.set('0')
            self.operation_label.config(text=' ')
        elif btn['text'] == '=':
            self.num2 = int(self.value.get())
            self.operation_label.config(text='=')
            if self.operation == '+':
                self.value.set(self.num1 + self.num2)
            elif self.operation == '-':
                self.value.set(self.num1 - self.num2)
            elif self.operation == '/':
                if self.num2 == 0:
                    self.value.set('Cannot divide by 0')
                else:
                    self.value.set(self.num1 / self.num2)
            elif self.operation == 'X':
                self.value.set(self.num1 * self.num2)
            elif self.operation == 'mod':
                self.value.set(self.num1 % self.num2)
        elif self.value.get() == 'Cannot divide by 0':
            self.value.set('0')
        elif btn['text'] == '+':
            self.num1 = int(self.value.get())
            self.value.set('')
            self.operation = '+'
            self.operation_label.config(text='+')
        elif btn['text'] == '-':
            self.num1 = int(self.value.get())
            self.value.set('')
            self.operation = '-'
            self.operation_label.config(text='-')
        elif btn['text'] == '/':
            self.num1 = int(self.value.get())
            self.value.set('')
            self.operation = '/'
            self.operation_label.config(text='/')
        elif btn['text'] == 'X':
            self.num1 = int(self.value.get())
            self.value.set('')
            self.operation = 'X'
            self.operation_label.config(text='X')
        elif btn['text'] == 'mod':
            self.num1 = int(self.value.get())
            self.value.set('')
            self.operation = 'mod'
            self.operation_label.config(text='mod')
        elif btn['text'] == '%':
            self.value.set(int(self.value.get())/100)
        else:
            self.value.set(self.value.get() + btn['text'])
        self.frame.update()


calc = Calculator()
