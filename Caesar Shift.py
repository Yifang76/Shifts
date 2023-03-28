alphabetC = list["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabet = list["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shiftList = list[" ",]

shiftNum = int(input("How many shifts would you like to perform?  "))
for i in range(shiftNum):
    shiftList = [shiftList, " "]
    newList = [shiftList, alphabetC]
    newList2 = [shiftList, alphabet]
print(shiftList)
print(newList)
print(newList2)

message = input("Please state your message. ")
message = [message]
print(message)
