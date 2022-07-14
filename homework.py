import requests, json
from colorama import Fore, Style
from pyfiglet import figlet_format

class Bored():
    def __init__(self):
        self.url = 'http://www.boredapi.com/api/activity?'

    def search_by_type(self):
        preference = input('Please select an activity type: recreational, relaxation, social, busywork, education, cooking, charity, music, or diy:\n')
        mod_search = self.url + 'type=' + preference
        response = requests.get(mod_search)
        data = response.json()
        self.results(data)

    def search_by_participants(self):
        preference = input('Please select how many participants. Number must be between 1-5:\n')
        mod_search = self.url + 'participants=' + preference
        response = requests.get(mod_search)
        data = response.json()
        self.results(data)      

    def search_by_price(self):
        minimum_price = input('Activity cost minimum_price: \n')
        maximum_price = input('Activity cost maximum_price: \n')
        mod_search = self.url + 'minprice=' + minimum_price + '&maxprice=' + maximum_price
        response = requests.get(mod_search)
        data = response.json()
        self.results(data)
        
    def results(self, data):
        self.activity = data['activity']
        self.type = data['type']
        self.participants = data['participants']
        self.price = data['price']
        self.link = data['link']
        self.key = data['key']
        self.accessibility = data['accessibility']
        
        print('*****************************************************')
        print(figlet_format('BORED API'))
        print('*****************************************************')
        print(Fore.BLUE, Style.BRIGHT, 'Activity: ' + self.activity, Style.RESET_ALL)
        print(Fore.RED, Style.BRIGHT, 'Type: ' + self.type, Style.RESET_ALL)
        print(Fore.YELLOW, Style.BRIGHT, 'Participants: ' + str(self.participants), Style.RESET_ALL)
        print(Fore.GREEN, Style.BRIGHT, 'Price: ' + str(self.price), Style.RESET_ALL)
        print('*****************************************************')


class User_prompt():
    bored = Bored()

    @classmethod
    def main(cls):
        while True:
            welcome = input("""Welcomee to BoredAPI where we'll find you something to do! How would you like to filter results? 
        Just input: 'type', 'participants', 'price' or 'quit: \n""")
            if welcome.lower() == 'quit':
                break
            elif welcome.lower() == 'type':
                cls.bored.search_by_type()
            elif welcome.lower() == 'participants':
                cls.bored.search_by_participants()
            elif welcome.lower() == 'price':
                cls.bored.search_by_price()
            else:
                print('Invalid input, try again!')
                           

if __name__ == "__main__":
    User_prompt.main()
    