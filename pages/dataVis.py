import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import os 
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

st.title(":bar_chart: Data Visualization")
st.sidebar.success("Generate New Columns")

data = st.file_uploader(":file_folder: Upload a file",type=(["csv","tsv","xlsx","xls"]))

# function chart 
def create_line_chart(df, x_col , y_col):
    if x_col == None or y_col == None:
        if x_col == None : 
            st.line_chart(df[y_col])
        if y_col == None :
            st.line_chart(df[x_col])
    else:
        st.line_chart(df.set_index(x_col)[y_col])
def create_bar_chart(df, x_col , y_col):
    if x_col == None or y_col == None:
        if x_col == None : 
            st.bar_chart(df[y_col])
        if y_col == None :
            st.bar_chart(df[x_col])
    else:
        st.bar_chart(df.set_index(x_col)[y_col])
def create_scatter_chart(df, x_col , y_col):
    st.scatter_chart(df.set_index(x_col)[y_col])
def create_area_chart(df, x_col , y_col):
    if x_col == None or y_col == None:
        if x_col == None : 
            st.area_chart(df[y_col])
        if y_col == None :
            st.area_chart(df[x_col])
    else:
        st.area_chart(df.set_index(x_col)[y_col])


# function create new data 
def create_new_columndf(df,col1_new_i, col2_new_i,col_operation, col_new_name):
    operation = ''
    if col_operation == " Add ( + ) ":
        operation = "+"
    elif col_operation == " Multi ( * ) ":
        operation = "*"  
    else:
        operation = "Lựa chọn không hợp lệ"
        
    st.sidebar.write(col1_new_i + operation + col2_new_i)    
    df[col1_new_i] = pd.to_numeric(df[col1_new_i], errors='coerce')
    df[col2_new_i] = pd.to_numeric(df[col2_new_i], errors='coerce')

    if operation != '':
        if operation == "+":
            df[col_new_name] = df[col1_new_i] + df[col2_new_i]
        if operation == "*":
            df[col_new_name] = df[col1_new_i] * df[col2_new_i]
    return df

# function LLM RAG

model = OllamaLLM(model="llama3.2")

def parse_with_ollama(dom_chunks):
    prompt = ChatPromptTemplate.from_template(

    """
    Here is a row from a CSV file that has been converted into a dictionary format:
    {dom_content}
    Please follow these instructions carefully: \n\n

    1. **Analyze the data and suggest suitable chart types for the columns.**
    When making your suggestions, please output only the chart name and the corresponding column names in a clear and concise manner. 
    Column names should be capitalized.
    **Note:** Only suggest the following chart types: line chart, bar chart, scatter chart, and area chart. 
    If there's no suitable chart for a column, skip it.
    
    2. **Suggest new column names** by combining existing columns using mathematical operations (e.g., addition, subtraction, etc.). 
    Just output the new column name and the mathematical expression (e.g., 'Total Sales' = 'Sales' + 'Discount').

    3. **Empty Response:** If there's any issue with the data or if you cannot find a suitable chart for any column, simply leave the output blank.
    """

    )
    chain = prompt | model 

    parsed_result = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_result.append(response)
    return "\n".join(parsed_result)

if data is not None:
    filename = data.name
    st.success(filename)
    df = pd.read_csv(data)

    # append into rows
    rows = []
    for i in range(3):
        rows.append(df.iloc[i].to_dict())

    #I.) preview data
    st.subheader("Data Preview")
    st.info("Preview data with first 5 rows")
    st.write(df.head())

    # describe data
    st.subheader("Data Summary")
    st.info("Basic general information of the dataf")
    st.write(df.describe())

    #II.) filter data
    st.subheader("Filter Data")
    st.info("Select detail each values in columns")
    columnes = df.columns.tolist()
    col_1 , col_2 = st.columns(2)
    with col_1:
        selected_col = st.selectbox("Select columns to filter by",columnes)
    unique_val = df[selected_col].unique()
    with col_2:    
        selected_val = st.selectbox("Select value",unique_val)

    filter_df = df[df[selected_col]== selected_val] 
    st.write(filter_df)
    
    
    # option chart 
    Chart_Name = ['line_chart','bar_chart','scatter_chart','area_chart']
    
    # create new column in NAVBAR
    col1_new_i = st.sidebar.selectbox("Select col 1",columnes)
    col2_new_i = st.sidebar.selectbox("Select col 2",columnes)
    col_operation = st.sidebar.selectbox("Select caculation",[" Add ( + ) "," Multi ( * ) "])
    col_new_name = st.sidebar.text_input("Col name")

    if 'flag' not in st.session_state:
        st.session_state.flag = False
        
    if col1_new_i and col2_new_i and col_operation and col_new_name:
        st.sidebar.info(f"You are make sure chose column name with {col_new_name} ?")
        if st.sidebar.button("Create Column"):
            st.session_state.flag = True

    #III.) create chart with columns
    st.subheader("Plot data")
    if st.session_state.flag:
        create_new_columndf(df,col1_new_i, col2_new_i,col_operation, col_new_name)
        columnes_after = df.columns.to_list()
    else:
        columnes_after = columnes   

    columnes_after.insert(0,None)         
    
    #a) select columns 
    st.info("Generate chart with [ column x ] , [ column y ]")
    col1, col2 = st.columns(2)
    with col1:
        x_col = st.selectbox("Select x-axis col",columnes_after)
    with col2:
        y_col = st.selectbox("Select y-axis col",columnes_after)
    
    Chart_Val = st.selectbox("Enter your chart you want",Chart_Name) 
    #b) show data after   
    st.write(df.head())

    #c) button create chart
    if st.button("Create Chart"):
        # st.line_chart(df.set_index(x_col)[y_col])
        if Chart_Val == 'line_chart':
            create_line_chart(df,x_col,y_col)
        elif Chart_Val == 'bar_chart':
            create_bar_chart(df,x_col,y_col)
        elif Chart_Val == 'scatter_chart':
            create_bar_chart(df,x_col,y_col)    
        elif Chart_Val == 'area_chart':
            create_area_chart(df,x_col,y_col)  


    #IV.) Generate recommand 
    # if 'prompt' not in st.session_state:
    #     st.session_state.prompt = False

    st.subheader("Create charts with AI suggestions")
    if st.button("Generate with Ollama 3.2"):
        st.write(parse_with_ollama(rows))

else:
    os.chdir("D:\FileExcel")    
    df = pd.read_csv("sales2019_1.csv")
    st.success("sales2019_1")

    # append into rows
    rows = []
    for i in range(2):
        rows.append(df.iloc[i].to_dict())

    # preview data
    st.subheader("Data Preview")
    st.info("Preview data with first 5 rows")
    st.write(df.head())

    # describe data
    st.subheader("Data Summary")
    st.info("Basic general information of the dataf")
    st.write(df.describe())

    # filter data
    st.subheader("Filter Data")
    st.info("Select detail each values in columns")
    columnes = df.columns.tolist()
    col_1 , col_2 = st.columns(2)
    with col_1:
        selected_col = st.selectbox("Select columns to filter by",columnes)
    unique_val = df[selected_col].unique()
    with col_2:    
        selected_val = st.selectbox("Select value",unique_val)

    filter_df = df[df[selected_col]== selected_val] 
    st.write(filter_df)
    
    
    # option chart 
    Chart_Name = [None,'line_chart','bar_chart','scatter_chart','area_chart']
    
    # create new column in NAVBAR
    col1_new_i = st.sidebar.selectbox("Select col 1",columnes)
    col2_new_i = st.sidebar.selectbox("Select col 2",columnes)
    col_operation = st.sidebar.selectbox("Select caculation",[" Add ( + ) "," Multi ( * ) "])
    col_new_name = st.sidebar.text_input("Col name")

    if 'flag' not in st.session_state:
        st.session_state.flag = False
        
    if col1_new_i and col2_new_i and col_operation and col_new_name:
        st.sidebar.info(f"You are make sure chose column name with {col_new_name} ?")
        if st.sidebar.button("Create Column"):
            st.session_state.flag = True

    #III.) create chart with columns
    st.subheader("Plot data")
    if st.session_state.flag:
        create_new_columndf(df,col1_new_i, col2_new_i,col_operation, col_new_name)
        columnes_after = df.columns.to_list()
    else:
        columnes_after = columnes    

    columnes_after.insert(0,None)
    
    #a) select columns 
    st.info("Generate chart with [ column x ] , [ column y ]")
    col1, col2 = st.columns(2)
    with col1:
        x_col = st.selectbox("Select x-axis col",columnes_after)
    with col2:
        y_col = st.selectbox("Select y-axis col",columnes_after)
    
    Chart_Val = st.selectbox("Enter your chart you want",Chart_Name) 
    #b) show data after   
    st.write(df.head())

    #c) button create chart
    if st.button("Create Chart"):
        # st.line_chart(df.set_index(x_col)[y_col])
        if Chart_Val == 'line_chart':
            create_line_chart(df,x_col,y_col)
        elif Chart_Val == 'bar_chart':
            create_bar_chart(df,x_col,y_col)
        elif Chart_Val == 'scatter_chart':
            create_bar_chart(df,x_col,y_col)    
        elif Chart_Val == 'area_chart':
            create_area_chart(df,x_col,y_col)  


    #IV.) Generate recommand 
    # if 'prompt' not in st.session_state:
    #     st.session_state.prompt = False

    st.subheader("Create charts with AI suggestions")
    if st.button("Generate with Ollama 3.2"):
        st.write(parse_with_ollama(rows))
    #     st.session_state.prompt = True 
    
    # if st.session_state.prompt:





         


    



    

    

    