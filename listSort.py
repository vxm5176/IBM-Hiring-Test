def numValleys(user_list):
    base = 0 #Initialize altitude at sea level
    baseList = [] #Initialize an empty list which will store the altitudes
    valleys = 0 #Initialize a count for the number of valleys
    for i in range(len(user_list)):
        if user_list[i] == "U":
            base += 1 #U signifies an increase in altitude
        elif user_list[i] == "D":
            base -=1 #D signifies a decrease in altitude
        baseList.append(base) #Add current altitude to a list of altitudes
    for i in range(len(baseList)-1):
        if baseList[i] == -1 and baseList[i+1] == 0: #A valley means we go from -1 to 0
            valleys += 1

    return valleys


if __name__ == "__main__":

    input_string = list(input('Enter elements of a list:'))
    print("\n")

    print(numValleys(input_string))

