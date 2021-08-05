import requests
import time

import chromedriver_binary
from selenium import webdriver, common
from selenium.webdriver.chrome.options import Options


LINE_NOTIFY_TOKEN = 'LINE notify token is here'
LINE_NOTIFY_API = 'https://notify-api.line.me/api/notify'


class ConnectWeb():
    
    def __init__(self, url: str, user_id: str, password: str) -> None:
        """
        Class initialization

        Args:
            user_id (str): User ID number to log in to Kubota.
            password: (str): Password to log in Kubota.
        """
        
        self.url = url
        self.user_id = user_id
        self.password = password
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)

    def fetch_page(self):
        try:
            browser = self.browser
            browser.get(self.url)

        except common.exceptions.TimeoutException():
            print('Time out')
            return '';

    def login(self):
        browser = self.browser
        browser.find_element_by_name('userid').send_keys(self.user_id)
        browser.find_element_by_name('password').send_keys(self.password)
        browser.find_element_by_class_name('btn-lg').click()
        browser.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/ul[1]/li[1]/a').click()
        # browser.get('get user summer intern page')
    
    def check(self):
        """
        Returns:
            result (bool): if schedule is full return False,
                           else return true.
        """
        browser = self.browser
        schedules = browser.find_elements_by_class_name('schedule')
        for i in range(len(schedules)):
            if '満席' in schedules[i].text:
                return False
            else:
                return True
    
    def send_line_notify(self, notification_message: str) -> None:
        """
        Args:
            notification_message (str): Message to send to LINE.
        """
        headers = {'Authorization': "Bearer " + LINE_NOTIFY_TOKEN}
        data = {"message": notification_message}
        requests.post(LINE_NOTIFY_API, headers=headers, data=data)

    def __exit__(self):
        """
        Terminate the connection.
        """
        print('del: browser...')
        self.browser.quit()
        

if __name__ == '__main__':
    connect = ConnectWeb('https://www.e2r.jp/ja/kubota2023/', 'user_id', 'password')
    connect.fetch_page()
    connect.login()
    result = connect.check()
    if result:
        connect.send_line_notify('空席ができました。')
    connect.__exit__()

