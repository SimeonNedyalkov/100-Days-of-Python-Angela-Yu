import random


theBoard = {'7':" ",'8':" ",'9':" ",
            '4':" ",'5':" ",'6':" ",
            '1':" ",'2':" ",'3':" ",}


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

printBoard(theBoard)

gameon = False
count = 0

def game():

    while gameon == False:
        global count
        yourturn = "X"
        computerturn = "O"

        # Game Over
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != '':
                print("Game over !!!")
                print(f'{theBoard["8"]} won')
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != '':
                print("Game over !!!")
                print(f'{theBoard["6"]} won')
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != '':
                print("Game over !!!")
                print(f'{theBoard["3"]} won')
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != '':
                print("Game over !!!")
                print(f'{theBoard["5"]} won')
            if theBoard['3'] == theBoard['5'] == theBoard['7'] != '':
                print("Game over !!!")
                print(f'{theBoard["5"]} won')
            if theBoard['1'] == theBoard['4'] == theBoard['7'] != '':
                print("Game over !!!")
                print(f'{theBoard["4"]} won')
            if theBoard['2'] == theBoard['5'] == theBoard['8'] != '':
                print("Game over !!!")
                print(f'{theBoard["5"]} won')
            if theBoard['3'] == theBoard['6'] == theBoard['9'] != '':
                print("Game over !!!")
                print(f'{theBoard["6"]} won')
            if count == 9:
                print("Game over its a TIE !!!")


        # Computer
        if count == 1 or count == 3 or count == 5 or count == 7 or count == 9:
            getrandint = str(random.randint(1,9))
            if theBoard[getrandint] == ' ':
                theBoard[getrandint] = computerturn
                printBoard(theBoard)
                count += 1
            elif theBoard[getrandint] != ' ':
                newrandint = str(random.randint(1, 9))
                if theBoard[newrandint] == ' ':
                    theBoard[newrandint] = computerturn
                    printBoard(theBoard)
                    count += 1
        move = input("where do you want to play: ")

        # ME
        if theBoard[move] == ' ':
            theBoard[move] = yourturn
            printBoard(theBoard)
            count += 1
        else:
            print("Its already taken")



game()

