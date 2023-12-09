from langchain.llms import GooglePalm
from pipeline import SQLConnect, fewShotPromptTemplate,vectorDB
from langchain_experimental.sql import SQLDatabaseChain

sql = SQLConnect()
sqldb = sql.connect()
vectordb = vectorDB(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
example_selector = vectordb.retriever()
few_shot_temp = fewShotPromptTemplate(example_selector=example_selector)
few_shot_prompt = few_shot_temp.prompt()

llm = GooglePalm(temperature = 0.1)

chain = SQLDatabaseChain.from_llm(llm = llm,db= sqldb, verbose=True, prompt=few_shot_prompt,return_intermediate_steps = True)