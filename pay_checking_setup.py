from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

os.popen('"chromium-browser" --user-data-dir=/home/pi/Desktop/NPPayCheck --remote-debugging-port=8989')

tk = "/home/pi/Desktop/NPPayCheck"

op = webdriver.ChromeOptions()
op.add_experimental_option('debuggerAddress', 'localhost:8989')
op.add_argument("user-data-dir=" + tk)
service = Service('/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service = service, options = op)
