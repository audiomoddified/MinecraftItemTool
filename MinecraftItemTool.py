import tkinter
import UserNameLoad
import ItemFileLoad
import MinecraftScreenSelector
import logging


class MinecraftItemTool:

    def __init__(self):
        window = tkinter.Tk()
        window.title("Minecraft Item Tool")

        self.user_name_load = UserNameLoad.UserNameLoad(0)
        self.item_file_load = ItemFileLoad.ItemFileLoad(1)
        self.minecraft_screen_selector = MinecraftScreenSelector.MinecraftScreenSelector(2, window)

        window.mainloop()


if __name__ == '__main__':
    mainClass = MinecraftItemTool()