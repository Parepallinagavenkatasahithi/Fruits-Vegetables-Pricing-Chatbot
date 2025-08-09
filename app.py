import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
from difflib import get_close_matches

# -------------------------
# Functions
# -------------------------
def scrape_prices(url):
    """Scrapes the price data from the given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    headers = [th.text.strip() for th in table.find_all("th")]
    rows = []

    for tr in table.find_all("tr")[1:]:
        cols = tr.find_all("td")
        if len(cols) == 5:
            rows.append({
                "name": cols[0].text.strip(),
                "unit": cols[1].text.strip(),
                "market_price": cols[2].text.strip(),
                "retail_price_range": cols[3].text.strip(),
                "mall_price_range": cols[4].text.strip()
            })
    return pd.DataFrame(rows)

@st.cache_data
def load_data():
    veg_url = "https://market.todaypricerates.com/Andhra-Pradesh-vegetables-price"
    fruit_url = "https://market.todaypricerates.com/Andhra-Pradesh-fruits-price"
    veg_df = scrape_prices(veg_url)
    fruit_df = scrape_prices(fruit_url)
    return veg_df, fruit_df

def find_matches(df, query):
    names = df['name'].tolist()
    matches = get_close_matches(query, names, n=5, cutoff=0.4)
    return matches

def get_item_details(df, name):
    row = df[df['name'].str.lower() == name.lower()]
    if not row.empty:
        r = row.iloc[0]
        return f"""
        **Fruit/Vegetable Name:** {r['name']}  
        **Unit:** {r['unit']}  
        **Market Price:** {r['market_price']}  
        **Retail Price Range:** {r['retail_price_range']}  
        **Mall Price Range:** {r['mall_price_range']}
        """
    return None

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="Fruit & Vegetable Pricing ChatBot")
