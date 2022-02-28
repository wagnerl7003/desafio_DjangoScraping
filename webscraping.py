from msilib.schema import tables
from unittest import result
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup as bs
import db


def LimpandoStr(mystr, palavra1, palavra2, addloc2):
    loc1 = mystr.find(palavra1)
    loc2 = mystr.find(palavra2)
    loc2 += addloc2
    campoexcluir = mystr[loc1:loc2]
    mystr = mystr.replace(campoexcluir, '')

    return mystr

def Coletando(mydriver):

    soup = bs(mydriver.page_source, 'html.parser')

    for tablesite in soup.find_all("tr", attrs={"class": ["Odd", "Even"]}):

        mytable = []

        adsense = tablesite.find("ins", attrs={"class": "adsbygoogle"})

        print(adsense)

        if adsense == None:

            for table_result in tablesite:

                isbar = table_result.find("span", class_="bar")

                if isbar != None :
                    bar = table_result.find("span", attrs={"class": "bar"}).get('style')
                    bar = LimpandoStr(bar, 'w', ':', 1)
                    bar = LimpandoStr(bar, '%', ':', 1)
                    bar = LimpandoStr(bar, '#', ';', 1)

                    mytable.append(bar)

                else :
                    myresult = table_result.text


                    if myresult == '':
                        myresult = "None"
                    
                    myresult = myresult.replace('%', '')

                    mytable.append(myresult)

            mytable = str(mytable)
            mytable = mytable.replace('[', '')
            mytable = mytable.replace(']', '')
            print(mytable)
            db.InsertSqlite(mytable)
            
        print('-------------------\n\n')
    

options = Options()
options.add_argument("-headless")

driver = webdriver.Chrome("chromedriver.exe", options=options)

driver.get("https://www.freeproxylists.net/")

while_check = 0
page = 1

soup = bs(driver.page_source, 'html.parser')

page = soup.find("div", attrs={"class": "page"}) #.a.string
print(page.find_all("a"))
page_a = page.find_all("a")

for allpage in page_a:
    valuepage = allpage.text
    print(valuepage)

    if valuepage != 'Next »':
        lastpage = int(valuepage)

    
print(lastpage)

n_while = 0

nextpage = 2

Coletando(driver)

while n_while < 1:

    if nextpage <= lastpage:
        driver.get("https://www.freeproxylists.net/?page="+str(nextpage))
        nextpage += 1
        Coletando(driver)
    else:
        n_while = 1
        break


driver.quit()
