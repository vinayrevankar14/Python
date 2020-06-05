'''
#1.	Write python program to perform bank operations using class and objects.
Conditions:
a.	Bank name should be static.
b.	Using menu driven program.
1 .Deposit
2. Withdraw
3. Exit
'''
import sys
class Bank:
    BankName = 'Bank of India'
    def __init__(self, name, accountno, balance=1000):
        self.name = name
        self.accountno = accountno
        self.balance = balance
        print('\nName:{}\nAccount no:{}\nBalannce:{}'.format(name,accountno,balance))

    def deposit(self, amount):
        self.balance += amount
        print('Total current amount in your account: {} rupees'.format(self.balance,'.2f'))

    def withdraw(self, amount):
        if self.balance < amount:
            print('Cannot withdraw the amount you entered as you have {} rupees in your account'.format(self.balance,'.2f'))
            sys.exit()
        self.balance -= amount
        print('Amount of {} rupees has been successfully withdrawn and availabel balance is {} rupees'.format(amount,self.balance))

print('Welcome to %s'%(Bank.BankName))
name = input('Please enter your name:')
acc = int(input('Account number:'))
b = Bank(name,acc)
while True:
    print('\n%s please enter the options to do the following\n1.Deposit\n2.Withdraw\n3.Exit'%(name))
    n = int(input('\nEnter the option number:'))

    if n==1:
        a = float(input('Enter the amount to deposit:\n'))
        b.deposit(a)
    elif n==2:
        x = float(input('Enter the amount to withdraw:\n'))
        b.withdraw(x)
    elif n==3:
        print('\nThank you %s for using the service visit again :)'%(name))
        break
    else:
        print('\nInvalid option choose out of three available options')