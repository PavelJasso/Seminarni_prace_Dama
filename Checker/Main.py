import csv
import pygame as pg
import itertools
from l_s import load_stones
from Pr_s import print_stones
from Pl_s import place_stones
from Stone import stone

def main():
    #názvy pro kameny
    w_stones = ["W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12"]
    b_stones = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12"]

    load_stones(w_stones,b_stones)

    print_stones(w_stones,b_stones)

    if place_stones(w_stones,b_stones)==True:    
        print_stones(w_stones,b_stones)

        #BĚH PROGRAMU
        #inicializuje všechny pygame moduly
        pg.init()                                          
        
        #barvy hrací plochy
        BLACK = pg.Color('black')
        WHITE = pg.Color('white')
        
        screen = pg.display.set_mode((840, 840))        #velikost okna
        clock = pg.time.Clock()

        colors = itertools.cycle((WHITE, BLACK))        #nastavení barev
        tile_size = 100                                 #velikost čtverce
        width, height = 8*tile_size, 8*tile_size        #velikost hrací plochy
        background = pg.Surface((width, height))        #tvorba pozadí, na které se dále vykreslí šachovnice    

        #vytvoření hrací plochy
        for y in range(0, height, tile_size):        
            for x in range(0, width, tile_size):            
                rect = (x, y, tile_size, tile_size)
                clr=next(colors)                       
                rectangle=pg.draw.rect(background, clr, rect)
                
                #vykreslení kamenů
                for i in range(12):
                    if w_stones[i].get_center()==[0,0]:               #pokud má střed v (0,0), pak není ve hře => nevykreslí se
                      break 
                    else:
                        pg.draw.circle(background, 'white', w_stones[i].get_center(),40)                

                for i in range(12):
                    if b_stones[i].get_center()==[0,0]:
                      break
                    else: 
                        pg.draw.circle(background, 'gray', b_stones[i].get_center(),40)                
              
            next(colors)
        game_exit = False

        #pozadí a ohraničení
        screen.fill((60, 70, 90))               #barva pozadí    
        screen.blit(background, (20, 20))       #velikost ohraničení

        #nastavení písmen a čísel hrací plochy
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 15)
        pismena = ["A","B","C","D","E","F","G","H"]
        poz=70
        for i in pismena:
            textsurface = myfont.render(f"{i}", False, (0,0,0))
            screen.blit(textsurface,(poz,0))
            poz=poz+100

        poz=50
        for i in range(8,0,-1):        
            textsurface = myfont.render(f'{i}', False, (0,0,0))
            screen.blit(textsurface,(10,poz))
            poz=poz+100

        #běh okna/programu a eventy v něm
        while not game_exit:
            for event in pg.event.get():           #dostává, co se děje, hlavně trackuje pozici myši, zaznamená i stisknutí
                print(event)            
                if event.type == pg.QUIT:
                    game_exit = True        

            pg.display.flip()                        #zobrazí display
            clock.tick(30)                          #zjistit, nemusí tu být  (pro plynulejší běh programu)      

        pg.quit()  
            
        print_stones(w_stones,b_stones)    


if __name__=="__main__":
    main()