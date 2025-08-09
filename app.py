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
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        rows = []

        if table:
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
    except Exception as e:
        st.error(f"Error scraping data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_data():
    veg_url = "https://market.todaypricerates.com/Andhra-Pradesh-vegetables-price"
    fruit_url = "https://market.todaypricerates.com/Andhra-Pradesh-fruits-price"
    veg_df = scrape_prices(veg_url)
    fruit_df = scrape_prices(fruit_url)
    return veg_df, fruit_df

def find_matches(df, query):
    names = df['name'].tolist()
    return get_close_matches(query, names, n=5, cutoff=0.4)

def get_item_details(df, name):
    row = df[df['name'].str.lower() == name.lower()]
    if not row.empty:
        r = row.iloc[0]
        return f"""
        **Name:** {r['name']}  
        **Unit:** {r['unit']}  
        **Market Price:** {r['market_price']}  
        **Retail Price Range:** {r['retail_price_range']}  
        **Mall Price Range:** {r['mall_price_range']}
        """
    return None

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="Fruit & Vegetable Pricing ChatBot", layout="wide")

st.title("🥦🍎 Fruit & Vegetable Pricing ChatBot")

# Load the data
veg_df, fruit_df = load_data()

# Sidebar selection
chatbot_type = st.sidebar.radio(
    "Select ChatBot:",
    ("Vegetable Pricing ChatBot", "Fruit Pricing ChatBot")
)

# Input box
query = st.text_input("Enter a fruit or vegetable name:")

if query:
    if chatbot_type == "Vegetable Pricing ChatBot":
        df = veg_df
    else:
        df = fruit_df

    matches = find_matches(df, query)

    if not matches:
        st.warning("No matches found. Please try another item.")
    elif len(matches) == 1:
        details = get_item_details(df, matches[0])
        if details:
            st.markdown(details)
    else:
        choice = st.selectbox("Did you mean:", matches)
        if st.button("Get Price"):
            details = get_item_details(df, choice)
            if details:
                st.markdown(details)
