from ast import Break
from Stone import stone
from C_M import center_mouse
from updt import screen_update
from Is_st import is_stone
from Is_st import is_true
import pygame as pg
from Plr import Player   #ošetřit, že jen ten hráč, co hraje hýbá se svými kameny

def Chosed(mouse_p,ws,bs,bg,scr,ch_stone,Pl_now):
    chosed=is_stone(ws,bs,mouse_p,ch_stone)       #vrátí, zda je ten kámen na stejný pozici, jako myš 
    if (chosed.get_color())==(Pl_now.get_color()):     #zda má vybraný kámen stejnou bravu jako hráč
            ch_stone.append(chosed)                             #přidej vybranej stone do seznamu, pro kontrolu
                                                                                                        
            #pokud jsem něco přidal do seznamu chosed a ten kámen neni vybrán
            pg.draw.circle(bg, 'red', mouse_p,40)            
                    
                    #print(f"pozice myši: {mouse_p}")
                    #print(f"čtverec: {new_rct_pos}")
            screen_update(scr,bg)
                    #print(ch_stone[0]) 

    return ch_stone