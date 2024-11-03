import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

def main():
    if len(sys.argv) != 2: 
        print('Usage: python analyze-data.py *name_of_csv_file*.csv')
        sys.exit(1)
    
    try:
        df = pd.read_csv(sys.argv[1])
    except FileNotFoundError:
        print("File is not a csv file or file does not exist.") 
        sys.exit(2)
    
    # clean up data
    # remove vacant land type
    df = df[df["Property_Type"] != "Vacant Land"]
    
    # remove year from property tax
    if df["Property_Tax"].dtype == 'object': 
        extr = df["Property_Tax"].str.extract(r'^(\d{4})', expand=False)
        df["Property_Tax"] = pd.to_numeric(extr)
    
    # drop all rows with null values
    new_df = df.dropna()
    
    ### Plot of all of the data
    
    # Price_Listing vs Property Sqft
    new_df.plot(kind="scatter", x="Price_Listing", y="Property_Sqft")
    x = new_df["Price_Listing"].to_numpy()
    m, b = np.polyfit(x, new_df["Property_Sqft"].to_numpy(), 1)
    plt.plot(x, m*x+b)
    
    plt.figure(1)
    
    # Price_Listing vs Property Tax
    new_df.plot(kind="scatter", x="Price_Listing", y="Property_Tax")
    m, b = np.polyfit(x, new_df["Property_Tax"].to_numpy(), 1)
    plt.plot(x, m*x+b)
    
    plt.figure(2)
    
    # Price_Listing vs Bed
    new_df.plot(kind="hist", x="Price_Listing", y="Bed")
    plt.figure(3)
    
    # Price_Listing vs Bath
    new_df.plot(kind="hist", x="Price_Listing", y="Bath")
    plt.figure(4)
    
    plt.show()
        
    
main()