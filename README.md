# 📊 Data Visualization with Ollama (LLaMA 3.2 by Meta)

![Project Screenshot](Screenshot%202024-10-11%20175927.png)

## 🔍 Overview
This project provides a powerful solution for sales data analysis and visualization. It supports **data ingestion from CSV files and web scraping**, enabling flexible data sourcing. Users can leverage **Pandas and Streamlit** for efficient data processing and exploration. 

🚀 **Key Highlights:**
- **AI-powered Chat** 🤖: Ask natural language questions about your data.
- **Dynamic Charting** 📈: Generate interactive visualizations.
- **Automated Table Structuring** 📋: AI organizes web-scraped data into tables.
- **Seamless Integration** 🔄: Works with CSV and web sources.

## ✨ Features
✅ **Flexible Data Ingestion**: Import sales data from CSV or scrape from websites. 

✅ **Interactive Data Processing**: Utilize Pandas and Streamlit for easy data transformation.

✅ **AI-Powered Insights**: Ask questions about your CSV data and receive instant responses.

✅ **Visual Analytics**: Generate insightful charts to identify trends and patterns.

✅ **Web Data Structuring**: Convert raw web data into structured tables for analysis.

### 🖥️ Demo
#### 🔎 Web Scraping Example
![Web Scraping Demo](Screen-Recording-2024-09-30-113502.gif)

#### 📊 Data Analysis in Action
![Data Analysis Demo](Screen-Recording-2024-10-11-201856.gif)

## ⚙️ Requirements
- Python 3.x 🐍
- Pandas 📊
- Streamlit 🌐
- Selenium 🕷️
- Ollama + LLaMA 3.2 Model 🧠

## 📥 Installation
1️⃣ **Clone the repository**:
```powershell
git clone https://github.com/vy-phan/WebScraping.git
```
2️⃣ **Navigate to the project directory**:
```powershell
cd datavis
```
3️⃣ **Install dependencies**:
```powershell
pip install -r requirements.txt
```

## 🛠️ Installing Ollama & LLaMA 3.2
### Step 1️⃣: Install Ollama
🔗 Download from: [Ollama Official Site](https://ollama.ai/download)  
📥 Run the installer and follow the setup instructions.

### Step 2️⃣: Install LLaMA 3.2 Model
Run the following command:
```bash
ollama pull llama3.2
```

### Step 3️⃣: Verify Installation
Check if the model is installed:
```bash
ollama list
```
✅ You should see `llama3.2` in the list.

### 🚀 Running LLaMA 3.2
Start a chat session with:
```bash
ollama run llama3.2
