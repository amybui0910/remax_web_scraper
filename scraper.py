from bs4 import BeautifulSoup
from csv import writer
import re
import requests

def main():
    # search for city and type of real estate to look for
    place = input('City to search: ').lower()
    search_type = input('Searching for (sale/rent): ').strip().lower()

    while search_type not in ['sale', 'rent']: 
        search_type = input('Please put \'sale\' or \'rent\': ')
        
    if search_type == 'sale': 
        type = 'false'
    else: 
        type = 'true'
        
    # read remax web pages
    params = {'pageNumber': '1', 'rentalsOnly': type}
    url = 'https://www.remax.ca/on/'+ place + '-real-estate'
    page = requests.get(url, params=params)
    soup = BeautifulSoup(page.content, 'lxml')
    lists = soup.find_all('a', attrs={'data-cy': 'listing-card'})

    # go through web pages and write to csv file
    with open(place + '_' + search_type + '_search_results.csv', 'w', encoding='utf8', newline='') as f: 
        # csv file header
        file_writer = writer(f)
        header = ['Location', 'Property_Type', 'Price_Listing', 'Property_Sqft', 'Property_Tax', 'Bed', 'Bath']
        file_writer.writerow(header)
        
        # go through web pages until no results appear
        while True: 
            for list in lists: 
                if list != None: 
                    # find address
                    address = list.find('div', attrs={'data-cy': 'property-address'})
                    location = ''
                    for span in address.find_all('span'): 
                        location += span.get_text()
                        
                    #find price listing of property
                    price_listing = list.find('h2', attrs={'class': 'listing-card_price__lEBmo'}).find('span').get_text()
                    price_listing = price_listing.replace('$', '').replace(',', '')
                                        
                    # find number of beds and baths on the listing
                    bed = list.find('span', attrs={'data-cy': 'property-beds'}).find('span').get_text()
                    bath = list.find('span', attrs={'data-cy': 'property-baths'}).find('span').get_text()
                    
                    # go into the page listing and look for type of property, property tax and square footage of property
                    listing_url = list['href']
                    listing_page = requests.get(listing_url)
                    listing_soup = BeautifulSoup(listing_page.content, 'lxml')
                    
                    details = listing_soup.find_all('li', attrs={'data-testid': 'detail-bullet'})
                    property_type = 'N/A'
                    property_sqft = 'N/A'
                    for detail in details: 
                        detail_type = detail.find('h4').get_text()
                        if detail_type == 'Property Tax': 
                            property_tax = detail.find_all('span')[1].get_text()
                            property_tax = property_tax.replace('$', '').replace(',', '')
                        elif detail_type == 'Property Type': 
                            property_type = detail.find_all('span')[1].get_text()
                        elif detail_type == 'Square Footage': 
                            property_sqft = detail.find_all('span')[1].get_text()
                            property_sqft = property_sqft.replace(',', '').replace(' SQFT', '')
                    
                    # consolidate information collected and put into csv file
                    info = [location, property_type, price_listing, property_sqft, property_tax, bed, bath]
                    file_writer.writerow(info)
                    
            # check next page to see if information is still available to scrape through
            params['pageNumber'] = str(int(params['pageNumber']) + 1)
            
            page = requests.get(url, params=params)
            soup = BeautifulSoup(page.content, 'lxml')
            lists = soup.find_all('a', attrs={'data-cy': 'listing-card'})
            
            if not lists:
                break
            
    print('Finished extracting.')
    
main()