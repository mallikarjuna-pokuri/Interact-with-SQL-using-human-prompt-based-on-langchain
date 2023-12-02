from langchain.utilities import SQLDatabase
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from artifacts.few_shots import few_shots
from langchain.prompts import SemanticSimilarityExampleSelector,FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from artifacts.few_shots import mysql_prompt
import os
from dotenv import load_dotenv

load_dotenv()


DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]
DBHOST = os.environ["DBHOST"]
DBNAME = os.environ["DBNAME"]
dbUri = f"mysql+pymysql://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}"
class SQLConnect:
    def __init__(self,dbUri = dbUri):
        self.dbUri = dbUri
    def connect(self):
        self.sqldb = SQLDatabase.from_uri(self.dbUri,sample_rows_in_table_info=3)
        return self.sqldb

class vectorDB:
    def __init__(self,model_name = 'sentence-transformers/all-MiniLM-L6-v2'):
        print("Successfully loaded embeddings model")
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
    def retriever(self):
        to_vectorize = [" ".join(example.values()) for example in few_shots]
        vectorstore = Chroma.from_texts(to_vectorize, self.embeddings, metadatas=few_shots)
        example_selector = SemanticSimilarityExampleSelector(
                vectorstore=vectorstore,
                k=2,
            )
        return example_selector

class fewShotPromptTemplate:
    def __init__(self,example_selector,mysql_prompt = mysql_prompt):
        self.mysql_prompt = mysql_prompt
        self.example_selector = example_selector
    def prompt(self):
        example_prompt = PromptTemplate(
                input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
                template="""
                Question: {Question}
                SQLQuery: {SQLQuery}
                SQLResult: {SQLResult}
                Answer: {Answer}
                """,
            )
        print("created Few Shot Prompt Template")
        few_shot_prompt = FewShotPromptTemplate(
            example_selector=self.example_selector,
            example_prompt=example_prompt,
            prefix=self.mysql_prompt,
            suffix=PROMPT_SUFFIX,
            input_variables=["input", "table_info", "top_k"], #These variables are used in the prefix and suffix
        )
        return few_shot_prompt



if __name__ == "__main__":
    example_selector = vectorDB().build()
    print(example_selector.select_examples({"Question": "Tell me about the doctor of patient Bell"}))
