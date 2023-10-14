from bs4 import BeautifulSoup
import time
import pandas as pd


START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

scarped_data = []

def scrape():
    
    soup = BeautifulSoup(browser.page_source, "html.parser")


    #VERY IMP: The class "wikitable" and < tr> data is at the time of creation of this code. 
    # This may be updated in future as the page is maintained by Wikipedia. 
    # Understand the page structure as discussed in the class & perform Web Scraping from scratch.

    bright_star_table = soup.find("table",attrs={"class","wikitable"})

    table_body = bright_star_table.find("tbody")

    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        print(table_cols)

        temp_list = []
    
    for col_data in table_cols:
        print(col_data.text)

        data = col_data.text.strip()
        print(data)

        temp_list.append(data)

    scarped_data.append(temp_list)

    stars_data = []

    for i in range(0,len(scarped_data)):
        
        Star_names = scarped_data[i][1]
        Distance = scarped_data[i][3]
        Mass = scarped_data[i][5]
        Radius = scarped_data[i][6]
        Lum = scarped_data[i][7]

        required_data = [Star_names,Distance,Mass,Radius,Lum]
        stars_data.append(required_data)

        headers = ['Star_name','Distance','Mass','Radius','Luminosity']

        star_df_1 = pd.DataFrame(stars_data,columns=headers)

        star_df_1.to_csv("scraped_data.csv",index=True,index_label="id")


    



