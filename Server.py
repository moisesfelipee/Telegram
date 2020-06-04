import telepot
from telepot.loop import MessageLoop
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time


telebot = telepot.Bot("TOKEN")


class BOT(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # chrome_options.add_argument('--headless')
        self.driver = selenium.webdriver.Chrome(executable_path='C:\\Users\\moise\\Documents\\chromedriver',
                                                options=chrome_options)
        self.driver.create_options()
        self.driver.maximize_window()

        self.bot_url = 'SITE'
        self.driver.get(self.bot_url)

        time.sleep(8.3)

        login_box = self.driver.find_element_by_xpath('//*[@id="P101_USERNAME"]')
        login_box.send_keys('USER')

        time.sleep(3.1)

        pass_box = self.driver.find_element_by_xpath('//*[@id="P101_PASSWORD"]')
        pass_box.send_keys('SENHA')

        time.sleep(1.9)

        login_btn = self.driver.find_element_by_xpath('//*[@id="B12496999583886503"]')
        login_btn.click()

        time.sleep(7.4)

        self.driver.find_element_by_xpath('//*[@id="t_PageBody"]/div[3]/div[1]/button/span[1]').click()

    def handle(self, msg):
        msg_id = msg['from']['id']
        cpf = msg['text']

        self.driver.find_element_by_xpath('//*[@id="t_Header"]/div[1]/div[2]/a/img').click()

        try:
            ......
        except:
            pass

        # PESQUISA
        cpf_input = self.driver.find_element_by_xpath('//*[@id="P1_CPF_BENEFICIO"]')

        cpf_input.send_keys(cpf)

        print(f"Procurando {cpf}.")

        cpf_bt = self.driver.find_element_by_xpath('//*[@id="B5459261221811725"]/span[2]')
        cpf_bt.click()

        time.sleep(2)

        nome = self.driver.find_element_by_xpath('//*[@id="report_R5470892214811731"]/div/div[1]/table/tbody/tr/td[1]').text
        telebot.sendMessage(msg_id, "NOME: " + nome)

        ......

        time.sleep(2)


bot = BOT()

MessageLoop(telebot, bot.handle).run_as_thread()

while True:
    pass
