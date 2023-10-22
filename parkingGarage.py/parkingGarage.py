# <-----------------Heathers Section---------->
class parkingGarage():
    def __init__(self, availability = 100, currentTicket = False):
        self.parkingSpaces = availability
        self.tickets = availability
        self.currentTicket = currentTicket

    def takeTicket(self):
        userPark = input('Would you like to park your car? ').lower()
        self.parkingSpaces = 100
        while True:
            if userPark == 'yes' and {self.parkingSpaces} != 0:
                print( 'Please take your ticket ')
                self.parkingSpaces -= 1
                self.tickets -= 1
                break
            elif userPark == 'no':
                print( 'Please use the left lane to exit.')
                break
            elif parkingGarage.parkingSpaces == 0:
                print( 'There are no more spaces available, please use the left lane to exit.')
        
        print(f'The available spaces are: {self.parkingSpaces} available. ')
        print(f'The available tickets are: {self.tickets} available. ')
# <-----------------End of Heathers Section----------> 
# <-----------------Jesses Section---------->
    def payForParking(self):
        while True:
            payment = (input('Please pay $15.  Would you like to pay now?  "Yes" or "No" ')).lower()
            if payment == 'yes':
                self.currentTicket = True
                print('Your ticket has been paid.  You have 15 minutes to exit the parking garage. ') 
                break  
            elif payment == 'no':
                print('When ready, please pay ticket to exit the parking garage. ')
                break
# <-----------------End of Jesses Section---------->
# <-----------------Peters Section---------->
    def leaveGarage(self):
        while True:
            if self.currentTicket == True:
                print('Thank you, have a nice day!')
                self.parkingSpaces += 1
                self.tickets += 1
                self.currentTicket = False
                break
            elif self.currentTicket == False:
                print('Please pay your ticket to exit the parking garage.')
                parking_garage.runner()
                break

        print(f'The available spaces are: {self.parkingSpaces} available. ')
        print(f'The available tickets are: {self.tickets} available. ')      
# <-----------------End of Peters Section---------->
    def runner(self):
        while True:
            action = input('What action are you taking?  Type "enter" to enter the garage.  Type "pay" to pay for your ticket.  Type "exit" to exit the parking garage. Type "quit" to quit. ').lower()
            if action == 'enter':
                parking_garage.takeTicket()
            elif action == 'pay':
                parking_garage.payForParking()
            elif action == 'exit':
                parking_garage.leaveGarage()
                break
            else:
                break

parking_garage = parkingGarage()
parking_garage.runner()