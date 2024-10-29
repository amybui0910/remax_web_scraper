# Remax.ca Web Scraper

This project is a Python project that extracts data from Remax.ca for real estate data
for any city in Canada and for real estate on sale or for rent. The data is then saved 
to a CSV file.

### Getting Started
To run scraper.py, you will need Python 3 installed on your machine. Additionally, 
the following libraries are required: 
- BeautifulSoup
- requests
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these libraries

```bash
pip install beautifulsoup4 requests
```

### Usage
To use the project, type in your terminal "python scraper.py". Then you will be prompted with 
"City to search: " in which you will type the city in Canada you wish to search. Then you will 
be prompted with "Searching for (sale/rent): " in which you will input which type of real 
estate you wish to scrape for. 

Then you will wait for the program to say "Finished extracting." and a file named 
"*city name*_*type of real estate*_search_results.csv will appear in the same directory.

### Data Collected in CSV file
The web scraper will extract the following data for each real estate listing
- Location
- Property Type
- Price of the Listing
- Total Square Footage
- Property Tax
- Number of Beds
- Numbers of Baths
See example csv file provided. 

## TODO
- [ ] Make it possible to put data into an sql database
- [ ] Create visualization tool with pandas/matplotlib

### Credits
This project was created by Amy Bui. The code is based on examples from the BeautifulSoup 
documentation and the requests documentation, and draws inspiration from 
https://github.com/oussafik/Web-Scraping-RealEstate-Beautifulsoup/tree/main. 

### License
MIT License

Copyright (c) [2024] [Amy Bui]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.