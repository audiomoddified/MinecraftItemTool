from tkinter import Label, Entry, Button, E, W, filedialog


class ItemFileLoad():
    def __init__(self, row_number):
        Label(text = "Item File").grid(row=row_number, column=0, sticky=E)

        self.file_selected = None

        self.entry = Entry()
        self.entry.grid(row=row_number, column=1, sticky=E+W)

        Button(text ="...", command=lambda: self.open_file()).grid(row=row_number, column=2, padx=5, ipadx=5, sticky=W)

        Button(text="Load Items").grid(row=row_number, column=3, padx=5, ipadx=4, sticky=E+W)

    def open_file(self):
        self.file_selected = filedialog.askopenfile()
        self.entry.delete(0)
        self.entry.insert(0, self.file_selected.name)
