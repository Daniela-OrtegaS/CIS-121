import Daniela_Ortega_Stats


file = open("500DayFruitData.txt" ,"r")
#Abrir el file donde tengo la informacion

data= file.read().splitlines()
#lo abre y se asegura que todas las lineas sean incluidas con splitlines

data.pop(0)
#removing the title line usando "variable".pop(index de lo que quiero quitar)
#print(data[0])

apples = []
banana =[]
strawberries = []

#Loop to go through the list
for day in data:
    temp = day.split()
    if temp[1] == "apple":
        apples.append(int(temp[2]))
    elif temp[1] == "banana":
        banana.append(int(temp[2]))
    elif temp[1] == "strawberry":
        strawberries.append(int(temp[2]))

#print(apples)

mean = Daniela_Ortega_Stats.mean(apples)
median = Daniela_Ortega_Stats.median(apples)
meanB = Daniela_Ortega_Stats.mean(banana)
medianB = Daniela_Ortega_Stats.median(banana)
meanS= Daniela_Ortega_Stats.mean(strawberries)
medianS= Daniela_Ortega_Stats.median(strawberries)


print("Median for apples: ", median)
print("Mean for apples: ", mean)
print("Median for Bananas: ", medianB)
print("Mean for Bananas: ", meanB)
print("Median for Strawberries: ", medianS)
print("Mean for Strawberries: ", meanS)


with open("Daniela_Ortega_Output.txt", "w") as f:
    #crear un nuevo file en el que estoy escribiendo "w" de write y "f" de file

    f.write("Apples:\n")
    f.write("Mean:"+ str(mean) + "\n" + "Median:" + str(median) +"\n")
    f.write("Bananas: \n")
    f.write("Mean:" + str(meanB) + "\n" + "Median:" + str(medianB)+"\n")
    f.write("Strawberries:\n")
    f.write("Mean:"+ str(meanS) + "\n" + "Median:" + str(medianS) + "\n")

