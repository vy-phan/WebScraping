import pandas as pd
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

df = pd.read_csv("sales2019_1.csv")

rows = []
for i in range(3):
    rows.append(df.iloc[i].to_dict())


model = OllamaLLM(model="llama3.2")

# print(rows)

def parse_with_ollama(dom_chunks):
    prompt = ChatPromptTemplate.from_template(
        """
        Here is a row from a CSV file that has been converted into a dictionary format:
        {dom_content}
        Please follow these instructions carefully \n\n
        1 ** Please analyze the data and suggest suitable chart types for the columns**.When making your suggestions, please output the chart name and the corresponding columns in a clear and concise manner. Column names should be capitalized. 
        2 **Empty Response** If there's any issue with the data or if you cannot find a suitable chart, simply leave the output blank.
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

readFile = parse_with_ollama(rows)
print(readFile)





