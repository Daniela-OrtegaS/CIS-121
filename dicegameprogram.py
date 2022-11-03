#
from dicegameclasses import HighTwoGame

print("Game one: ")

game1 = HighTwoGame("Matt", "Ashley")

game1.playOneGame()

print("")

print("Game two:")

game2 = HighTwoGame("Dexter", "Eugene")

game2.playOneGame()

print("")

print("Play many games: ")

game3 = HighTwoGame("Regina", "Mayiie")

game3.playManyGames(4)