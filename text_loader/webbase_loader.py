from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/apple-iphone-17-white-256-gb/p/itm68ad8410784c7?pid=MOBHQV9YAZYYWY8A&lid=LSTMOBHQV9YAZYYWY8A6D2THC&hl_lid=&marketplace=FLIPKART&fm=eyJ3dHAiOiJwbXVfdjMiLCJwcnB0IjoiaHAiLCJtaWQiOiJjb250aW51dW0vaHAifQ%3D%3D&ctx=eyJkZWxpdmVyZWRCeSI6IiIsImRpc3BsYXlQcmljZSI6Ijg5MTAwIn0%3D&pageUID=1795254029666"

loader = WebBaseLoader(url) 

docs =loader.load()
print(len(docs))
print(docs[0].page_content)