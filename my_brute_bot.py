from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from time import sleep

## This is run.py for my "mybrute.com" bot
keyboard = Controller()
driver = webdriver.Chrome()

# Let's define what a user is
class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def format_name(name):
    return name.replace(' ', '-')

# Let's make a list of users
list_of_users = [
    # enter a list of different brute like this 
    # user('username', 'password'),
    # user('username1', 'password') 
]

class mybrutebot:
    def __init__(self, user 
    ):
        self.username = user.username
        self.password = user.password
        self.driver = driver

    def create_new_brute(self):
        driver.get("http://www.mybrute.com")
        driver.find_element_by_id('swf_create_form').click()
        keyboard.press(Key.tab)
        keyboard.send_keys(self.username)
        keyboard.send_keys(Key.enter)
        sleep(1)

        self.define_password()

    def define_password(self):
        username = format_name(self.username)
        driver.get('http://' + username + '.mybrute.com/setPass')
        # find the password box
        password_box = driver.find_element_by_name('pass')
        password_box.clear()
        password_box.send_keys(self.password)
        # find the confirmation box
        password_box = driver.find_element_by_name('pass2')
        password_box.clear()
        password_box.send_keys(self.set_password)
        password_box.send_keys(Keys.RETURN)
        sleep(1)

    def cellule(self):
        driver = self.driver
        driver.get("http://" + self.username + ".mybrute.com/cellule")
        sleep(1)

    def login(self):
        driver = self.driver
        username = self.username
        driver.get('http://' + username + '.mybrute.com/login')
        # find the password and fill it in
        password_box = driver.find_element_by_name('pass')
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        sleep(1)
        
    def fight_new_opponents(self, number_of_fights=1):
        opponents = self.find_opponents(number_of_opponents=number_of_fights)
        for opponent in opponents:
            self.fight(opponent_name=opponent)
        

    def find_opponents(self, number_of_opponents=1):
        # load the fight page
        driver = self.driver
        driver.get('http://' + self.username + '.mybrute.com/arene')
        sleep(1)
        # get the opponents (maximum 6 names at once)
        opponent_elems = driver.find_elements_by_class_name('name')
        opponent_names = list()
        for i in range(0, number_of_opponents):
            opponent_names.append(opponent_elems[i].text)
        print(opponent_names)
        return opponent_names

    def fight(self, opponent_name=''):
        # in case there are spaces in the opponent's name
        opponent_name = format_name(opponent_name)
        # get the fight page
        driver = self.driver
        username = self.username
        to_open_href = f'http://{username}.mybrute.com/vs/{opponent_name}'
        driver.get(to_open_href)
        sleep(1)
        # click the update flash button
        try:
            update_button = driver.find_element_by_xpath('//a[@href="http://get.adobe.com/flashplayer/"]')
            update_button.click()
            print('found the flash button')
            # allow flash plugins
            sleep(1)
            keyboard.press(Key.tab)
            keyboard.press(Key.enter)
        except:
            print('There was no flash button')
            pass
        sleep(1)
        # click the fight button
        try:
            fight_button_elem = driver.find_element_by_id('btn')
            fight_button_elem.click()   # this 'plays' the button (flash plugin bug)
            fight_button_elem.click()   # this should click the button
        except:
            print('failed to press the fight')

for user in list_of_users:
    Bot = mybrutebot(user)
    Bot.login()
    try:
        Bot.fight_new_opponents(3)
        sleep(2)
    except Exception as e:
        print(Bot.username, 'can no longer fight :', e)
        print('')