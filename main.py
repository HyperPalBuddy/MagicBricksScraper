# import packages
from csv import *
from bs4 import BeautifulSoup
import requests

"""
Data Info
mainList  ->    divClass=mb-srp__list   
title     ->    h2Class=mb-srp__card--title
totalCost ->    divClass=mb-srp__card__price--amount
area      ->    divClass=mb-srp__card__summary--value   

"""


def getURL(choice, city, local="N/A"):
    if choice == "1":
        url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=" + city + "&page=1&sortBy=premiumRecent&postedSince=-1&isNRI=N"
    elif choice == "2":
        url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&Locality=" + local + "&cityName=" + city
    return url


print("How Do You Want To Search: \n 1:By City\n 2:By Locality")

how = input()
try:
    if how == "1":
        city = input("Enter City:")
        url = getURL(how, city)
    elif how == "2":
        locality = input('Enter Locality:')
        city = input("Enter City:")
        url = getURL(how, city, locality)
    else:
        raise Exception("Incorrect Search Option")
except Exception as e:
    print(e)
else:
    print("URL:"+url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("div", class_="mb-srp__list")

    with open('sales.csv', 'w', encoding='utf8',newline='') as f:
       write = writer(f)
       header = ["Title","Area","Cost"]
       write.writerow(header)
       for result in results:
           title = result.find('h2', class_="mb-srp__card--title").text
           area = result.find('div', class_="mb-srp__card__summary--value").text
           totalCost = result.find("div", class_="mb-srp__card__price--amount").text
           totalCost = totalCost[1:]
           write.writerow([title, area, totalCost])



