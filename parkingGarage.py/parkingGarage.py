# <-----------------Heathers Section---------->
class parkingGarage():
    def __init__(self, availibity=3, currentTicket= False):
        self.parkingSpaces= availibity
        self.tickets= availibity
        self.currentTicket =currentTicket

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
# standard = parkingGarage(3,3,False)        

garageAvailibity = parkingGarage()

garageAvailibity.takeTicket()
garageAvailibity.takeTicket()
garageAvailibity.takeTicket()





# <-----------------End of Heathers Section---------->
# <-----------------Jesses Section---------->




















# <-----------------End of Jesses Section---------->
# <-----------------Peters Section---------->




















# <-----------------End of Peters Section---------->