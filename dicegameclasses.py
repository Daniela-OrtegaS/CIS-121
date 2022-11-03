import random
#
# class Die:
#     def __init__(self, numberSides, faceUpValue):
#         self.numberSides= int(input("Please enter the number of sides of your die:"))
#         self.faceUpValue = 1
#     def roll(self):
#
#     def getValue(self):
#
# class Player(Die):
#     def __init__(self, rollDice, getDiceValue):
#         self.rollDice = rollDice
#         self.getDiceValue = getDiceValue
#
# class HighTwoGame(Player):
#     def __init__(self, playOneGame, playManyGames):
#         self.playOneGame = playOneGame
#         self.playManyGames = playManyGames

##########################################################
class HighTwoGame:

  def __init__(self, player1Name, player2Name):
    self.player1 = Player(player1Name, Die(6, 1), Die(10, 1))
    self.player2 = Player(player2Name, Die(6, 1), Die(10, 1))
    self.winner = ""
    self.loser = ""
    self.winnerScore = -1
    self.loserScore = -1

  def __str__(self):
    return f"Player 1: {self.player1} Player 2: {self.player2}"

  def playOneGame(self, isManyGames=False):
    self.player1.rollDice()
    self.player2.rollDice()
    self.getWinner()

    if (not isManyGames):
      print(f"{self.winner} rolled {self.winnerScore}")
      print(f"{self.loser} rolled {self.loserScore}")

    print(f"The score is {self.winnerScore} to {self.loserScore}")
    if (self.winnerScore == self.loserScore):
      print("Tie")
    else:
      print(f"{self.winner} wins!")

  def playManyGames(self, numGames):
    for gameCount in range(numGames):
      print(f"Game {gameCount+1}:")
      self.playOneGame(True)
      print()

  def getWinner(self):
    if (self.player1.getDiceValue() > self.player2.getDiceValue()):
      self.winner = self.player1.getName()
      self.winnerScore = self.player1.getDiceValue()
      self.loser = self.player2.getName()
      self.loserScore = self.player2.getDiceValue()
      return self.winnerScore

    self.winner = self.player2.getName()
    self.winnerScore = self.player2.getDiceValue()
    self.loser = self.player1.getName()
    self.loserScore = self.player1.getDiceValue()
    return self.winnerScore


#####################################
class Player:

  def __init__(self, player, die1, die2):
    self.player = player
    self.die1 = die1
    self.die2 = die2
    self.name = player

  def __str__(self):
    return f"Player: {self.player1}, Die 1: {self.die1}, Die 2: {self.die2}"

  def rollDice(self):
    self.die1.roll()
    self.die2.roll()

  def getDiceValue(self):
    return self.die1.__add__(self.die2)

  def getName(self):
    return self.name


#####################################
class Die:

  def __init__(self, numSides, faceUpValue):
    self.numSides = numSides
    self.faceUpValue = faceUpValue

  def __str__(self):
    return f"NumSides: {self.numSides}, FaceUpValue: {self.faceUpValue}"

  def getFaceUpValue(self):
    return self.faceUpValue

  def roll(self):
    self.faceUpValue = random.randint(1, self.numSides)

  def getValue(self):
    return self.faceUpValue

  def __add__(self, otherDie):
    return self.faceUpValue + otherDie.getFaceUpValue()

  def __gt__(self, otherDie):
    return self.faceUpValue > otherDie.getFaceUpValue()


