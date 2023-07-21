class Atm():

    #Static Variable
    __counter = 1

    # constructor
    def __init__(self):
        self.pin = ''
        self.__balance = 5000
        Atm.__counter = Atm.__counter + 1
        self.menu()

    def get_balance(self):
        return self.__balance
    def set_balance(self, new_value):
        self.__balance = new_value
    
    # utility function jisko method ki zarurat nh h
    @staticmethod
    def get_counter(self):
        return Atm.__counter


    def menu(self):        
        user_input = input('''
            Hello! how may I help you?
            
              1 - Press 1 to Generate Pin
              2 - Press 2 to Change Pin
              3 - Press 3 to Check Balance
              4 - Press 4 to Withdraw Amount
              5 - Anything else to Exit
        ''')

        if user_input == '1':
            self.generate_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw_amount()
        else:
            exit()

    # generate pin
    def generate_pin(self):
        user_pin = input('Enter your pin: ')
        self.pin = user_pin

        print('pin created successfully...')
        self.menu()

    def change_pin(self):
        old_pin = input('Enter your old pin: ')
        if old_pin == self.pin:
            new_pin = input('Enter new pin: ')
            self.pin = new_pin
            
            print('pin changed successfully...')
            self.menu()
        else:
            print("you've entered wrong input...")
            self.menu()

    def check_balance(self):
        pin = input('Enter your pin: ')
        if pin == self.pin:
            print(f'your current balance is {self.__balance}')
            self.menu()
        else:
            print("you've entered wrong pin...")
            self.menu()

    def withdraw_amount(self):
        pin = input('Enter your pin: ')
        if pin == self.pin:
            amount = int(input('Enter amount: '))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print(f'Transaction successful! your balance is Rs.{self.__balance}')
            else:
                print("You don't have suffiecient amount")
            self.menu()
        else:
            print("you've entered wrong pin...")
            self.menu()

obj = Atm()

