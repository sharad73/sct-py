#!/usr/bin/python2.7
# The purpose of the script is to get the desired data from the defined url
#Install BeautifulSoup4 before import. cmd pip install BeautifulSoup4.
#import libraries
import urllib2
import csv
import time
from datetime import datetime

from bs4 import BeautifulSoup

#b_42 company_name, id=Bse_prc_tick

# Specify the url. To get multiple indices modify quote_page into an list of URLs.
quote_page = ['http://www.moneycontrol.com/india/stockpricequote/steel-tubes-pipes/aplapollotubes/BT09',
              'http://www.moneycontrol.com/india/stockpricequote/plastics/arrowgreentech/ACP',
              'http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/axisbank/AB16',
              'http://www.moneycontrol.com/india/stockpricequote/finance-investments/bajajholdingsinvestment/BHI',
              'http://www.moneycontrol.com/india/stockpricequote/infrastructure-general/bharatheavyelectricals/BHE',
              'http://www.moneycontrol.com/india/stockpricequote/dyes-pigments/bodalchemicals/BC15',
              'http://www.moneycontrol.com/india/stockpricequote/finance-investments/centraldepositoryservicesltd/CDS',
              'http://www.moneycontrol.com/india/stockpricequote/banks-public-sector/corporationbank/CB',
              'http://www.moneycontrol.com/india/stockpricequote/media-entertainment/galaxyentertainment/GE04',
              'http://www.moneycontrol.com/india/stockpricequote/diversified/generalinsurancecorporationindia/GIC12',
              'http://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/glenmarkpharma/GP08',
              'http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01',
              'http://www.moneycontrol.com/india/stockpricequote/plastics/innovativetechpack/ITP',
              'http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/karnatakabank/KB04',
              'http://www.moneycontrol.com/india/stockpricequote/infrastructure-general/larsentoubro/LT',
              'http://www.moneycontrol.com/india/stockpricequote/consumer-goods-white-goods/leel/LEE',
              'http://www.moneycontrol.com/india/stockpricequote/power-generation-distribution/nhpc/N07',
              'http://www.moneycontrol.com/india/stockpricequote/mining-minerals/nmdc/NMD02',
              'http://www.moneycontrol.com/india/stockpricequote/power-generation-distribution/nlcindia/NLC',
              'http://www.moneycontrol.com/india/stockpricequote/power-generation-distribution/ntpc/NTP',
              'http://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI',
              'http://www.moneycontrol.com/india/stockpricequote/cement-products-building-materials/sanghiindustries/SI04',
              'http://www.moneycontrol.com/india/stockpricequote/diversified/sintexindustries/SI27',
              'http://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS',
              'http://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI',
              'http://www.moneycontrol.com/india/stockpricequote/computers-software-medium-small/vakrangee/VS',
              'http://www.moneycontrol.com/india/stockpricequote/infrastructure-general/vatechwabag/VTW']
#for loop data
data = []
#query the url and return the html to variable 'page'. For loop which will process url one by one and store all the data in to variable data in tuples.

for pg in quote_page:
    page = urllib2.urlopen(pg)

    #parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    #Take out the <div> of the name and get its value
    name_box = soup.find('h1', attrs={'class':'b_42 company_name'})

    #After we have the tag, we can get the data by getting its text
    name = name_box.text.strip() #strip() is used to remove starting and trailing

    #get the index price
    price_box = soup.find('span', attrs={'id':'Bse_Prc_tick'})
    if price_box is None:                                           #If company does not trade in BSE, check the price in NSE
        price_box = soup.find('span', attrs={'id':'Nse_Prc_tick'})
    #After we have the tag we can get the data by getting its text
    price = price_box.text.strip()
    #print name.ljust(40), price.rjust(8)

    #Save the data in tuple
    data.append((name,price))
 
###for x in data:
###print data[]
###open a csv file with append, so old data will not be erased
with open('index.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for name,price in data:    
        writer.writerow([name.ljust(40),price.rjust(8),datetime.now().strftime("%d%b%y")]) # %b will print month in abbriviated form e.g. Oct
        #print name,price
