import requests
import time

import chromedriver_binary
from selenium import webdriver, common
from selenium.webdriver.chrome.options import Options



LINE_NOTIFY_TOKEN = 'lLgySNv2xbgAxfyub1vDtqNWsG30UfqYmVi47GWbDzF'
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
            print(browser.title)
            print('get browser')

        except common.exceptions.TimeoutException():
            print('Time out')
            return '';

    def login(self):
        browser = self.browser
        browser.find_element_by_name('userid').send_keys(self.user_id)
        browser.find_element_by_name('password').send_keys(self.password)
        browser.find_element_by_class_name('btn-lg').click()
        title = browser.title
        browser.get('https://www.e2r.jp/eARTH/e2r/user/pageset/Pageset?deliverID=79&pageID=40')
        print(title)
    
    def check(self):
        browser = self.browser
        schedules = browser.find_elements_by_class_name('schedule')
        for i in range(len(schedules)):
            if '満席' in schedules[i].text:
                return False
            else:
                return True
    
    def send_line_notify(self, notification_message):
        # notification_message = '空席ができました。'
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
    connect = ConnectWeb('https://www.e2r.jp/ja/kubota2023/', 'kb153376', 'basuke811')
    connect.fetch_page()
    connect.login()
    result = connect.check()
    if result:
        connect.send_line_notify('空席ができました。')
    connect.__exit__()

