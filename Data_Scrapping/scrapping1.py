from selenium import webdriver
from selenium.driver.common.by import by
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://exoplants.nasa.gov/exoplanet-catalog/"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
planets_data=[]

def scrape():
    for i in range(0, 10):
        print(f'scrapping page (i+1)')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs=("class", "exoplanet")):
            li_tags = ul_tag.find_all("li")
            for index, li_tag in enumerate(li_tags):
                temp_list=[]
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.content[0])
                    except:
                        temp_list.append("")
                planets_data.append(temp_list)
            browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
scrape()

headers=["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_data"]

planet_df_1 = pd.DataFrame(planets_data, columns=headers)

planet_df_1.to_csv('scraped_data.csv', index=True, index_label="id")