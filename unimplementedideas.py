import requests
from bs4 import BeautifulSoup



url = 'https://www.drugs.com'

alphabets = [f"{chr(i).lower()}.html" for i in range(65,91)]

extension = '/alpha/'

for alpha in alphabets:
    r = requests.get(url=url+extension+alpha)
    soup = BeautifulSoup(r.text,features='html.parser')
    ul = soup.find('ul',{"class": "ddc-list-column-2"})

    for x in ul.children:
        print(x)

    break

# a way to get info about drugs, still in baby phase