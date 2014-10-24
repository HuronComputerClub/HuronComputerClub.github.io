#here is a comment

password = " "

while password!="123":#repeats until the string password contains the value "123"
    
    password=input("What is the password? ")#receives user input
    if password!="123":
        print("That is incorrect")
#code after this is run only once the "while" statement is finished
print("You got the password")
