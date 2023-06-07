#
# File: tons.py
# Descrition: main file for the game
# Author: Yile Wang (王以乐)
# Student ID: 2218040121
# This is my own work as defined by 
#  the University's Academic Misconduct Policy.
#

import random
from abc import ABC

class TonsODice:
    def __init__(self):
        self.__players = []

    def append_players(self, player):
        self.__players.append(player)

    def get_players(self):
        return self.__players
    
    players = property(get_players, append_players)

    def welcome(self):
        print("Welcome to Tons-o-Dice!\n\
Developed by Yile Wang\n\
COMP 1048 Object-Oriented Programming\n")
              
    def menu(self):
        print("What would you like to do?\n\
 (n) register a new player\n\
 (c) show your coins\n\
 (s) show the leader board\n\
 (p) play a game\n\
 (q) quit\n")
        
    def addPlayer(self):
        print("What is the name of the new player?")
        print("> ", end="")
        name = input()
        nameList = []
        for p in self.players:
            nameList.append(p.get_name())
        if name in nameList:
            print("Sorry, the name is already taken.")
            return
        man = Player(name)
        self.players = man
        print("Welcome, " + name)

    def showLeaderboard(self):
        #玩家按照coins排序，coins相同的玩家按照won的比例排序
        try:
            self.players.sort(key=lambda x:( x.get_coins(),x.get_won()/x.get_played() ), reverse=True)
        except:
            print('Some players have not played the game, the ranking may not be accurate.')
        print('=============================')
        print('Name       Played  Won  Coins')
        print('=============================')
        for player in self.players:
            print('{:<10s}{:>8d}{:>5d}{:>6d}'.format(player.get_name(), player.get_played(), player.get_won(), player.get_coins()))
        print('=============================')

    def playGame(self):
        print('Which game would you like to play?\n\
 (e) Even-or-Odd\n\
 (m) Minz\n\
 (b) Bunco')
        print('> ', end='')
        g = input()
        if g == 'e':
            game = Play('EvenOrOdd')
            game.play()
        elif g == 'm':
            if len(self.players) < 3:
                print('Not enough players to play Minz.')
                return
            game = Play('Minz')
            game.play()
        elif g == 'b':
            if len(self.players) < 2:
                print('Not enough players to play Bunco.')
                return
            game = Play('Bunco')
            game.play()

    def showCoins(self):
        print('You have ' + str(self.players[0].get_coins()) + ' coins!')
    
    def run(self):
        self.welcome()
        while True:
            self.menu()
            print("> ", end="")
            command = input()
            if command == "n":
                self.addPlayer()
            elif command == "c":
                self.showCoins()
            elif command == "s":
                self.showLeaderboard()
            elif command == "p":
                self.playGame()
            elif command == "q":
                print('Thank you for playing Tons-o-Dice!')
                quit()




class Player:
    def __init__(self, name):
        self.__name = name
        self.__coins = 100
        self.__won = 0
        self.__played = 0

    def get_name(self):
        return self.__name
    def get_coins(self):
        return self.__coins
    def get_won(self):
        return self.__won
    def get_played(self):
        return self.__played
    def add_coins(self, coins):
        self.__coins += coins
    def add_won(self):
        self.__won += 1
    def add_played(self):
        self.__played += 1


class Play:
    def __init__(self,game) -> None:
        self.__game = game
        self.__playing = None
        self.__player = []
        self.__bid = []
        self.__nameList = []
        for p in tod.players:
            self.__nameList.append(p.get_name())

    


    def add_player(self):
        if self.__game == 'Minz':
            print("Let's play the game of Minz!")
            print('How many players (3-5)?')
            self.a,self.b = 3,5
        elif self.__game == 'EvenOrOdd':
            print("Let's play the game of Even Or Odd!")
            print('How many players (1)?')
            self.a,self.b = 1,1
        elif self.__game == 'Bunco':
            print("Let's play the game of Minz!")
            print('How many players (2-4)?')
            self.a,self.b = 2,4

        print('> ', end='')
        num = input()
        while not num.isdigit():
            print('Invalid number of players.')
            print('> ', end='')
            num = input()
        num = int(num)
        if num < self.a or num > self.b:
            print('Invalid number of players.')
            return -1
        for i in range(num):
            flag = 0
            if flag == 0:
                print(f'What is the name of player #{i+1}?')
                print('>',end='')
                name = input()
                playerNameList = []
                for p in self.__player:
                    playerNameList.append(p.get_name())
                if name in self.__player:
                    print('Sorry, the name is already taken.')
                elif name not in self.__nameList:
                    print('Sorry, the name is not in player list')
                else:
                    self.__player.append(tod.players[self.__nameList.index(name)])
                    flag = 1
                    print(f'How many coins would you bid {name} (1-{tod.players[self.__nameList.index(name)].get_coins()})?')
                    print('>',end='')
                    bid = input()
                    try:
                        bid = int(bid)
                    except:
                        bid = -1
                    while bid < 1 or bid > tod.players[self.__nameList.index(name)].get_coins():
                        print('Invalid number of coins.')
                        print(f'How many coins would you bid {name} (1-{tod.players[self.__nameList.index(name)].get_coins()})?')
                        print('>',end='')
                        bid = input()
                        try:
                            bid = int(bid)
                        except:
                            bid = -1
                    self.__bid.append(bid)



    def play(self):
        a = self.add_player()
        playerNameList = []
        for p in self.__player:
            playerNameList.append(p.get_name())
        while a == -1:
            a = self.add_player()
        if self.__game == 'Minz':
            self.__playing = Minz(playerNameList)
            self.__playing.play()
        elif self.__game == 'EvenOrOdd':
            self.__playing = EvenOrOdd(playerNameList)
            self.__playing.play()
        elif self.__game == 'Bunco':
            self.__playing = Bunco(playerNameList)
            self.__playing.play()

        result = self.__playing.get_result()
        for i in range(len(self.__player)):
            if result[i] == 1:
                if len(result) != 1:
                    self.__player[i].add_coins(-self.__bid[i])
                self.__player[i].add_coins(sum(self.__bid[:]))
                self.__player[i].add_won()
            else:
                self.__player[i].add_coins(-self.__bid[i])
            self.__player[i].add_played()


class Game(ABC):
    def __init__(self) -> None:
        self.__dices = []
    DICE = ['⚀','⚁','⚂','⚃','⚄','⚅']

    def addDice(self,num):
        for i in range(num):
            self.__dices.append(Dice())

    def throw(self):
        print('How strong will you throw (0-5)?')
        print('>',end='')
        try:
            strong = int(input())
        except KeyboardInterrupt:
            quit()
        except:
            strong = -1
        while strong < 0 or strong > 5:
            print('Invalid strength.')
            print('>',end='')
            try:
                strong = int(input())
            except KeyboardInterrupt: #to quit the game when you don't want to play 
                quit()
            except:
                strong = -1
        tmp = []
        for dice in self.__dices:
            dice.throw(strong)
            tmp.append(dice.get_result())
        for d in tmp:
            print(Game.DICE[d-1],end=' ')
        print()
        return tmp


class Dice:
    def __init__(self):
        self.__strong = 0
        self.__result = 0

    def throw(self, strong):
        self.__strong = strong
        self.__result = (random.randint(1,6) + self.__strong) % 6 + 1 #1-6

    def get_result(self):
        return self.__result

class Minz(Game):
    def __init__(self,player) -> None:
        self.__player = player
        self.__result = []
        super().__init__()

    def play(self):
        self.addDice(2)
        print('Let the game begin!')
        while len(self.__result) < len(self.__player):
            temp = []
            for player in self.__player:
                print(f"It's {player}'s turn.")
                dice = self.throw()
                temp.append(dice[0]+dice[1])
            #找出是否存在同样的最小值
            minNum = min(temp)
            minNumList = []
            for i in range(len(temp)):
                if temp[i] == minNum:
                    minNumList.append(i)
            if len(minNumList) == 1:
                print(f'Congratulations, {self.__player[minNumList[0]]}! You win!')
                for i in range(len(self.__player)):
                    if i == minNumList[0]:
                        self.__result.append(1)
                    else:
                        self.__result.append(0)
            else:
                print('Players remaining:',end='')
                for i in range(len(minNumList)):
                    print(f' {self.__player[minNumList[i]]}',end='')
                print()

    def get_result(self):
        return self.__result




class EvenOrOdd(Game):
    def __init__(self,player) -> None:
        self.__player = player
        self.__result = []
        super().__init__()

    def play(self):
        self.addDice(1)
        for player in self.__player:
            print(f'Hey {player}, Even (e) or Odd (o)?')
            print('>',end='')
            choice = input()
            while choice != 'e' and choice != 'o':
                print('Invalid choice.')
                print('>',end='')
                choice = input()
            dice = self.throw()
            if (dice[0] % 2 == 0 and choice == 'e') or (dice[0] % 2 == 1 and choice == 'o'):
                print(f'Congratulations, {player}! You win!')
                self.__result.append(1)
            else:
                print(f'Sorry, {player}! You lose!')
                self.__result.append(0)
    
    def get_result(self):
        return self.__result



class Bunco(Game):
    def __init__(self,player) -> None:
        self.__player = player
        super().__init__()
        self.__result = [0 for i in range(len(self.__player))]

    def play(self):
        self.addDice(3)
        scoreboard = [[0 for i in range(len(self.__player)+2)] for j in range(6)]
        playing = 0
        for i in range(1,7):
            roundFlag = 1
            print(f'<Round {i}>')
            while roundFlag == 1:
                for j in range(len(self.__player)):
                    j = (j + playing-1) % len(self.__player) #循环列表
                    print(f"It's {self.__player[j]}'s turn.")
                    flag = 1
                    while flag == 1:
                        dice = self.throw()
                        if dice[0] == dice[1] == dice[2] == i:
                            print('Bunco!')
                            scoreboard[i-1][j] += 21
                            scoreboard[i-1][len(self.__player)] = j
                            print(f'You earned 21 points, {scoreboard[i-1][j]} points in total.')
                            print(f'{self.__player[j]} is the winner in round {i}!')
                            roundFlag = 0
                            playing = j
                            scoreboard[i-1][len(self.__player)+1] = j
                            flag = 0
                        elif dice[0] == dice[1] == dice[2]:
                            scoreboard[i-1][j] += 5
                            if scoreboard[i-1][j] >= 21:
                                print(f'You earned 5 points, {scoreboard[i-1][j]} points in total.')
                                print(f'{self.__player[j]} is the winner in round {i}!')
                                roundFlag = 0
                                playing = j
                                scoreboard[i-1][len(self.__player)+1] = j
                                flag = 0
                            else:
                                print(f'You earned 5 points, {scoreboard[i-1][j]} points in total.')
                                print(f'Keep playing {self.__player[j]}.')
                        elif dice[0] == dice[1] and dice[0] == i  or dice[0] == dice[2] and dice[0] == i or dice[1] == dice[2] and dice[1] == i:
                            scoreboard[i-1][j] += 2
                            if scoreboard[i-1][j] >= 21:
                                print(f'You earned 2 points, {scoreboard[i-1][j]} points in total.')
                                print(f'{self.__player[j]} is the winner in round {i}!')
                                roundFlag = 0
                                playing = j
                                scoreboard[i-1][len(self.__player)+1] = j
                                flag = 0
                            else:
                                print(f'You earned 2 points, {scoreboard[i-1][j]} points in total.')
                                print(f'Keep playing {self.__player[j]}.')
                        elif dice[0] == i or dice[1] == i or dice[2] == i:
                            scoreboard[i-1][j] += 1
                            if scoreboard[i-1][j] >= 21:
                                print(f'You earned 1 point, {scoreboard[i-1][j]} points in total.')
                                print(f'{self.__player[j]} is the winner in round {i}!')
                                roundFlag = 0
                                playing = j
                                scoreboard[i-1][len(self.__player)+1] = j
                                flag = 0
                            else:
                                print(f'You earned 1 point, {scoreboard[i-1][j]} points in total.')
                                print(f'Keep playing {self.__player[j]}.')
                        else:
                            print(f'You earned 0 points, {scoreboard[i-1][j]} points in total.')
                            flag = 0
                    if roundFlag == 0:
                        break
        letter = 0
        for c in self.__player:
            letter += len(c)
        letter += len(self.__player)*7 + 5
        print('='*letter)
        print('Round       ',end='')
        print('       '.join(self.__player))
        for i in range(6):
            print(f'{i+1}           ',end='')
            for j in range(len(self.__player)):
                print(f'{scoreboard[i][j]}         ',end='')
            print()
        print('='*letter)
        print('Total       ',end='')
        score = []
        for i in range(len(self.__player)):
            print(f'{sum(scoreboard[:][i])}         ',end='')
            score.append(sum(scoreboard[:][i]))
        print()
        print('='*letter)
        print('Bunco      ',end='')
        Bunco = []
        for i in range(len(self.__player)):
            print(f'{scoreboard[:][len(self.__player)].count(i)}         ',end='')
            Bunco.append(scoreboard[:][len(self.__player)].count(i))
        print()
        print('='*letter)
        win = []
        for i in range(len(self.__player)):
            win.append(scoreboard[:][len(self.__player)+1].count(i))
        #赢得最多回合的玩家是总比赛的赢家，通过比较总得分来打破平局
        if win.count(max(win)) == 1:
            winnerIndex = win.index(max(win))
            print(f'{self.__player[winnerIndex]} won {max(win)} rounds, scoring {score[winnerIndex]} points, with {Bunco[winnerIndex]} Bunco(s).')
            self.__result[winnerIndex] = 1
        else:
            winnerIndex = []
            for i in range(len(self.__player)):
                if win[i] == max(win):
                    winnerIndex.append(i)
            winnerScore = []
            for i in range(len(winnerIndex)):
                winnerScore.append(score[winnerIndex[i]])
            if winnerScore.count(max(winnerScore)) == 1:
                winnerIndex = winnerIndex[winnerScore.index(max(winnerScore))]
                print(f'{self.__player[winnerIndex]} won {max(win)} rounds, scoring {score[winnerIndex]} points, with {Bunco[winnerIndex]} Bunco(s).')
                self.__result[winnerIndex] = 1
            else:
                winnerIndex = []
                for i in range(len(winnerScore)):
                    if winnerScore[i] == max(winnerScore):
                        winnerIndex.append(i)
                winnerBunco = []
                for i in range(len(winnerIndex)):
                    winnerBunco.append(Bunco[winnerIndex[i]])
                if winnerBunco.count(max(winnerBunco)) == 1:
                    winnerIndex = winnerIndex[winnerBunco.index(max(winnerBunco))]
                    print(f'{self.__player[winnerIndex]} won {max(win)} rounds, scoring {score[winnerIndex]} points, with {Bunco[winnerIndex]} Bunco(s).')
                    self.__result[winnerIndex] = 1
                else:
                    winnerIndex = []
                    for i in range(len(winnerBunco)):
                        if winnerBunco[i] == max(winnerBunco):
                            winnerIndex.append(i)
                    winnerIndex = winnerIndex[0]
                    print(f'{self.__player[winnerIndex]} won {max(win)} rounds, scoring {score[winnerIndex]} points, with {Bunco[winnerIndex]} Bunco(s).')
                    self.__result[winnerIndex] = 1
    
    def get_result(self):
        return self.__result




if __name__ == "__main__":
    tod = TonsODice()
    tod.run()