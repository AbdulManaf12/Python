import threading
from tkinter import Tk, Label, Entry, Button, StringVar, DISABLED, ACTIVE, messagebox, HIDDEN
from time import sleep
import random,os

class Tic_Tac_Game:
    def __init__(self):
        self.Turn = True
        self.buttonClicks = 0
        self.frame = Tk()
        self.frame.geometry('400x450')
        self.frame.title('Tic Tac Game')
        self.frame.configure(bg='Gray')
        self.l1 = Label(text="Computer  ", font='Times 20 bold', bg='white', fg='black', height=1, width=25)
        self.l1.grid(column=0, row=0, columnspan=5)
        self.player2_name = StringVar()
        self.t2 = Entry(self.frame, textvariable=self.player2_name, bd=10, width=28)
        self.t2.grid(column=0, row=1, columnspan=5)
        self.l2 = Label(text='', font='Times 20 bold', bg='white', fg='black', height=1, width=25)

        self.Start = Button(text='Start', font='Times 10 bold', width=12, height=1, borderwidth=10, command=self._start_Game_)
        self.Start.grid(column=0, row=2, columnspan=5)

        self.b1 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b1))
        self.b1.grid(column=0, row=3)
        self.b2 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b2))
        self.b2.grid(column=1, row=3)
        self.b3 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b3))
        self.b3.grid(column=2, row=3)
        self.b4 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b4))
        self.b4.grid(column=0, row=4)
        self.b5 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b5))
        self.b5.grid(column=1, row=4)
        self.b6 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b6))
        self.b6.grid(column=2, row=4)
        self.b7 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b7))
        self.b7.grid(column=0, row=5)
        self.b8 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b8))
        self.b8.grid(column=1, row=5)
        self.b9 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b9))
        self.b9.grid(column=2, row=5)
        self._disable_all_button()

        self.frame.mainloop()

    def _isWin_(self):
        if (self.b1['text'] == 'X' and self.b2['text'] == 'X' and self.b3['text'] == 'X' or
                self.b4['text'] == 'X' and self.b5['text'] == 'X' and self.b6['text'] == 'X' or
                self.b7['text'] == 'X' and self.b8['text'] == 'X' and self.b9['text'] == 'X' or
                self.b1['text'] == 'X' and self.b4['text'] == 'X' and self.b7['text'] == 'X' or
                self.b2['text'] == 'X' and self.b5['text'] == 'X' and self.b8['text'] == 'X' or
                self.b3['text'] == 'X' and self.b6['text'] == 'X' and self.b9['text'] == 'X' or
                self.b1['text'] == 'X' and self.b5['text'] == 'X' and self.b9['text'] == 'X' or
                self.b3['text'] == 'X' and self.b5['text'] == 'X' and self.b7['text'] == 'X'):
            self._disable_all_button()
            if messagebox.askyesno(title='Result', message=self.player2_name.get()+' won the match\n Do you want play again?'):
                self._restart_()
            else:
                self.frame.destroy()
            return True
        elif (self.b1['text'] == 'O' and self.b2['text'] == 'O' and self.b3['text'] == 'O' or
              self.b4['text'] == 'O' and self.b5['text'] == 'O' and self.b6['text'] == 'O' or
              self.b7['text'] == 'O' and self.b8['text'] == 'O' and self.b9['text'] == 'O' or
              self.b1['text'] == 'O' and self.b4['text'] == 'O' and self.b7['text'] == 'O' or
              self.b2['text'] == 'O' and self.b5['text'] == 'O' and self.b8['text'] == 'O' or
              self.b3['text'] == 'O' and self.b6['text'] == 'O' and self.b9['text'] == 'O' or
              self.b1['text'] == 'O' and self.b5['text'] == 'O' and self.b9['text'] == 'O' or
              self.b3['text'] == 'O' and self.b5['text'] == 'O' and self.b7['text'] == 'O'):
            self._disable_all_button()
            if messagebox.askyesno(title='Result', message='Computer won the match\n Do you want play again?'):
                self._restart_()
            else:
                self.frame.destroy()
            return True
        return False

    def _disable_all_button(self):
        self.b1.configure(state=DISABLED)
        self.b2.configure(state=DISABLED)
        self.b3.configure(state=DISABLED)
        self.b4.configure(state=DISABLED)
        self.b5.configure(state=DISABLED)
        self.b6.configure(state=DISABLED)
        self.b7.configure(state=DISABLED)
        self.b8.configure(state=DISABLED)
        self.b9.configure(state=DISABLED)

    def _enable_all_button(self):
        self.b1.configure(state=ACTIVE)
        self.b2.configure(state=ACTIVE)
        self.b3.configure(state=ACTIVE)
        self.b4.configure(state=ACTIVE)
        self.b5.configure(state=ACTIVE)
        self.b6.configure(state=ACTIVE)
        self.b7.configure(state=ACTIVE)
        self.b8.configure(state=ACTIVE)
        self.b9.configure(state=ACTIVE)

    def _start_Game_(self):
        if len(self.player2_name.get()) != 0:
            self.Start.grid_remove()
            self.t2.grid_remove()
            self.frame.geometry('400x422')
            self._enable_all_button()
            self.l2.configure(text=self.player2_name.get())
            self.l2.grid(column=0, row=2, columnspan=5)
        else:
            messagebox.showerror(title='error',message='Invalid Name')

    def _restart_(self):
        self.frame.destroy()
        os.system('python Tic_Tac_With_Computer.py')

    def _click_on_button_(self, button):
        self.buttonClicks = self.buttonClicks + 1
        button.configure(text='X', state=DISABLED)
        if self._isWin_():
            return
        flag = False
        if self.buttonClicks != 9:
            self.buttonClicks = self.buttonClicks + 1
            temp = self._generate_random_()
            temp.configure(text='O', state=DISABLED)
            flag = self._isWin_()
        if self.buttonClicks == 9 and flag == False:
            if messagebox.askyesno(title='Result', message='The Match is Tie\n Do you want play again?'):
                self._restart_()
            else:
                self.frame.destroy()

    def _generate_random_(self):
        i = random.Random().randint(1, 9)
        btn = self._isValid_(i)
        while btn == None:
            i = random.Random().randint(1, 9)
            btn = self._isValid_(i)
        return btn

    def _isValid_(self,index):
        if index == 1:
            if self.b1['text'] == ' ':
                return self.b1
            return None
        elif index == 2:
            if self.b2['text'] == ' ':
                return self.b2
            return None
        elif index == 3:
            if self.b3['text'] == ' ':
                return self.b3
            return None
        elif index == 4:
            if self.b4['text'] == ' ':
                return self.b4
            return None
        elif index == 5:
            if self.b5['text'] == ' ':
                return self.b5
            return None
        elif index == 6:
            if self.b6['text'] == ' ':
                return self.b6
            return None
        elif index == 7:
            if self.b7['text'] == ' ':
                return self.b7
            return None
        elif index == 8:
            if self.b8['text'] == ' ':
                return self.b8
            return None
        elif index == 9:
            if self.b9['text'] == ' ':
                return self.b9
            return None
game = Tic_Tac_Game()
