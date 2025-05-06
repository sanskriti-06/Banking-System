
import time
import pandas as pd
import os

def new1():
    print("\n*** New User Registration ***")
    name=(input("Enter your full name:")).capitalize()
    if not os.path.exists('customer.xlsx'):
        df = pd.DataFrame(columns=['NAME', 'PASSWORD','BALANCE'])
        df.to_excel('customer.xlsx', index=False)
    while True:
        pas=input("Set your password of 6 digit:")
        if len(pas)!=6 or not pas.isdigit() :
            print("invalid password,try again")
        else:
            break
    df=pd.read_excel('customer.xlsx')
    new_row=pd.DataFrame([{'NAME':name,'PASSWORD':int(pas),'BALANCE':0}])
    df=pd.concat([df,new_row],ignore_index=True)
    df.to_excel('customer.xlsx',index=False)
    print("\nRegistration Successful!")
    print(f"Welcome, {name}!\n")
    return name,pas,0
def login():
    print("\n*** Login ***")
    name=(input("Enter your name:")).capitalize()
    try:
        pas=int(input("Enter your password:"))
    except ValueError:
        print("\nError! please write numeric value")
        return False
    try:
        df = pd.read_excel('customer.xlsx')
    except FileNotFoundError:
        print("\nError: Customer database file not found!")
        return False
    true_pass=df.loc[df["NAME"]==name,"PASSWORD"].values
    if true_pass.size==0 :
        print("\nYou are not registered yet......")
        try:
            ch=(input("Would you like to register(yes / no ):")).lower()
            if ch=="yes":
                 name,pas,c=new1()
                 banking_operation(name,pas,c)
            else:
                print("THANK YOU...")
                return False
        except ValueError:
            print("\nInvalid input")
    elif pas!=true_pass[0]:
            print("\nWrong password, try again")
            return False
    else:
        c=df.loc[(df["NAME"]==name) &(df["PASSWORD"]==pas),"BALANCE"].values[0]
        if pd.isna(c):
            c=0
        print("\nLogin Successful!")
        print(f"Welcome back, {name}!\n")
        return name,pas,c
def banking_operation(name, pas, c):
    while True:
            print("\n*** Banking Operations ***")
            print("1.Withdraw\n2.Deposit\n3.Check Balance\n4.Exit")
            try:
                ch = int(input("\nSelect one of the options (1-4): "))
            except ValueError:
                print("\nInvalid input! Please select a number between 1 and 4.")
                continue
            if ch==1:
                try:
                    wit=int(input("\nEnter amount to withdraw:"))
                    if c<wit:
                        print("\nInsufficient balance.\n")
                    else:
                        c-=wit
                        print("\nWithdrawal Successful!")
                        print(f"Remaining Balance: {c}\n")
                except ValueError:
                    print("\nInvalid input! Please enter a numeric amount.")
            elif ch==2:
                try:
                    dep=int(input("\nEnter amount to deposit:"))
                    c+=dep
                    print("\nDeposit Successful!")
                    print(f"Updated Balance: {c}\n")
                except ValueError:
                    print("\nInvalid input! Please enter a numeric amount.")
            elif ch==3:
                print(f"your total balance = {c}")
            elif ch==4:
                 print("\nThank you for using the banking system. Goodbye!\n")
                 break
            else:
                print("\nInvalid choice! Please select a valid option.\n")
            df=pd.read_excel('customer.xlsx')
            df.loc[(df["NAME"]==name)&(df["PASSWORD"]==pas),"BALANCE"]=float(c)
            df.to_excel('customer.xlsx',index=False)
print("\t\tWELCOME TO OUR BANKING SYSTEM")
for i in range(7):
    print("\t*",end="")
    time.sleep(0.3)
new=(input("\nAre you new here(yes/no):")).lower()
if new=="yes":
    name,pas,c=new1()
    banking_operation(name,pas,c)
elif new=="no":
    login_data=login()
    if login_data:
        name,pas,c=login_data
        banking_operation(name,pas,c)
else:
    print("\nInvalid option! Exiting.....")
         
                
                
       
                
        
        
    
    

