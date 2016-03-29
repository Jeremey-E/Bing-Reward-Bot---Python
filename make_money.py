from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import random
import keyring
from random_words import RandomWords

__service_name__ = 'bing_rewards_account'


def wait_after(func, wait_time=5):
    sleep(wait_time)


def perform_searches(driver, words, num_searches):
    wait_after(driver.get('https://login.live.com/'))
    driver.find_element_by_id('i0116').send_keys(sys.argv[1])
    driver.find_element_by_id('i0118').send_keys(keyring.get_password(__service_name__, sys.argv[1]))
    wait_after(driver.find_element_by_id('idSIButton9').click())
    wait_after(driver.get('http://www.bing.com'))

    for i in range(0, num_searches):
        wait_after(driver.find_element_by_id('sb_form_q').send_keys(words.get_random_word()), 2)
        wait_after(driver.find_element_by_id('sb_form_q').send_keys(Keys.ENTER), random.randrange(2, 10))
        driver.find_element_by_id('sb_form_q').clear()

    driver.close()


def main():
    if len(sys.argv) > 2:
        keyring.set_password(__service_name__, sys.argv[1], sys.argv[2])


    if len(sys.argv) < 2 or keyring.get_password(__service_name__, sys.argv[1]) is None:
        print('Please valid enter username and password!')
        return


    words = RandomWords()
    driver = webdriver.Firefox()
    perform_searches(driver, words, 30)
    # Sets the user agent string to an Android mobile device.
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36")
    driver = webdriver.Firefox(profile)
    perform_searches(driver, words, 20)

    print('Completed!')


if __name__ == "__main__":
    main()
