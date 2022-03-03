import requests
import pandas as pd

def reverse_string(string : str) -> str:


    return string[::-1]


def get_animes(names: str) -> dict:
    response = requests.get(f"https://api.jikan.moe/v3/search/anime?q={names}")
    
    return response.json()


def extract(ANIMES: list) -> list:
    combined = []
    for names in ANIMES:
        anime_raw_info = get_animes(names)['results']
        combined += anime_raw_info
        
    return combined


def transform(combined: list) -> pd.DataFrame:
    COLUMNS = ['title']
    anime_df = pd.DataFrame(combined)
    anime_df = anime_df[COLUMNS]
    return anime_df


def read_csv(csv_file: str) -> pd.DataFrame:
    csv_contents = pd.read_csv(f"/Users/tyson/new_projects/assignment/sample_data/{csv_file}")
    
    
    return csv_contents


def transform_csv(csv_contents : pd.DataFrame) -> pd.DataFrame:
    csv_contents['Total Rooms'] = csv_contents[' "Beds"'] + csv_contents[' "Baths"']
    csv_contents['ListPriceInclTax'] = csv_contents[' "List Price ($)"'] * 1.13
    csv_contents['EstMortgageFees'] = csv_contents[' "List Price ($)"'] * 0.05
    csv_contents = csv_contents.drop(csv_contents[csv_contents[' "Year"'] < 1980].index)
    csv_contents = csv_contents.drop(csv_contents[csv_contents['ListPriceInclTax'] < 130000].index)

    return csv_contents

def write_csv(csv_contents: pd.DataFrame):
    csv_contents.to_csv('/Users/tyson/new_projects/assignment/sample_data/zillow_cleaned.csv', index=False)



