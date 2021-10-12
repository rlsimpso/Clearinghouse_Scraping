from selenium import webdriver
import time
import pandas as pd

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

web_address = 'https://wbl.futurereadyiowa.gov/business-partners?fbclid=IwAR1fME1l8qs5f9gTZCZFP7sutKEibSEEifGA19Yh7Sm782tDtetEzDvz4Zk'
driver.get(web_address)

time.sleep(2)
all_links = driver.find_elements_by_css_selector('.name_link a')
all_names = driver.find_elements_by_css_selector('.name_link a')

next_page = driver.find_element_by_id('returns_next')
link_text = []
links = []

for n in range(0, 15):
    for n in range(len(all_links)):
        all_links = driver.find_elements_by_css_selector('.name_link a')
        all_names = driver.find_elements_by_css_selector('.name_link a')
        link = all_links[n].get_attribute('href')
        links.append(link)
        name = all_names[n].text
        link_text.append(name)
        next_page = driver.find_element_by_id('returns_next')

    next_page.click()
    time.sleep(2)


print(links)
print(link_text)


dict = {
    'Name': link_text,
    'URL': links
}
df = pd.DataFrame(dict)

df.to_csv('aaron_2.csv')


driver.quit()
