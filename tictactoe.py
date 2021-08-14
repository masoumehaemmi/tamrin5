def show_game_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end='  ')
        print()

game= [["_","_","_"],
       ["_","_","_"],
       ["_","_","_"]]

show_game_board()

while True:
    print("player1")
    row=int(input("satr ra vared kon"))
    col=int(input("soton ra vared kon"))
    game[row][col]="x"
    show_game_board()

    print("player2")
    row=int(input("satr ra vared kon"))
    col=int(input("soton ra vared kon"))
    game[row][col]="o"
    show_game_board()

