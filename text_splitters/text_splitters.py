from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Abhishek_Soni (2).pdf')

docs = loader.load()
# print(docs)

# text = """
# Generative AI is a branch of artificial intelligence that focuses on generating new content, such as text, images, audio, and code. It uses Large Language Models (LLMs) like GPT, Llama, and Gemini to understand user queries and generate human-like responses. Generative AI is widely used in chatbots, content generation, document summarization, question answering, and code generation. It helps businesses automate repetitive tasks, improve productivity, and provide better customer experiences.
# """


splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=20,
    separators=''
)

res = splitter.split_documents(docs)
print(res[0].page_content)