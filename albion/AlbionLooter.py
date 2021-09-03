from tkinter.constants import END
import tkinter as tk
import tkinter.font as tkFont
import threading
from time import sleep
import keyboard
from looterFunctions import BODY_COORD_X, BODY_COORD_Y, clearInventory, runLooter

### CONST ###
HOTKEY_LOOT = "-"
HOTKEY_INV  = "+"
DEBUG       = True
INVENTORY   = [{'x': 1590, 'y': 550, 'isFilled': False}, {'x': 1670, 'y': 550, 'isFilled': False}, {'x': 1750, 'y': 550, 'isFilled': False}, {'x': 1830, 'y': 550, 'isFilled': False}, {'x': 1590, 'y': 630, 'isFilled': False}, {'x': 1670, 'y': 630, 'isFilled': False}, {'x': 1750, 'y': 630, 'isFilled': False}, {'x': 1830, 'y': 630, 'isFilled': False}, {'x': 1590, 'y': 710, 'isFilled': False}, {'x': 1670, 'y': 710, 'isFilled': False}, {'x': 1750, 'y': 710, 'isFilled': False}, {'x': 1830, 'y': 710, 'isFilled': False}, {'x': 1590, 'y': 790, 'isFilled': False}, {'x': 1670, 'y': 790, 'isFilled': False}, {'x': 1751, 'y': 790, 'isFilled': False}, {'x': 1830, 'y': 790, 'isFilled': False}, {'x': 1590, 'y': 870, 'isFilled': False}, {'x': 1670, 'y': 870, 'isFilled': False}, {'x': 1750, 'y': 870, 'isFilled': False}, {'x': 1830, 'y': 870, 'isFilled': False}, {'x': 1590, 'y': 580, 'isFilled': False}, {'x': 1670, 'y': 580, 'isFilled': False}, {'x': 1750, 'y': 580, 'isFilled': False}, {'x': 1830, 'y': 580, 'isFilled': False}, {'x': 1590, 'y': 660, 'isFilled': False}, {'x': 1670, 'y': 660, 'isFilled': False}, {'x': 1750, 'y': 660, 'isFilled': False}, {'x': 1830, 'y': 660, 'isFilled': False}, {'x': 1590, 'y': 740, 'isFilled': False}, {'x': 1670, 'y': 740, 'isFilled': False}, {'x': 1750, 'y': 740, 'isFilled': False}, {'x': 1830, 'y': 740, 'isFilled': False}, {'x': 1590, 'y': 820, 'isFilled': False}, {'x': 1670, 'y': 820, 'isFilled': False}, {'x': 1750, 'y': 820, 'isFilled': False}, {'x': 1830, 'y': 820, 'isFilled': False}, {'x': 1590, 'y': 900, 'isFilled': False}, {'x': 1670, 'y': 900, 'isFilled': False}, {'x': 1750, 'y': 900, 'isFilled': False}, {'x': 1830, 'y': 900, 'isFilled': False}, {'x': 1590, 'y': 820, 'isFilled': False}, {'x': 1670, 'y': 820, 'isFilled': False}, {'x': 1750, 'y': 820, 'isFilled': False}, {'x': 1830, 'y': 820, 'isFilled': False}, {'x': 1590, 'y': 900, 'isFilled': False}, {'x': 1670, 'y': 900, 'isFilled': False}, {'x': 1750, 'y': 900, 'isFilled': False}, {'x': 1830, 'y': 900, 'isFilled': False}]
## Avisar de vaciar el inventario con pop-up de tkinter ##
## CONST ##

class App:
    
    entryLootKey = ""
    entryInvKey = ""
    successMsg = ""
        
    def __init__(self, root):
        root.title("AlbionLooter v0.1")
        width=500
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        contentTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        contentTitle["font"] = ft
        contentTitle["fg"] = "#333333"
        contentTitle["justify"] = "center"
        contentTitle["text"] = "AlbionLooter v0.1"
        contentTitle.place(x=0,y=20,width=498,height=48)

        hotkeyTextarea=tk.Entry(root)
        hotkeyTextarea["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        hotkeyTextarea["font"] = ft
        hotkeyTextarea["fg"] = "#333333"
        hotkeyTextarea["justify"] = "center"
        hotkeyTextarea["text"] = ""
        hotkeyTextarea.place(x=210,y=150,width=150,height=30)
        self.entryLootKey =  hotkeyTextarea

        setAutolootButton=tk.Button(root)
        setAutolootButton["bg"] = "#4b0082"
        setAutolootButton["cursor"] = "cross"
        ft = tkFont.Font(family='Times',size=10)
        setAutolootButton["font"] = ft
        setAutolootButton["fg"] = "#ffffff"
        setAutolootButton["justify"] = "center"
        setAutolootButton["text"] = "Set Key"
        setAutolootButton.place(x=400,y=150,width=65,height=30)
        setAutolootButton["command"] = self.setAutolootButton_command
        
        bindingDescriptionTextbox=tk.Message(root)
        bindingDescriptionTextbox["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=10)
        bindingDescriptionTextbox["font"] = ft
        bindingDescriptionTextbox["fg"] = "#333333"
        bindingDescriptionTextbox["justify"] = "center"
        bindingDescriptionTextbox["text"] = "Enter the desidered key binding for autoloot"
        bindingDescriptionTextbox.place(x=60,y=130,width=120,height=63)
        
        successMessage=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        successMessage["font"] = ft
        successMessage["fg"] = "#4BB543"
        successMessage["justify"] = "center"
        successMessage["text"] = "Key binding set! Happy Looting :)"
        successMessage.place(x=50,y=420,width=400,height=130)
        successMessage.pack()
        successMessage.pack_forget()
        self.successMsg = successMessage
        
        setInventoryButton=tk.Button(root)
        setInventoryButton["bg"] = "#4b0082"
        setInventoryButton["cursor"] = "cross"
        ft = tkFont.Font(family='Times',size=10)
        setInventoryButton["font"] = ft
        setInventoryButton["fg"] = "#ffffff"
        setInventoryButton["justify"] = "center"
        setInventoryButton["text"] = "Reset Inventory"
        setInventoryButton.place(x=380,y=210,width=105,height=30)
        setInventoryButton["command"] = self.setInventoryButton_command

        inventoryTextbox=tk.Entry(root)
        inventoryTextbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        inventoryTextbox["font"] = ft
        inventoryTextbox["fg"] = "#333333"
        inventoryTextbox["justify"] = "center"
        inventoryTextbox["text"] = ""
        inventoryTextbox.place(x=210,y=210,width=150,height=30)
        self.entryInvKey = inventoryTextbox
        
        inventoryDescription=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        inventoryDescription["font"] = ft
        inventoryDescription["fg"] = "#333333"
        inventoryDescription["justify"] = "center"
        inventoryDescription["text"] = "Cleared Inventory HOTKEY"
        inventoryDescription.place(x=60,y=200,width=129,height=44)

    def setInventoryButton_command(self):
        global HOTKEY_INV
        HOTKEY_INV = self.entryInvKey.get()
        self.entryInvKey.delete(0, END)
        t = threading.Thread(target=self.showSuccess)
        t.start()
        if DEBUG:
            print(HOTKEY_INV)

    def setAutolootButton_command(self):
        global HOTKEY_LOOT
        HOTKEY_LOOT = self.entryLootKey.get()
        self.entryLootKey.delete(0, END)
        t = threading.Thread(target=self.showSuccess)
        t.start()
        if DEBUG:
            print(HOTKEY_LOOT)
    
    def showSuccess(self):
        self.successMsg.pack_forget()
        self.successMsg.pack(pady=420)
        sleep(3)
        self.successMsg.pack()
        self.successMsg.pack_forget()
        
################## CLASS APP END ##################


def startKeyboardListener(root):
    if DEBUG:
        print("Keyboard listener started!")

    global HOTKEY_INV
    global HOTKEY_LOOT
    global INVENTORY
    
    #try:
    while root.state() == "normal":
        if(keyboard.is_pressed(HOTKEY_LOOT)):
            print("pressed: " + HOTKEY_LOOT)
            INVENTORY = runLooter(INVENTORY, 0, BODY_COORD_X, BODY_COORD_Y)
        elif(keyboard.is_pressed(HOTKEY_INV)):
            print("pressed: " + HOTKEY_INV)
            clearInventory(INVENTORY)
    #except:
    if DEBUG:
        print("KeyboardListener Exited")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    keyboardListener = threading.Thread(target=startKeyboardListener, args=(root,))
    keyboardListener.start()
    guiloop = threading.Thread(target=root.mainloop())
    guiloop.start()