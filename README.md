# 🥦🍎 Fruit & Vegetable Pricing ChatBot

A **Streamlit**-based chatbot that provides the latest **fruit and vegetable prices** in Andhra Pradesh by scraping live data from [market.todaypricerates.com](https://market.todaypricerates.com).  
Simply type the name of a fruit or vegetable, and the chatbot will return its market price, retail range, and mall range.
**🌐 Live Demo:** https://fruit-vegetable-pricing-chatbot.streamlit.app/

---

## 🚀 Features

- 📊 **Live Price Data** – Scrapes updated prices from the web
- 🥗 **Supports Fruits & Vegetables** – Choose from a sidebar switch
- 🧠 **Smart Matching** – Suggests closest matches if the item name isn’t exact
- 📱 **User-friendly Interface** – Built with Streamlit for simplicity
- 🔍 **Detailed Output** – Shows market, retail, and mall price ranges

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (for UI)
- **BeautifulSoup** (for web scraping)
- **Pandas** (for data handling)
- **Requests** (for HTTP requests)
- **difflib** (for fuzzy matching)

---

## 📦 Installation
1. **Clone the repository**
->git clone https://github.com/yourusername/Fruit-Vegetable-Pricing-Chatbot.git
->cd Fruit-Vegetable-Pricing-Chatbot
2. **Install dependencies**
->pip install -r requirements.txt
3. **Run the chatbot**
->streamlit run app.py

-----
**📌 Usage**
Select Vegetable Pricing ChatBot or Fruit Pricing ChatBot from the sidebar.
Enter the name of the item (e.g., Tomato, Banana).
If exact match is not found, select from suggested matches.
**View prices including:**
->Market Price
->Retail Price Range
->Mall Price Range

---
**✨ Example**
**Input:** Tomato
**Output:**
Name: Tomato  
Unit: 1 Kg  
Market Price: ₹30  
Retail Price Range: ₹32 - ₹35  
Mall Price Range: ₹35 - ₹40

----
**👨‍💻 Author**
Crafted with curiosity 🚀 by Sahithi — turning ideas into code, one project at a time.

---
**“Data is the new oil — and now you can get it for your groceries too!” 😄**
