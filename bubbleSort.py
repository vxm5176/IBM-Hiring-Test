import math


def bubbleSort(user_list):
    for i in range(len(user_list)-1,0,-1):
        for j in range(i):
            if user_list[j]>user_list[j+1]: #If the current value is bigger than the next value
                temp = user_list[j]
                user_list[j] = user_list[j+1] #Replace the current value with the next
                user_list[j+1] = temp #Replace the next value with the original current

if __name__ == "__main__":

    input_string = input('Enter elements of a list separated by space: ')
    print("\n")
    user_list = input_string.split()


    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = float(user_list[i]) #Initially convert all values to floats

        if user_list[i] / math.ceil(user_list[i]) == 1: #If we have a whole number
            user_list[i] = int(user_list[i]) #Convert that value to an int to remove trailing zeros


    bubbleSort(user_list)
    print(user_list)
