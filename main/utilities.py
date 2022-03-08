import requests
import pandas as pd
import numpy as np


def reverse_string(string: str) -> str:

    return string[::-1]


def get_animes(names: str) -> dict:
    response = requests.get(f"https://api.jikan.moe/v3/search/anime?q={names}")

    return response.json()


def extract(ANIMES: list) -> list:
    combined = []
    for names in ANIMES:
        anime_raw_info = get_animes(names)["results"]
        combined += anime_raw_info

    return combined


def transform(combined: list) -> pd.DataFrame:
    COLUMNS = ["title"]
    anime_df = pd.DataFrame(combined)
    anime_df = anime_df[COLUMNS]
    return anime_df


def read_csv(csv_file: str) -> pd.DataFrame:
    csv_listings = pd.read_csv(
        f"/Users/tyson/new_projects/assignment/sample_data/{csv_file}"
    )

    return csv_listings


def transform_csv(csv_listings: pd.DataFrame) -> pd.DataFrame:
    csv_listings.rename(
        columns={
            "Index": "house_id",
            ' "Living Space (sq ft)"': "living_space",
            ' "Beds"': "beds",
            ' "Baths"': "baths",
            ' "Zip"': "zip",
            ' "Year"': "year_of_house",
            ' "List Price ($)"': "list_price",
        },
        inplace=True,
    )
    csv_listings["LivingSpaceGreaterThan2000"] = np.where(
        csv_listings["living_space"] > 2000, True, False
    )
    csv_listings["Total_Rooms"] = csv_listings["beds"] + csv_listings["baths"]
    csv_listings["ListPriceInclTax"] = csv_listings["list_price"] * 1.13
    csv_listings["EstMortgageFees"] = csv_listings["list_price"] * 0.05
    csv_listings = csv_listings.drop(columns=["zip"])
    csv_listings = csv_listings.drop(
        csv_listings[csv_listings["year_of_house"] < 1980].index
    )
    csv_listings = csv_listings.drop(
        csv_listings[csv_listings["ListPriceInclTax"] < 130000].index
    )

    return csv_listings


def write_csv(csv_listings: pd.DataFrame):
    csv_listings.to_csv(
        "/Users/tyson/new_projects/assignment/sample_data/zillow_cleaned.csv",
        index=False,
    )
