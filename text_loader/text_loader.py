from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv  

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary for the following sample -\n {sample}",
    input_variables = ["sample"]
)

parser = StrOutputParser()

loader = TextLoader("sample.txt", encoding="utf-8")


samples = loader.load()

print(type(samples))
print(len(samples))
print(samples[0].page_content)
print(samples[0].meta_data)
chain = prompt | model | parser
print(chain.invoke({"sample":samples[0].page_content}))