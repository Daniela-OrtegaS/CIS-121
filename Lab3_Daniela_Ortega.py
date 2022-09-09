"""
Daniela Ortega
9/9/2022

Description of what this program does
"""
#This program calculates TaxesOwed based on the income of the user and their marital status.
import sys


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")


# Your code goes here

if 0 <= earnedIncome <= 9950 and maritalStatus == "s":
	taxOwed = earnedIncome*0.1
	print("This year you owe", taxOwed, "in taxes")
elif 0 <= earnedIncome <= 19900 and maritalStatus == "m":
	taxOwed = earnedIncome*0.1
	print("this year you owe", taxOwed,"in taxes")
# Revisar la primera categoria con el 10% si estan casados o solteros

if 9951<= earnedIncome <= 40525 and maritalStatus == "s":
	taxOwed = ((9950*0.1) + ((earnedIncome-9950)*0.12))
	print("This year you owe", taxOwed, "in taxes")
elif 19901 <= earnedIncome <= 81050 and maritalStatus == "m":
	taxOwed = ((19900 * 0.1) + ((earnedIncome - 19900)* 0.12))
	print("this year you owe", taxOwed,"in taxes")
# Segunda categoria. Calcular el 10% de la primera cantidad y sumarle el 12% del resto

if 40526 <= earnedIncome <= 86375 and maritalStatus == "s":
	taxOwed = (((earnedIncome - 40525)*0.22)+(30575*.12)+(9950*.10))
	print("This year you owe", taxOwed, "in taxes")
elif 81051 <= earnedIncome <= 172750 and maritalStatus == "m":
	taxOwed = (((earnedIncome - 81050) * 0.22) + (61150 * .12) + (19900 * .10) )
	print("this year you owe", taxOwed,"in taxes")
# Calcular el 22%. Primero restarle al income la cantidad mayor del 12%. Para sacar el 12% restarle a la cantidad mayor
# de la categoria anterior ( 81050 para m) el mayor de la primera categoria (19900 para m) y multiplicar eso por el 12% +
# la primera cantidad por el 10%

if earnedIncome > 86375 and maritalStatus == "s" or earnedIncome > 172750 and maritalStatus == "m":
	print("Our calculator does not work for you")

