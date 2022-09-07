# lab 2
#1a
human_age = 6
dog_year = 7
human_in_dog_years = human_age * dog_year

print("An age", human_age,"human should be",human_in_dog_years,"in dog years")

#1b An age 2.1 human should be 14 years, 8 months, and 12 days in dog age.

human_age= float(input("Please enter your age: "))
dog_year = 7
human_in_dog_years = (human_age * dog_year)
months = (human_in_dog_years*12) - int(human_in_dog_years)*12
days = (months*30) - int(months)*30

print("An age", human_age, "human should be",
      int(human_in_dog_years),"years", int(months),
      "months",int(days),"days, in dog age")


#2a
human_age = 18
cat_year = 9
human_in_cat_years = human_age/ cat_year

print("An age", human_age,"human should be",human_in_cat_years,"in cat age")
# escribir int antes del parentesis para que el output sea un numero entero despues de la division



#2b An age 21.6 human should be 2 years, 4 months, and 24 days in cat age.

human_age= float(input("Please enter your age"))
cat_year = 9
human_in_cat_years = (human_age / cat_year)
months = (human_in_cat_years*12)-int(human_in_cat_years)*12
days = (months*30)-int(months)*30
print("An age", human_age, "human should be", int(human_in_cat_years),"years", int(months),"months",int(days),"days,in cat age")


#3a
human_age = 12
horse_years = 3 * ((((human_age ** 2)-47)/7)+12)
# usar los dos astericos para elevar un numero
print("An age", human_age,"human should be about",horse_years,"in horse age")

#3b An age 12 human should be 77 years, 6 months, and 25 days in horse age

human_age= float(input("Please enter your age"))
horse_years = 3 * ((((human_age ** 2)-47)/7)+12)
months = (horse_years*12)-int(horse_years)*12
days = (months*30)-int(months)*30

print("An age", human_age,"human should be about",int(horse_years), int(months), "months","and",int(days),"days in horse age")

#para que el usuario ponga su informacion
#human_age = int(input("Please enter your age:"))

#write a script that asks the user for their name, lastnmae and age. Print out their age times 35

name= (input("Please type your name"))
last_name = (input("Please type your lastname"))
age= int(input("Please enter your age"))
age35 = age * 35
print("Name:",name)
print("Lastname:", last_name)
print("your age is",age35)


