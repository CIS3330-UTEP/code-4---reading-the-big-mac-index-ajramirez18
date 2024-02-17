import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)



def get_big_mac_price_by_year(year,country_code):
    df['date'] = pd.to_datetime(df['date'])

    df_new = df[(df['date'].dt.year == year) & (df['iso_a3'] == country_code.upper())]

    mean_price = df_new['dollar_price'].mean()

    mean_price_rounded = round(mean_price, 2)

    return year, country_code, mean_price_rounded
    
    pass # Remove this line and code your function

def get_big_mac_price_by_country(country_code):
    
    df_new = df[(df['iso_a3'] == country_code.upper())]
    

    mean_price = df_new['dollar_price'].mean()

    mean_price_rounded = round(mean_price, 2)

    return country_code, mean_price_rounded    

    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):

    df['date'] = pd.to_datetime(df['date'])
    

    df_new = df[(df['date'].dt.year == year)] 


    cheapest = df_new['dollar_price'].min()
    cheapest_row = df_new[df_new['dollar_price'] == cheapest]
    country_name = cheapest_row['name'].iloc[0]
    country_code = cheapest_row['iso_a3'].iloc[0]
    cheapest_round = round(cheapest, 2)
    output_string = country_name +'('+country_code+'): $' +str(cheapest_round)

    
    return output_string


    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    
    df['date'] = pd.to_datetime(df['date'])
    

    df_new = df[(df['date'].dt.year == year)]    
    
    most_expensive = df_new['dollar_price'].max()
    max_row = df_new[df_new['dollar_price'] == most_expensive]
    country_name = max_row['name'].iloc[0]
    country_code = max_row['iso_a3'].iloc[0]
    max_round = round(most_expensive, 2)
    output_string = country_name +'('+country_code+'): $' +str(max_round)

    
    return output_string

    pass # Remove this line and code your function

if __name__ == "__main__":


    pass # Remove this line and code your user interface