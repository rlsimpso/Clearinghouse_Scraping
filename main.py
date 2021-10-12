from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd

# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9"
# }
#
# response = requests.get("https://wbl.futurereadyiowa.gov/business-partners?fbclid=IwAR1fME1l8qs5f9gTZCZFP7sutKEibSEEifGA19Yh7Sm782tDtetEzDvz4Zk", headers=header)
#
# webpage = response.text
#
# soup = BeautifulSoup(webpage, 'html.parser')
#
# all_links = soup.select('.name_link')
#
# print(all_links)

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

web_address = 'https://wbl.futurereadyiowa.gov/business-partners?fbclid=IwAR1fME1l8qs5f9gTZCZFP7sutKEibSEEifGA19Yh7Sm782tDtetEzDvz4Zk'
driver.get(web_address)

time.sleep(2)
all_links = driver.find_elements_by_css_selector('.name_link a')

links = []
for n in range(len(all_links)):
    # time.sleep(1)
    link = all_links[n].get_attribute('href')
    links.append(link)


print(links)



dict = {'URL': links}

df = pd.DataFrame(dict)

df.to_csv('aaron.csv')




driver.quit()