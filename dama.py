import numpy as np
import csv

def create_board(x):
    if x==1:
        board=np.array([["XXXX","    ","XXXX","    ","XXXX","    ","XXXX","    "],["    ","XXXX","    ","XXXX","    ","XXXX","    ","XXXX"],["XXXX","    ","XXXX","    ","XXXX","    ","XXXX","    "],["    ","XXXX","    ","XXXX","    ","XXXX","    ","XXXX"],["XXXX","    ","XXXX","    ","XXXX","    ","XXXX","    "],["    ","XXXX","    ","XXXX","    ","XXXX","    ","XXXX"],["XXXX","    ","XXXX","    ","XXXX","    ","XXXX","    "],["    ","XXXX","    ","XXXX","    ","XXXX","    ","XXXX"]])
    if x==2:
        board=np.array([["XXXX"," B1 ","XXXX"," B2 ","XXXX"," B3 ","XXXX"," B4 "],[" B5 ","XXXX"," B6 ","XXXX"," B7 ","XXXX"," B8 ","XXXX"],["XXXX"," B9 ","XXXX"," B10","XXXX"," B11","XXXX"," B12"],["    ","XXXX","    ","XXXX","    ","XXXX","    ","XXXX"],["XXXX","    ","XXXX","    ","XXXX","    ","XXXX","    "],[" A9 ","XXXX"," A10","XXXX"," A11","XXXX"," A12","XXXX"],["XXXX"," A5 ","XXXX"," A6 ","XXXX"," A7 ","XXXX"," A8 "],[" A1 ","XXXX"," A2 ","XXXX"," A3 ","XXXX"," A4 ","XXXX"]])
    return board

def show_board(board):
    j=8   
    print("   |                     BLACK                             |")
    print("   ---------------------------------------------------------")
    print("       A      B      C      D      E      F      G      H  ")
    for i in board:
        print(f"{j}: {i}")
        j=j-1
    print("   ---------------------------------------------------------")
    print("   |                     WHITE                             |")

#vyřešit 2 stejné pozice, načtení do šachovnice, délka větší jak 2 pro řádek v csv
def place_stones(board):
    filename="dama3.csv"
    b_stone_positions=["a7", "b6", "b8", "c7", "d6", "d8", "e7", "f6", "f8", "g7", "h6", "h8"]
    w_stone_positions=["a1", "a3", "b2", "c1", "c3", "d2", "e1", "e3", "f2", "g1", "g3", "h2"]
    w_used_positions=[]
    b_used_positions=[]

    #otevření csv
    with open(filename,"r") as csvfile:
        csvreader =list(csv.reader(csvfile,delimiter=';'))    
        #print(csvreader)
        #chyba vstupu csv
        if len(csvreader)!=25:                                             #špatný formát (veliksot) souboru
            raise Exception("špatný vstup csv!")
        for i in range(1,25):                       
            #kontrola kamenů            
            if ((csvreader[i][0] in w_stone_positions) & (csvreader[i][1]=="w")):       #v pořádku, políčko ano, barva ano
                print("tady bílá")
            elif ((csvreader[i][0] in b_stone_positions) & (csvreader[i][1]=="b")):         #v pořádku, políčko ano, barva ano                
                print("tady černá")
            else:                
                raise Exception("špatný vstup csv!")
        board=create_board(2)  
        return board  
                
                


def main():
    
    game=input("Chcete začít hru? (Y/N): ")
    if game=="Y":
        ch_board = create_board(1)
        show_board(ch_board)        
        ch_board =place_stones(ch_board)
        show_board(ch_board) 
    else:
        print("tak nic!") 

if __name__=="__main__":
    main()