from abc import ABC, abstractmethod
from tkinter import *


class root(Tk, ABC):
    def __init__(self):
        super().__init__()
        self.title('Number Pad')
        self.geometry('250x300')
        self.nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]
        self.build_ui()

    @abstractmethod
    def configure_grid(self):
        """Set up the grid sizes and weights."""

    @abstractmethod
    def create_buttons(self):
        """Create clickable labels for each number."""

    def build_ui(self):
        self.configure_grid()
        self.create_buttons()


class NumberPad(root):
    def configure_grid(self):
        for i in range(4):
            self.columnconfigure(i, weight=1, minsize=75)
            self.rowconfigure(i, weight=1, minsize=50)

    def create_buttons(self):
        for i in range(4):
            for j in range(3):
                frame = Frame(master=self, relief=SUNKEN, borderwidth=1)
                frame.grid(row=i, column=j, sticky='nsew')
                label = Label(master=frame, text=self.nums[i][j], bg='#d0efff', padx=10, pady=10)
                label.pack(expand=True, fill='both')


if __name__ == '__main__':
    app = NumberPad()
    app.mainloop()