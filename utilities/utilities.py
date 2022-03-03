import requests
import pandas as pd

def reverse_string(string : str) -> str:

    
    return string[::-1]


def get_animes(names: str):
    response = requests.get('https://api.jikan.moe/v3/search/anime?q=' + names)
    
    return response.json()


def extract(ANIMES: list):
    combined = []
    for names in ANIMES:
        anime_raw_info = get_animes(names)['results']
        combined += anime_raw_info
        
    return combined


def transform(combined: list):
    COLUMNS = ['title']
    anime_df = pd.DataFrame(combined)
    anime_df = anime_df[COLUMNS]
    return anime_df