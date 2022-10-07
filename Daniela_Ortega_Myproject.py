#LAB7 COMPLETED BY REGINA AND DANIELA


#importing file with formulas
import Daniela_Ortega_stats

#open file with data and deleting the titles of each column
file = open("50DayFruitData.txt","r")
data= file.read().splitlines()
data.pop(0)

# list to store the values for apples
apples = []

#busco si el numero en mi data equivale a apples para anadirlo a mi lista
for day in data:
    temp = day.split()
    if temp[1] == "apple":
        apples.append(int(temp[2]))


#use formulas and giving the values for apples as "number"
mean = Daniela_Ortega_stats.mean(apples)
median = Daniela_Ortega_stats.median(apples)
mode = Daniela_Ortega_stats.mode(apples)

print("The mean number of apples eaten is: ",mean)
print("The median number of apples eaten is: ",median)
print("The mode number of apples eaten are: ",mode)

#mode=[]
#modeA= Daniela_Ortega_stats.mode(apples)
#mode.append(modeA)


#crear un nuevo archivo y anadirle mi data
with open("Daniela_Ortega_Output.txt", "w") as f:
    f.write("the mean number of apples eaten is:" + str(mean) + "\n" + "The Median number of apples eaten is:" + str(median) + "\n" + "The mode of apples eaten is (are):"+ str(mode) +"\n")
