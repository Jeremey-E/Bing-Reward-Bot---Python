__author__ = 'Jeremey Ebenezer'

# words.txt from http://www-01.sil.org/linguistics/wordlists/english/

from selenium import webdriver
from time import sleep
import random
import sys
from random_words import RandomWords

def wait(func, wait_time=5):
    sleep(wait_time)


def main():
    if len(sys.argv) < 3:
        print('Enter username and password!')
        return

    words = RandomWords()
    driver = webdriver.Firefox()
    wait(driver.get('http://www.bing.com'))
    wait(driver.find_element_by_id('id_l').click(), 2)
    wait(driver.find_element_by_class_name('id_link_text').click(), 5)
    driver.find_element_by_id('i0116').send_keys(sys.argv[1])
    driver.find_element_by_id('i0118').send_keys(sys.argv[2])
    wait(driver.find_element_by_id('idSIButton9').click(), 5)
    for i in range(0, 30):
        wait(driver.find_element_by_id('sb_form_q').send_keys(words.get_random_word()))
        wait(driver.find_element_by_id('sb_form_go').click(), random.randrange(3, 10))

if __name__ == "__main__":
    main()
