from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os.path
import sys
import random
import keyring

from random_words import RandomWords

__service_name__ = 'bing_rewards_account'


def wait_after(func, wait_time=5):
    sleep(wait_time)


def perform_searches(username, driver, words, num_searches):
    wait_after(driver.get('https://login.live.com/'))
    driver.find_element_by_id('i0116').send_keys(username)
    driver.find_element_by_id('i0118').send_keys(keyring.get_password(__service_name__, username))
    wait_after(driver.find_element_by_id('idSIButton9').click())
    wait_after(driver.get('http://www.bing.com'))

    for i in range(0, num_searches):
        wait_after(driver.find_element_by_id('sb_form_q').send_keys(words.get_random_phrase()), 2)
        wait_after(driver.find_element_by_id('sb_form_q').send_keys(Keys.ENTER), random.randrange(2, 15))
        driver.find_element_by_id('sb_form_q').clear()

    driver.close()


def main():
    if len(sys.argv) > 2:
        keyring.set_password(__service_name__, sys.argv[1], sys.argv[2])
        with open('bing_rewards_user.txt', 'w') as f:
            f.write(sys.argv[1])

    if os.path.isfile('bing_rewards_user.txt'):
        with open('bing_rewards_user.txt') as f:
            username = f.read()
        if keyring.get_password(__service_name__, username) is None:
            print('Please enter enter username and password!\n'
                  'make_money [username] [password]')
            return
    else:
        print('Please enter valid username and password!\n'
              'make_money [username] [password]')
        return

    words = RandomWords()
    driver = webdriver.Firefox()
    perform_searches(username, driver, words, 15)
    # Sets the user agent string to an Android mobile device.
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36")
    driver = webdriver.Firefox(profile)
    perform_searches(username, driver, words, 5)

    print('Completed!')


if __name__ == "__main__":
    main()
