"""
This isnt the greatest code, and would never work in a real-life enviroment, but it was for a computer science work booklet and I was tired.
The balance doesnt change if you withdraw or deposit, and I might change that later.
"""
#Import the time module
import time
#Create the base balance variable
balance = 67.14 
#Placing everything in a function makes it easier to restart if needed
def main():
    #If the balance is under 100, it removes the ones and decimal values
    if balance <100:
        balance21 = balance // 10
        int(balance21)
        balance2 = balance21 * 10
    #To make the code shorter, I made it so the balance cannot be over 100
    else:
        print("you got too many rikos, criminal activity detected, police have been alerted and faputa is 300m from your house") 
        exit()
    #Simple welcome
    print("welcome to da sosu bank\n1. display rikos\n2. withdraw rikos\n3. deposit rikos\n9. return card")
    o = input()
    #Show balance and amount able to withdraw
    if o == "1":
        print("you have ",balance, "rikos, you can withdraw", balance2, "rikos"); main()
    #Withdraw panel
    if o == "2":
        print("how much would you like to withdraw (10, 20, 40, 60, 80) or do you wanna return to menu (101) or return card (102)") 
        #Making it so you cannot withdraw less than 10 rikos
        o2 = int(input())
        if o2 <10: print("you cant do that fool"); exit()
        #Not the most efficient, but I was tired while writing this
        elif o2 in range(10,20): print("withdrawing 10 rikos now..."); time.sleep(0.5); print("withdraw complete, check below you for your rikos") 
        elif o2 in range(20,40): print("withdrawing 20 rikos now..."); time.sleep(0.5); print("withdraw complete, check below you for your rikos") 
        elif o2 in range(40, 60): print("withdrawing 40 rikos now..."); time.sleep(0.5); print("withdraw complete, check below you for your rikos") 
        elif o2 in range(60, 80): print("withdrawing 60 rikos now..."); time.sleep(0.5); print("withdraw complete, check below you for your rikos") 
        elif o2 in range(80, 100): print("withdrawing 80 rikos now..."); time.sleep(0.5); print("withdraw complete, check below you for your rikos")
        #Placing everything in a function comes in handy here
        while o2 == 101: main()
        while o2 == 102: print("card returned"); exit()
        print("you have", balance - o2, "rikos left"); main()
    #Depositing rikos
    if o == "3":
        print("how much you depositing sosu")
        o3 = int(input())
        print("deposited, your balance is now", balance + o3)
        exit()
    #Returning card
    if o == "9":
        print("adios my aubade")
        exit()
    #Incase they were a mong and didnt enter a number
    else:
        print("enter a valid number fool")
        main()
main()