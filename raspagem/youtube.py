from bs4 import BeautifulSoup
import requests

url = "https://youtube.com"
resposta = requests.get(url)
conteudo_html = resposta.content

soup = BeautifulSoup (conteudo_html, "html.parser")

links = soup.find_all ("p")

for link in links:
    print("texto {%s}, url {%s}" % (link.text,link.get("href")))