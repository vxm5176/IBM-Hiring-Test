def bubbleSort(user_list):
    for i in range(len(user_list)-1,0,-1):
        for j in range(i):
            if user_list[j]>user_list[j+1]:
                temp = user_list[j]
                user_list[j] = user_list[j+1]
                user_list[j+1] = temp

if __name__ == "__main__":

    input_string = input('Enter elements of a list separated by space ')
    print("\n")
    user_list = input_string.split()

    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])

    bubbleSort(user_list)
    print(user_list)