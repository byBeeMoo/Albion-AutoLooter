from os import write
import pyautogui as py
import time

def generateInventory():
    AVG_PX_DISTANCE_BLOCKS = 80
    INVERTORY_COORD_X = 1590
    INVERTORY_COORD_Y = 550

    inventory = []
    inventoryX = INVERTORY_COORD_X
    inventoryY = INVERTORY_COORD_Y
    py.click(inventoryX - 40, inventoryY - 90)
    try:
        for i in range(1, 13):
            if i > 1:
                inventoryY += AVG_PX_DISTANCE_BLOCKS
                
            if i == 6 or i == 11:
                py.scroll(-1)
                time.sleep(0.2)
                inventoryX = INVERTORY_COORD_X
                if i != 11:
                    inventoryY = INVERTORY_COORD_Y + 30
                else:
                    inventoryY= INVERTORY_COORD_Y + 270
            py.moveTo(inventoryX, inventoryY)
            pos = py.position()
            inventory.append({'x':pos[0],'y':pos[1],'isFilled':False})
            
            for j in range(1,4):
                inventoryX += AVG_PX_DISTANCE_BLOCKS        
                py.moveTo(inventoryX, inventoryY)
                pos = py.position()
                inventory.append({'x':pos[0],'y':pos[1],'isFilled':False}) 
                if j == 3:
                    inventoryX = INVERTORY_COORD_X
        py.scroll(1)
        py.scroll(1)
        time.sleep(0.2)     
    except:
        pass
    return inventory