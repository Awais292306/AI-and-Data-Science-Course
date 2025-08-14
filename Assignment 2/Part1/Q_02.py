a = int(input("Enter Your Age: "))

# if, elif, else ladder 

if(a>=18):
    print("you are eligible to make cnic")
    print("Thankyou")

elif(a<0):
    print("you are entering an invalid negative age")
    print("Its wrong")

elif(a==0):
    print("you are entering 0 which is not a valid age")
    print("Not matched")
    
else:
    print("You are not eligible to make cnic")
    print("Try later")
    
print("End")
    
