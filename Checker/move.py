from ast import Break
from Stone import stone
from C_M import center_mouse
from updt import screen_update
from Is_st import is_stone
from Is_st import is_true
import pygame as pg
from Plr import Player   #ošetřit, že jen ten hráč, co hraje hýbá se svými kameny

#dalo by se to rozdělit na dvě fce......ve vnitřním ifu!!!!! resp. vnitřní if kontrolovat v mainu, aby fce nevracela tolik hodnot!!!!!
def move_stone(mouse_p,bg,scr,tile_s,ch_stone,new_rct_pos,bol,next_player):     #ch_stone a new_rct_pos musim volat, protože si je musím pamatovat globálně, abych se na ně mohl odkázat znovu
        if (ch_stone!=[])&(bol==False):          #pokud už mám vybraný kámen a hodlám udělat tah -> kliknu na pole bez kamene
            rect = (new_rct_pos[0],new_rct_pos[1], tile_s, tile_s)
            pg.draw.rect(bg, 'black', rect)
            pg.draw.circle(bg, ch_stone[0].get_color(), mouse_p,40)                                 
            ch_stone[0].center(mouse_p)   #chosed.center(mouse_p)
            screen_update(scr,bg)
            next_player=True   
        return next_player   
        
    #return ch_stone,new_rct_pos,next_player