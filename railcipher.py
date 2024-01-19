
#Define a function called rail cipher where the user is asked to enter the rail length where the message entered will be returned 
#encrypted on this rail. Assume the rail as a matrix or sublist in a list
#The encrypted message should be read by diagonals to get the origin messages
#For example if you entered the rail number is "3" and the message is : Hi the war is coming
#The result matrix will be as below:
# [['H', 0, 0, 0, 'e', 0, 0, 0, 'i', 0, 0, 0, 'm', 0, 0, 0, 0],
#  [0, 'i', 0, 'h', 0, 'w', 0, 'r', 0, 's', 0, 'o', 0, 'i', 0, 'g', 0]
#  [0, 0, 't', 0, 0, 0, 'a', 0, 0, 0, 'c', 0, 0, 0, 'n', 0, 0]]
def rail():

    n = int(input("Please enter the message rail length\t"))
    message = input("Please enter your message to be encoded\n")
    new_message = message.replace(" ","")
    my_array = [[0 for i in range(len(new_message)+1)]for j in range(n)]

    length_mess = len(new_message)
    row = 0
    old_row = 0
    i = 0

    while length_mess != 0:         
                if row == 0:
                    my_array[row][i] = new_message[i]
                    row +=1
                    old_row = 0
                    length_mess -=1
                    i +=1

                elif  row == 1 and old_row == 0:
                    my_array[row][i] = new_message[i]
                    row +=1
                    length_mess -=1
                    old_row +=1
                    i +=1
                
                elif  row == 1 and old_row == 2:
                    my_array[row][i] = new_message[i]
                    row -=1
                    length_mess -=1
                    old_row -=1
                    i +=1

                elif row ==2:
                    my_array[row][i] = new_message[i]
                    row -=1
                    length_mess -=1
                    old_row +=1
                    i +=1
    return my_array   
print(rail())
