from tkinter import *
import bib_saves as sv
from random import randint
import winsound
sv.load("FlowerClicker", "save_2.0")



# Variavéis / Constantes =============
SCREEN_X = 1280
SCREEN_Y = 920
Font = ("Terminal", 20, "bold")
ColorButton = "#0044FF"
leafs = []
# Configs da janela =====
Window = Tk()
Window.geometry(f"{SCREEN_X}x{SCREEN_Y}")
Window.resizable(False, False)
Window.config(bg="#1FAFDB")
Window.title("FlowerCliker")
c = Canvas(Window, bg= "#1FAFDB", width= SCREEN_X, height=SCREEN_Y)
c.pack()


# Flowers IMAGES ===================
FlowerIMAGE_1 = PhotoImage(file="Flower_1.png")
FlowerIMAGE_2 = PhotoImage(file="Flower_2.png")
FlowerIMAGE_3 = PhotoImage(file="Flower_3.png")
FlowerIMAGE_4 = PhotoImage(file="Flower_4.png")
FlowerIMAGE_5 = PhotoImage(file="Flower_5.png")
FlowerIMAGE_6 = PhotoImage(file="Flower_6.png")
FlowerIMAGE_7 = PhotoImage(file="Flower_7.png")
FlowerIMAGE_8 = PhotoImage(file="Flower_8.png")
FlowerIMAGE_9 = PhotoImage(file="Flower_9.png")
FlowerIMAGE_10 = PhotoImage(file="Flower_10.png")
FlowerIMAGE_11 = PhotoImage(file="Flower_11.png")
FlowerIMAGE_12 = PhotoImage(file="Flower_12.png")

TreeIMAGE_1 = PhotoImage(file="Tree_1.png")
TreeIMAGE_2 = PhotoImage(file="Tree_2.png")
TreeIMAGE_3 = PhotoImage(file="Tree_3.png")

FlowerIMAGE_143 = PhotoImage(file="Flower_143.png")
Shop_markerIMAGE = PhotoImage(file="Shop_marker.png")
falling_starIMAGE = PhotoImage(file="falling_star.png")
Flower = c.create_image(SCREEN_X / 2, SCREEN_Y / 2 + 180, image= FlowerIMAGE_1)

# DEFS ================================================================================
#======================================== COISAS DA TELA
def refresh_screen_itens():
    # LEVEL UP BUTTON ======================================
    if sv.saves["points"] < sv.saves["price_level_up"]:
        level_up_button.config(state="disabled")
    else:
        level_up_button.config(state="normal")
    if sv.saves["points"] < sv.saves["price_level_up_2"]:
        level_up_2_button.config(state="disabled")
    else:
        level_up_2_button.config(state="normal")

    # REBIRTH 1 BUTTON ======================================
    if sv.saves["rebirth"] == 0:
        if sv.saves["points"] < 20000 or sv.saves["Level"] < 250:
            points_per_click_button.config(state="disabled")
        else:
            points_per_click_button.config(state="normal")
    elif sv.saves["rebirth"] >= 1:
        if sv.saves["points"] >= sv.saves["price_add_points_per_click"]:
            points_per_click_button.config(state="normal")
        else:
            points_per_click_button.config(state="disabled")
        points_per_click_button.config(text="MORE POINTS\nPER CLICK", command= level_up_points_per_click)
    # REBIRTH 2 BUTTON ======================================
    if sv.saves["rebirth"] == 1:
        if sv.saves["points"] < 20000 or sv.saves["Level"] < 250:
            points_per_leaf_button.config(state="disabled")
        else:
            points_per_leaf_button.config(state="normal")
    
    elif sv.saves["rebirth"] >= 2:
        if sv.saves["points"] >= sv.saves["price_add_points_per_leaf"]:
            points_per_leaf_button.config(state="normal")
        else:
            points_per_leaf_button.config(state="disabled")
        points_per_leaf_button.config(text="MORE POINTS\nPER LEAF", command= level_up_points_per_leaf)
    else: 
        points_per_leaf_button.config(state="disabled")
    # TEXTS ======================================
    c.itemconfig(level_text, text= f"Level: {sv.saves["Level"]}")
    c.itemconfig(points_text, text= f"Points: {sv.saves["points"]:.1f}")


    # BACKGROUND COLORS ======================================
    if sv.saves["Level"] == 143:
        Window.config(bg="#C438B1")
        c.config(bg="#C438B1")
    elif sv.saves["rebirth"] == 2:
        Window.config(bg="#FFBBF0")
        c.config(bg="#FFBBF0")
    elif sv.saves["rebirth"] == 1:
        Window.config(bg="#20299B")
        c.config(bg="#20299B")
    elif sv.saves["rebirth"] == 0:
        Window.config(bg="#1FAFDB")
        c.config(bg="#1FAFDB")

    Update_flower()

def Update_flower():
    global Flower
    if sv.saves["Level"] == 143:
        image= FlowerIMAGE_143
    elif sv.saves["Level"] < 5:
        image= FlowerIMAGE_1
    elif sv.saves["Level"]  < 15:
        image= FlowerIMAGE_2
    elif sv.saves["Level"] < 30:
        image= FlowerIMAGE_3
    elif sv.saves["Level"] < 50:
        image= FlowerIMAGE_4
    elif sv.saves["Level"] < 75:
        image= FlowerIMAGE_5
    elif sv.saves["Level"] < 100:
        image= FlowerIMAGE_6
    elif sv.saves["Level"] < 125:
        image= FlowerIMAGE_7
    elif sv.saves["Level"] < 150:
        image= FlowerIMAGE_8
    elif sv.saves["Level"] < 175:
        image= FlowerIMAGE_9
    elif sv.saves["Level"] < 200:
        image= FlowerIMAGE_10
    elif sv.saves["Level"] < 225:
        image= FlowerIMAGE_11
    elif sv.saves["Level"] < 250:
        image= FlowerIMAGE_12
    elif sv.saves["rebirth"] == 0:
        image= TreeIMAGE_1
    elif sv.saves["rebirth"] == 1:
        image= TreeIMAGE_2
    elif sv.saves["rebirth"] == 2:
        image= TreeIMAGE_3
    if c.coords(Flower)[1] > 615.0 and sv.saves["Level"] >= 250: # Muda o Y se ele for menor que 585, pois tem margem de erro de alguns pixeis.
            c.move(Flower, 0, -70)
    elif c.coords(Flower)[1] < 615.0 and sv.saves["Level"] < 250:
            c.move(Flower, 0, +70)
    c.itemconfig(Flower, image= image)

def create_screen_itens():
    global level_up_button, level_up_2_button, level_text, points_text, points_per_click_button, points_per_leaf_button
    # Criação dos butões ============================================================================================================
    level_up_button = Button(Window, command= level_up,
                            text= "LEVEL UP", font= Font, width= 14, height= 2, pady= -2, # Pady para balancear o tamanho
                            bg= ColorButton, activebackground= ColorButton)
    level_up_button.place(x= (SCREEN_X / 2) + 350, y= (SCREEN_Y / 2) - 458) # 65 pixeis Y + 2 de espaçamento

    level_up_2_button = Button(Window, command= level_up_2,
                            text= "MORE\nPOINTS UPD", font= Font, width= 14, height= 2,
                            bg= ColorButton, activebackground= ColorButton)
    level_up_2_button.place(x= (SCREEN_X / 2) + 350, y= (SCREEN_Y / 2) - 393)

    points_per_click_button = Button(Window, command= rebirth_1,
                            text= "REBIRTH 1", font= Font, width= 14, height= 2,
                            bg= ColorButton, activebackground= ColorButton)
    points_per_click_button.place(x= (SCREEN_X / 2) + 350, y= (SCREEN_Y / 2) - 326)
    points_per_leaf_button = Button(Window, command= rebirth_2,
                            text= "REBIRTH 2", font= Font, width= 14, height= 2,
                            bg= ColorButton, activebackground= ColorButton)
    points_per_leaf_button.place(x= (SCREEN_X / 2) + 350, y= (SCREEN_Y / 2) - 259) 
    # Criação dos labels ============================================================================================================
    level_text = c.create_text(20, 20, text=f"Level: {sv.saves["Level"]}",
                               font= (Font[0], Font[1] + 4), anchor= "nw")
    points_text = c.create_text(20, 55, text=f"Points: {sv.saves["points"]:.1f}",
                                font= (Font[0], Font[1] + 4), anchor= "nw")
    refresh_screen_itens()
    # Criação de itens ==============================================================================================================
    c.create_rectangle((SCREEN_X / 2) + 347, 0, 1253, (SCREEN_Y / 2) - 192, fill="Black")
    c.create_image((SCREEN_X / 2) + 485, (SCREEN_Y / 2) - 210, image= Shop_markerIMAGE)

def create_get_points_text(type):
    # Cria o texto dos pontos e agenda o desaparecimento
    get_points_text_areaX = randint(int((SCREEN_X / 2)) - 60, int((SCREEN_X / 2) + 60))
    get_points_text_areaY = (randint(int((SCREEN_Y / 2)) - 5, int((SCREEN_Y / 2) + 5))) - (120 if sv.saves["Level"] <= 175 else  260)
    get_points_text = c.create_text(get_points_text_areaX, get_points_text_areaY,
                                    text= f"+ {sv.saves[type]}", font= Font)

    t = Window.after(750, lambda: c.delete(get_points_text))

def create_falling_star():
    # Cria a estrela cadente e agenda o desaparecimento
    falling_star_areaX = randint(0, SCREEN_X)
    falling_star_areaY = randint(0, int(SCREEN_Y / 2))
    falling_star = c.create_image(falling_star_areaX, falling_star_areaY, image= falling_starIMAGE)
    c.tag_lower(falling_star) # Coloca a estrela atrás de tudo
    def move_star():
        try:
            c.move(falling_star, -10, 10)
            Window.after(50, move_star)
        except NameError:
            pass
    move_star()
    Window.after(1000, lambda: c.delete(falling_star))
    Window.after(2000, create_falling_star)

def create_leafs():
    # Cria as folhas caindo e agenda o desaparecimento
    leaf_areaX = randint(int(SCREEN_X / 2) - 120, int(SCREEN_X / 2) + 120)
    leaf_areaY = randint(int(SCREEN_Y / 2) + 100, SCREEN_Y - 100)
    leaf = c.create_rectangle(leaf_areaX, leaf_areaY, leaf_areaX + 20, leaf_areaY + 10, fill="#228B22", outline="")
    leafs.append(leaf)
    def move_leaf():
        try:
            if c.coords(leaf)[1] < SCREEN_Y - 15:
                c.move(leaf, 0, 10)
                Window.after(100, move_leaf)
        except (NameError, ValueError, IndexError):
            pass
    move_leaf()

    Window.after(8000, lambda: c.delete(leaf) if leaf in c.find_all() else None)
    Window.after(8000, lambda: leafs.remove(leaf) if leaf in leafs else None)
    Window.after(2000, create_leafs)

#======================================== COMEÇAR AS FUNÇÕES BASICAS
def start_music():
    winsound.PlaySound("FlowerClicker_background_music.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

def Start():
    if sv.FirstTime:
        reset()
    Update_flower()
    create_screen_itens()
    start_music()
    auto_save()
    create_falling_star()
    if sv.saves["rebirth"] >= 2:
        create_leafs()

def get_points(event=None):
    global points, t
    refresh_screen_itens()
    sv.saves["points"] += sv.saves["add_points"]

    # Adiciona movimento á flor
    c.move(Flower, 0, + 5)
    Window.after(200, lambda: c.move(Flower, 0, -5))

    create_get_points_text("add_points")

def get_points_per_click(event=None):
    global points, t
    if sv.saves["rebirth"] >= 1:
        refresh_screen_itens()
        sv.saves["points"] += sv.saves["add_points_per_click"]

        # Adiciona movimento á flor
        c.move(Flower, 0, + 5)
        Window.after(200, lambda: c.move(Flower, 0, -5))

        create_get_points_text("add_points_per_click")

def catch_leaf(event=None):
    if sv.saves["rebirth"] >= 2:
        if (int(SCREEN_X / 2) - 120 <= event.x <= int(SCREEN_X / 2) + 120) and  (event.y >= int(SCREEN_Y / 2) + 100):
            
            for leaf in leafs:
                try:
                    leafs.remove(leaf)
                    c.delete(leaf)
                    sv.saves["points"] += sv.saves["add_points_per_leaf"]
                    create_get_points_text("add_points_per_leaf")
                    refresh_screen_itens()
                except ValueError:
                    pass
            

def reset():
    sv.save("points", 0)
    sv.save("add_points", 1)
    sv.save("Level", 1)
    sv.save("price_level_up", sv.saves["Level"] ** 1.50)
    sv.save("price_level_up_2", sv.saves["add_points"] ** 2.125)
    sv.save("add_points_per_click", 1)
    sv.save("price_add_points_per_click", sv.saves["add_points_per_click"] ** 5.125)
    sv.save("rebirth", 0)
    sv.save("add_points_per_leaf", 50)
    sv.save("price_add_points_per_leaf", sv.saves["add_points_per_leaf"] ** 1.25)
#======================================== SALVAR / SAIR
def quit(event=None):
    sv.save_all()
    Window.destroy()

def auto_save():
    sv.save_all()
    print("Salvo")
    Window.after(30000, auto_save)
  
#======================================== MELHORIAS
def level_up():
    if sv.saves["points"] >= sv.saves["price_level_up"]:
        sv.saves["points"] -= sv.saves["price_level_up"]
        sv.saves["Level"] += 1
        sv.saves["price_level_up"] = sv.saves["Level"] ** 1.50
        refresh_screen_itens()
    
def level_up_2():
    if sv.saves["points"] >= sv.saves["price_level_up_2"]:
        sv.saves["points"] -= sv.saves["price_level_up_2"]
        sv.saves["add_points"] += 1
        sv.saves["price_level_up_2"] = sv.saves["add_points"] ** 2.125
        refresh_screen_itens()
        Update_flower()
    else:
        level_up_2_button.config(state="disabled")

def rebirth_1():
    if sv.saves["Level"] >= 250 and sv.saves["points"] >= 50000:
        reset()
        sv.save("rebirth", 1)
        refresh_screen_itens()

def rebirth_2():
    if sv.saves["Level"] >= 250 and sv.saves["points"] >= 50000 and sv.saves["rebirth"] == 1:
        reset()
        sv.save("rebirth", 2)
        create_leafs()
        refresh_screen_itens()

def level_up_points_per_click():
    if sv.saves["points"] >= sv.saves["price_add_points_per_click"]:
        sv.saves["points"] -= sv.saves["price_add_points_per_click"]
        sv.saves["add_points_per_click"] += 1
        sv.saves["price_add_points_per_click"] = sv.saves["add_points_per_click"] ** 5.125
        refresh_screen_itens()

def level_up_points_per_leaf():
    if sv.saves["points"] >= sv.saves["price_add_points_per_leaf"]:
        sv.saves["points"] -= sv.saves["price_add_points_per_leaf"]
        sv.saves["add_points_per_leaf"] += 2
        sv.saves["price_add_points_per_leaf"] = sv.saves["add_points_per_leaf"] ** 1.25
        refresh_screen_itens()
# Main Loop =====================
Window.bind("<KeyRelease-space>", get_points)
Window.bind("<Button-1>", get_points_per_click)
Window.bind("<Button-3>", catch_leaf)
#Window.bind("<space>", get_points) # CHEAT
Window.protocol("WM_DELETE_WINDOW", quit)
Start()
Window.mainloop()

"""
MEDIDAS:
 || Podemos desenhar noutro tamanho e redimencionar o canvas
    Medida das flores: 240x560
    Medida das arvores: 350x700
TO DO:

""" 