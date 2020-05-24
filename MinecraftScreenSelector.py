from tkinter import Label, OptionMenu, Button, E, W, StringVar
import logging


class MinecraftScreenSelector:

    def __init__(self, row_number, root):
        Label(text="Minecraft Screen").grid(row=row_number, column=0, sticky=E)

        self.selected_option = StringVar()
        self.choices = {'This One', 'That One'}
        self.selected_option.set(next(iter(self.choices)))
        self.optionMenu = OptionMenu(root, self.selected_option, *self.choices)
        self.optionMenu.grid(row=row_number, column=1, sticky=E + W)

        Button(text="Search For Windows", command = lambda: self.search_for_windows())\
            .grid(row=row_number, column=2, padx=5, ipadx=5, sticky = W, columnspan = 2)

    def search_for_windows(self):
        logging.info("Searching for windows")