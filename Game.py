from tkinter import*
import random

GRID_SIZE = 15
SQUARE_SIZE = 50
MINES_NUM = 100

root = Tk()
root.title("Pythonicway Minesweep")
c= Canvas(root, width=GRID_SIZE *SQUARE_SIZE, height=GRID_SIZE *SQUARE_SIZE)
c.pack()
 #(Малює решітку на ігровому полі)

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
                           i *SQUARE_SIZE + SQUARE_SIZE,
                           j*SQUARE_SIZE + SQUARE_SIZE, fill='gray')
 # Запускаємо програму
mines = set(random.sample(range(1,GRID_SIZE**2+1 ), MINES_NUM)) # Генеруємо міни
clicked = set() # Сет для клітинок, по яким клікнути
#Функція реагування на клік
def click(event):
    ids = c.find_withtag(CURRENT)[0]
    if ids in mines:
        c.itemconfig(CURRENT, fill="red")
    elif ids not in clicked:
        c.itemconfig(CURRENT, fill="green")
    c.update()
    # Функція для помітки мін
def mark_mine(evenr):
    ids= c.find_withtag(CURRENT)[0]
       #Якщо не кликати по клытинці - красим її в жовтий колір, або в сірий
    if ids not in clicked:
        clicked.add(ids)
        x1, y1, x2, y2= c.coords(ids)
        c.itemconfig(CURRENT, fill="yellow")
    else:
        clicked.remove(ids)
        c.itemconfig(CURRENT, fill="gray")

c.bind("<Button-1>", click)
c.bind("<Button-3>", mark_mine)

def generate_neighbors(square):
    """" повертає клітини, сусідні із     square """
    #Ліва верхня клітинка
    if square ==1:
        data = {GRID_SIZE + 1, 2, GRID_SIZE +2}
    #Права нижня
    elif square ==GRID_SIZE**2:
        data = {square - GRID_SIZE, square -1, square - GRID_SIZE -1}
    #Ліва нижня
    elif square == GRID_SIZE:
        data= {square -1, GRID_SIZE *2, GRID_SIZE *2 - 1}
    #Верхня права
    elif squeare == GRID_SIZE** 2 - GRID_SIZE +1:
        data = {square +1, square - GRID_SIZE, square - GRID_SIZE +1}
    #Клытка в лывому ряду
    elif square< GRID_SIZE:
        data = {square +1, square - 1,square +GRID_SIZE,
                square +GRID_SIZE -1, square + GRID_SIZE +1}
    #Клытка в нижньому ряд
    elif square % GRID_SIZE ==0:
        data= {square + GRID_SIZE, square - GRID_SIZE, square -1,
               square + GRID_SIZE - 1, square - GRID_SIZE -1}
    #Клытинка в верхньому ряду
    elif square % GRID_SIZE ==1:
        data = {square +GRID_SIZE, square -GRID_SIZE, square +1,
                square + GRID_SIZE +1, square - GRID_SIZE +1}
    #Люба ынша клытинка
    else:
        data = {square -1, square +1, square -GRID_SIZE, square + GRID_SIZE,
                square - GRID_SIZE -1, square - GRID_SIZE + 1,
                square + GRID_SIZE + 1, square + GRID_SIZE -1}
    return data
def check_mines(neighbors):
    return len(mines.intersection(neighbors))
def clearance(ids):
    #Ljlj'vj rksnbyre gj zrsq rksryenb e cgbcje
    clicked.add(ids)
    #Отримали список сусідніх клітин
    neighbors = generate_neighbors(ids)
    #Кількість мін у сусідніх клітинках
    around = check_mines(neighbors)
    #Якщо мыни еавколо клытини э
    if around:
        x1, y1, x2, y2 = c.coords(ids)
        c.itemconfig(ids, fill="green")
        c.create_text(x1 + SQUARE_SIZE /2,
                      y1 + SQUARE_SIZE /2,
                      text = str(around), fond="Ariall{}".format(int(SQUARE_SIZE /2)), fill = "yellow")
    else:
        for item in set(neighbors).difference(clicked):
            c.itemconfig(item, fill="green")
            clearance(item)
import sys
sys.setrecursionlimit(5000)
root.mainloop()
