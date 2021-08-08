from tkinter import Tk, Label, Entry, Button, StringVar, DISABLED, ACTIVE, messagebox
import os


class Tic_Tac_Game:
    def __init__(self):
        self.Turn = True
        self.buttonClicks = 0
        self.frame = Tk()
        self.frame.geometry('400x430')
        self.frame.title('Tic Tac Game')
        self.frame.configure(bg='Gray')
        self.l1 = Label(text="Player 1:  ", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        self.l1.grid(column=0, row=0)
        self.l2 = Label(text="Player 2:  ", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        self.l2.grid(column=0, row=1)

        self.player1_name = StringVar()
        self.player2_name = StringVar()
        self.commandButton = StringVar(value='')

        self.t1 = Entry(self.frame, textvariable=self.player1_name, bd=10, width=25)
        self.t1.grid(column=0, row=0, columnspan=8)
        self.t2 = Entry(self.frame, textvariable=self.player2_name, bd=10, width=25)
        self.t2.grid(column=0, row=1, columnspan=8)

        self.workingbutton = Button(textvariable=self.commandButton, font='Times 10 bold', width=12, height=1,
                                    borderwidth=10, state=DISABLED, command=self._restart_)
        self.workingbutton.grid(column=2, row=0)
        self.Save = Button(text='Save', font='Times 10 bold', width=12, height=1, borderwidth=10,
                           command=self.Save_names_of_player)
        self.Save.grid(column=2, row=1)

        self.b1 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b1))
        self.b1.grid(column=0, row=4)
        self.b2 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b2))
        self.b2.grid(column=1, row=4)
        self.b3 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b3))
        self.b3.grid(column=2, row=4)
        self.b4 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b4))
        self.b4.grid(column=0, row=5)
        self.b5 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b5))
        self.b5.grid(column=1, row=5)
        self.b6 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b6))
        self.b6.grid(column=2, row=5)
        self.b7 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b7))
        self.b7.grid(column=0, row=6)
        self.b8 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b8))
        self.b8.grid(column=1, row=6)
        self.b9 = Button(text=' ', width=18, height=7, font='Times 10 bold',
                         command=lambda: self._click_on_button_(self.b9))
        self.b9.grid(column=2, row=6)
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
            messagebox.showinfo(title='Result', message=(self.player1_name.get() + ' won the match'))
            self.commandButton.set(value='Restart')
        elif (self.b1['text'] == 'O' and self.b2['text'] == 'O' and self.b3['text'] == 'O' or
              self.b4['text'] == 'O' and self.b5['text'] == 'O' and self.b6['text'] == 'O' or
              self.b7['text'] == 'O' and self.b8['text'] == 'O' and self.b9['text'] == 'O' or
              self.b1['text'] == 'O' and self.b4['text'] == 'O' and self.b7['text'] == 'O' or
              self.b2['text'] == 'O' and self.b5['text'] == 'O' and self.b8['text'] == 'O' or
              self.b3['text'] == 'O' and self.b6['text'] == 'O' and self.b9['text'] == 'O' or
              self.b1['text'] == 'O' and self.b5['text'] == 'O' and self.b9['text'] == 'O' or
              self.b3['text'] == 'O' and self.b5['text'] == 'O' and self.b7['text'] == 'O'):
            self._disable_all_button()
            messagebox.showinfo(title='Result', message=(self.player2_name.get() + ' won the match'))
            self.commandButton.set(value='Restart')
        elif self.buttonClicks == 9:
            messagebox.showinfo(title='Result', message='The Match is Tie')
            self.commandButton.set(value='Restart')

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

    def Save_names_of_player(self):
        self.t1.configure(state=DISABLED)
        self.t2.configure(state=DISABLED)
        self.Save.configure(state=DISABLED)
        self._enable_all_button()
        self.player1_name.set(value=self.player1_name.get() + " X ")
        self.player2_name.set(value=self.player2_name.get() + " O ")
        self.commandButton.set(value=self.player1_name.get())
        self.workingbutton.configure(state=ACTIVE)

    def _restart_(self):
        if self.commandButton.get() == 'Restart':
            self.frame.destroy()
            os.system('python Tic_Tac_Game_with_Two_Players.py')

    def _click_on_button_(self, button):
        if self.Turn and self.commandButton.get() == self.player1_name.get():
            self.buttonClicks = self.buttonClicks + 1
            self.Turn = not self.Turn
            button.configure(text='X')
            self.commandButton.set(value=self.player2_name.get())
            self.workingbutton.configure(state=ACTIVE)
            self._isWin_()
        elif not self.Turn and self.commandButton.get() == self.player2_name.get():
            self.buttonClicks = self.buttonClicks + 1
            self.Turn = not self.Turn
            button.configure(text='O')
            self.commandButton.set(value=self.player1_name.get())
            self.workingbutton.configure(state=ACTIVE)
            self._isWin_()


game = Tic_Tac_Game()
