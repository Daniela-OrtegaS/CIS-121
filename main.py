groceryList = []
costOfItem = []

item = input("Enter your grocery list item: ")
groceryList.append(item)
while item != "DONE":
    cost = int(input("Enter your grocery list cost in dollars: "))
    costOfItem.append(cost)
    item = input("Enter your grocery list item: ")
    groceryList.append(item)
    # cost = input("Enter your grocery list cost in dollars: ")
    # costOfItem.append(cost)

groceryList.pop()

print("My grocery List is:", groceryList)
print("Cost of each item is:", costOfItem)

groceries = {}
for i in range(len(groceryList)):
    groceries[groceryList[i]] = costOfItem[i]
print(groceries)


totalPurchase = 0
for i in costOfItem:
    totalPurchase += i
print("your total purchase is:", totalPurchase)

purchase2 = {
    "banana": 3,
    "apples": 3,
    "strawberries": 5,
    "orange": 4
}

def checkItems(data1, data2):
    length = len(data1)
    temp = 0
    for key1 in data1:
        for key2 in data2:
            if key1 == key2:
                temp += 1
    if length == temp:
        print(data1, "and", data2, "have the same items.")
    else:
        print("Lists have different items")

checkItems(groceries, purchase2)

def checkCost(data1, data2):
    list1 = list(data1.keys())
    list2 = list(data2.keys())

    for i in range (len(list1)):
        for x in range(len(list2)):
            if list1[i] == list2[x]:
                if data1[list1[i]] > data2[list2[i]]:
                    print("The cost for", list1[i], "is cheaper in your second list")
                elif data1[list1[i]] < data2[list2[x]]:
                    print("The cost for", list1[i], "is cheaper in your first list")
                else:
                    print("Your costs are the same")
            elif list1[i] != list2[x]:
                print("your item", list1[i], "only appears in one of your lists")

checkCost(groceries, purchase2)










# purchase2["banana"]



