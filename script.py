import pandas as pd
import webbrowser

from selenium import webdriver
import time

import re
import random

import requests
import json

from inputs import *

url = 'https://colonist.io/?#'

driver = webdriver.Chrome('{}'.format(driver)) #in inputs file
driver.get("{}".format(url))
start_game_button = driver.find_element_by_class_name('btn_create')

print('page is loading')
time.sleep(15)


print('entering the game')
start_game_button.send_keys("\n")


time.sleep(5)

print('this is the game id')
print(driver.current_url)
game_url = driver.current_url

print('making the game private')
private_game_button = driver.find_element_by_id('room_center_checkbox_privategame')
time.sleep(3)
private_game_button.click()
print('made the game private')

### send to slack
slack_bot_url = '{}'.format(slack_bot) # in inputs file
text_array = ["Here's the link", "Sheep ports only!", "I'm going fishing boys!"]
random_int = random.randint(0,len(text_array)-1)
game_link = "<{0}|{1}>".format(game_url, text_array[random_int])
message = {
    "text": "{0}".format(game_link)
}

message_json = json.dumps(message)
print('Sending message to slack!')
slack_message = requests.post(url=slack_bot_url, json=message)
print(slack_message.status_code)
print(slack_message.text)
print('Sent message to Catan!')


#getting how many users are in the game
users_in_game = driver.find_element_by_id('lobby_userlist_header')
users_in_game_text = users_in_game.text
int_players_in_game = int(re.search(r'\d+', users_in_game_text).group())
i = 0
#while player count is less than one, stay as the leader for 2 minutes - after that end the game.
while int_players_in_game <= 1:
    time.sleep(2)
    users_in_game_loop = driver.find_element_by_id('lobby_userlist_header')
    users_in_game_text_loop = users_in_game_loop.text
    int_players_in_game = int(re.search(r'\d+', users_in_game_text_loop).group())
    i = i + 1
    if i == 60:
        print('No-one has entered the game. Shutting it down.')
        break



print('leaving the game')

#this quits the game, which transfers the ownership of the room to the next user, or kills the lobby
time.sleep(2)
driver.quit()
