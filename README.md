# Data Visualization with Ollama version llama3.2 by Meta
<img src="Screenshot 2024-10-11 175927.png">

## Description
This project offers a comprehensive solution for sales data analysis and visualization. It seamlessly integrates data ingestion from CSV files and web scraping, providing flexibility in data sourcing. Users can leverage the power of Pandas and Streamlit for efficient data processing and interactive exploration. A unique AI-powered chat feature allows users to ask natural language questions about their data, gaining deeper insights. Dynamic charting capabilities enable the creation of compelling visualizations, revealing trends and patterns. Furthermore, the project employs AI to automatically structure scraped web data into organized tables, streamlining the analysis process. This project empowers users to unlock the full potential of their sales data, regardless of its origin, through a user-friendly and intelligent interface.

## Features
-**Flexible Data Ingestion:** Import sales data from CSV files. The project allows users to easily change the working directory for seamless file access. Additionally, it incorporates web scraping capabilities to extract data from various websites, expanding the range of data sources.

-**Powerful Data Processing with Pandas and Streamlit:** Leveraging the robust data manipulation capabilities of the Pandas library within an interactive Streamlit interface, users can explore and process data efficiently. This includes data cleaning, transformation, and aggregation.

-**Interactive Data Exploration with AI-Powered Chat:** A unique feature of this project is its integrated AI chat functionality. Users can ask natural language questions about their CSV data and receive insightful responses, facilitating data understanding and exploration. This provides a user-friendly way to interact with and glean insights from the data.

-**Dynamic Data Visualization:** Create compelling visualizations of sales data using a variety of chart types. This feature allows users to identify trends, patterns, and outliers within their data, enhancing data interpretation and communication.

-**AI-Powered Table Generation from Web Data:** Scraped web data can be automatically structured into organized tables using AI, simplifying data analysis and reporting. This feature streamlines the process of converting unstructured web data into a usable format.

<h2>Demo Page Scraping</h2>
<img src="Screen-Recording-2024-09-30-113502.gif">
<br>
<h2>Demo Page Analyize</h2>
<img src="Screen-Recording-2024-10-11-201856.gif">

## Requirements
- Python 3.x
- pandas
- Streamlit
- Seleiumn
- ollama with model Llama 3.2 7B by Meta

## Installation
1. Clone the repository:
    ```powershell
    git clone https://github.com/vy-phan/WebScraping.git
    ```
2. Navigate to the project directory:
    ```powershell
    cd datavis
    ```
3. Install the required packages:
    ```powershell
    pip install -r requirements.txt
    ```

# Installing Ollama and LLaMA 3.2 Model

This guide outlines the steps to install Ollama and the LLaMA 3.2 model.

## Step 1: Install Ollama

1. Download the Ollama installer from the official website: [https://ollama.ai/download](https://ollama.ai/download)
2. Run the installer and follow the on-screen instructions to complete the installation.

## Step 2: Install LLaMA 3.2 Model

1. Open a terminal or command prompt.
2. Run the following command to install the LLaMA 3.2 model:

```bash
ollama pull llama-3.2
```

## Step 3: Verify Installation

1. Run the following command to verify that the model has been installed correctly:

```bash
ollama list
```

You should see llama-3.2 listed among the installed models.

## Running LLaMA 3.2

After successful installation and verification, you can start a chat session with the LLaMA 3.2 model using:

```bash
ollama run llama-3.2
```
