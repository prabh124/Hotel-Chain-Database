#Command used to read the text file and print the line of the hotel
def printHotel(x):
    commandFile = open('hotels.txt', 'r') 
    job = commandFile.readlines()
    return job[x]
def numOfLines():
    with open('hotels.txt') as r:
        lines = 0
        for line in r:
            lines += 1
    return lines

#function to display menu and submenus, it returns userinput values which is used for the main code, as well as returns a criteria value for some stages of the program
def displayMenu():

    print("\nChoose an option from the following!")
    print("1. Add a new hotel: ")
    print("2. Average of a score criteria: ")
    print("3. Minimum criteria search")
    print("4. Overall average satisfaction of guests: ")
    print("5. Search for a hotel: ")
    print("6. Exit")

    userIn = input()
    userIn = int(userIn)

    while (userIn < 1) or (userIn > 6):
        userIn = input("ERROR: Enter a choice between 1 and 6! \n")
        userIn = int(userIn)

    if userIn is 1:
        print("Adding a hotel!")
        return 1, 0

    elif userIn is 2:
        print("\nChoose from the following criteria to find an average score of!:")
        print("1. Preferred location average: ")
        print("2. Reputation average: ")
        print("3. Cleanliness and Comfort average: ")
        print("4. Amenities average: ")
        print("5. Price average: ")   
        print("6. Overall Luxury average: ")
        print("7. Overall satisfaction of guests average: ")
       
        userInTwo = input()
        userInTwo = int(userInTwo)
        while (userInTwo < 1) or (userInTwo > 7):
            userInTwo = input("ERROR: Enter a choice between 1 and 7! \n")
            userInTwo= int(userInTwo)

        if userInTwo is 1:
            return 2, 0
        elif userInTwo is 2:
            return 3, 0
        elif userInTwo is 3:
            return 4, 0
        elif userInTwo is 4:
            return 5, 0
        elif userInTwo is 5:
            return 6, 0
        elif userInTwo is 6:
            return 7, 0
        else:
            return 8, 0

    elif userIn is 3:
        print("\nChoose from the following criteria to find a minimum score!:")
        print("1. Preferred location: ")
        print("2. Reputation score: ")
        print("3. Cleanliness and Comfort score: ")
        print("4. Amenities score: ")
        print("5. Price score: ")
        print("6. Overall Luxury score: ")
        print("7. Overall satisfaction of guests: ")
        userInThree = input()
        userInThree = int(userInThree)
        while (userInThree < 1) or (userInThree > 7):
            userInThree = input("ERROR: Enter a choice between 1 and 7! \n")
            userInThree= int(userInThree)

        if userInThree is 1:
            criteria = input("Enter a percentage (0-1) that you want the criteria to be above!")
            criteria = float(criteria) * 25
            return 9, criteria

        elif userInThree is 2:
            criteria = input("Enter a percentage (0-1) that you want the criteria to be above!")
            criteria = float(criteria) * 25
            return 10, criteria

        elif userInThree is 3:
            criteria = input("Enter a percentage (0-1) that you want the criteria to be above!")
            criteria = float(criteria) * 15
            return 11, criteria

        elif userInThree is 4:
            criteria = input("Enter a percentage (0-1) that you want the criteria to be above!")
            criteria = float(criteria) * 20
            return 12, criteria

        elif userInThree is 5:
            criteria = input("Enter a percentage (0-1) that you want the criteria to be above!")
            criteria = float(criteria) * 20
            return 13, criteria

        elif userInThree is 6:
            criteria = input("Enter a percentage (0-1) that you want the criteria to be above!")
            criteria = float(criteria) * 35
            return 14, criteria
        else:
            criteria = input("Enter a percentage (0-1) that you want the criteria to be above!")
            criteria = float(criteria) * 65
            return 15, criteria

    elif userIn is 4:
        print("Finding the amount of hotels with an overall average satisfaction level below 70%! ")
        criteria = 1
        criteria = float(criteria) * 45.5
        return 16, criteria

    elif userIn is 5:
        print("Search for a hotel!")
        criteria = input("Enter the hotel number!")
        return 17, criteria

    else:
        return 0, 0
    
# ADD FUNCTION TAKEN FROM GIVEN CODES
def add(tree, value):
    if tree == None:
        return {'data':value, 'left':None, 'right':None}
    elif value < tree['data']:
        tree['left'] = add(tree['left'],value)
        return tree
    elif value > tree['data']:
        tree['right'] = add(tree['right'],value)
        return tree
    else: # value == tree['data']
        return tree # ignore duplicate

# PRINT VALE FUNCTION TAKEN FROM GIVEN CODES, ONLY USED FOR EASE OF USE
def printValues(tree):
    if tree == None:
        return
    printValues(tree['left'])
    print(tree['data'])
    printValues(tree['right'])

#tree creation function, it iterates through every line of the file and calls the add to tree function
def createTree(tree):    
    num = 0
    for num in range(numOfLines()):
        node = printHotel(num)
        node = node.split(",")
        node = list(map(float, node))
        tree = add(tree, node)
   
    return tree

#same as createTree, except it accepts input for the many scores and values and then calls the add function
def manualAddToTree(tree, newLeaf):
    newLeaf = newLeaf.split(",")
    newLeaf = list(map(float, newLeaf))
    tree = add(tree, newLeaf)
    
    return tree

#Sum function, used to calculate sum of the criteria index or certain type of score (ex. amenities)
def sum(tree, criteriaIndex):
    if tree is None:
        return 0
    return (tree['data'][criteriaIndex] + sum(tree['left'], criteriaIndex) + sum(tree['right'], criteriaIndex))

#count function used to count the number of leafs in the tree
def count(tree):
    if tree is None:
        return 0
    return (1 + count(tree['left']) + count(tree['right']))

#finding hotels with a score higher than the given criteria, used by comparing each node to criteria values
def minimumScore(tree, userIn, criteria):
    if tree is None:
        return 0
    elif tree['data'][userIn] <= criteria:
        return 0 + minimumScore(tree['left'], userIn, criteria) + minimumScore(tree['right'], userIn, criteria)
    print(tree['data'][0])
    return(1 + minimumScore(tree['left'], userIn, criteria) + minimumScore(tree['right'], userIn, criteria))

#average satisfaction is the same as above except the sign is reversed in the if statement as we are searching for below a value, notq above
def avgSatisfaction(tree, userIn, criteria):
   
    if tree is None:
        return 0
    elif tree['data'][userIn] >= criteria:
        
        return 0 + avgSatisfaction(tree['left'], userIn, criteria) + avgSatisfaction(tree['right'], userIn, criteria)
    return(1 + avgSatisfaction(tree['left'], userIn, criteria) + avgSatisfaction(tree['right'], userIn, criteria))

#hotel search function to see if any leaf in the tree equates to the input given
def hotelSearch(tree, hotelNumber):
    if tree is None:
        return 0
    if tree['data'][0] == hotelNumber:
        print("Located a hotel of number: ", str(hotelNumber))
    if (hotelNumber < tree['data'][0]):
        return hotelSearch(tree['left'], hotelNumber)
    if (hotelNumber > tree['data'][0]):
        return hotelSearch(tree['right'], hotelNumber)
    return tree['data']

#global variables, num is so that we can start the tree on the first loop, hoteltree is designating the tree to none
num = 0 
hotelTree = None

#Main fun, keep iterating until a break
while True:
    
    #if it is loop one, create the tree. Else continue as normal
    if num is 0:
        
        hotelTree = createTree(hotelTree)
        
    else:
        userIn, criteria = displayMenu()

        #if the user chose to exit, program will close
        if userIn is 0:
            print("Exiting")
            break
        #manually add to tree
        elif userIn is 1:
            newLeaf = input("Please enter the hotel number and scores seperated by commas ex. 2020,23,13,9,16,10,25,30 ")
            tree = manualAddToTree(hotelTree, newLeaf)
            print("Added!")
            #find average of scores, used by both the sum and count functions
        elif 2 <= userIn <= 8:
            average = sum(hotelTree, (userIn - 1)) / count(hotelTree)
            print(average)
            #find scores above a threshold
        elif 9 <= userIn <= 15:
            print("\nThe following hotels had a score above: ", str(criteria))
            minScore = minimumScore(hotelTree, (userIn - 8), criteria)
            print(str(minScore) + " Hotels had a score above ", str(criteria) + "!")
            #average overall satisfaction 
        elif userIn is 16:
            print(criteria)
            avgOverall = avgSatisfaction(hotelTree, (userIn - 9), criteria)
            print(str(avgOverall) + " Hotels had overall guess satisfaction score of less than 70%! ")
            #finally, searching for hotel numbers 
        else: 
            
            hotelSearch = (hotelSearch(hotelTree, float(criteria)))
            #if nothing is found print an error
            if hotelSearch is 0:
                print("ERROR: No hotel matches the number you entered!")
                #if found print the contents
            else: 
                print("The hotel and all its scores are as follows: " + str(hotelSearch))

    num += 1
    


