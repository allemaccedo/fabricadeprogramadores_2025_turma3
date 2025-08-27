from bs4 import BeautifulSoup
import requests

url = "https://www.tiktok.com/login?redirect_url=https%3A%2F%2Fwww.tiktok.com%2Fpt-BR%2F&lang=en&enter_method=mandatory"
resposta = requests.get(url)
conteudo_html = resposta.content

soup = BeautifulSoup (conteudo_html, "html.parser")

links = soup.find_all ("a")

for link in links:
    print("texto {%s}, url {%s}" % (link.text,link.get("href")))