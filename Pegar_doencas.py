import requests
import re
from bs4 import BeautifulSoup

def clean_html(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def get_descricao(doenca):

    doenca = doenca.replace(' ', '-')
    request_url = 'https://www.minhavida.com.br/saude/temas/' + doenca

    page = requests.get(request_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    main_div = soup.find(class_='main-contents').find(class_='paragraph')

    descricao = clean_html(str(main_div))

    return descricao


def get_sintomas(doenca):

    doenca = doenca.replace(' ', '-')
    request_url = 'https://www.minhavida.com.br/saude/temas/' + doenca

    page = requests.get(request_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    main_div = soup.find(class_='main-contents').find(class_='main-article -spacing-left')

    index_sintoma_title = None
    sintomas_raw = None
    sintomas = list()

    for i in range(len(main_div.contents)):
      if('Sintomas' in str(main_div.contents[i]) and 'topic-title' in str(main_div.contents[i])):
          index_sintoma_title = i
      if(index_sintoma_title != None and i > index_sintoma_title and 'paragraph bullet' in str(main_div.contents[i])):
        sintomas_raw = main_div.contents[i]
        break
    
    sintomas_raw = sintomas_raw.find_all('li')

    for sintoma in sintomas_raw:
      sintoma = clean_html(str(sintoma))
      sintomas.append(sintoma)

    return sintomas

def main():

  list_doencas = set()
  f = open("doencas.txt", "r")
  if f.mode == 'r':
    contents = f.read()
    contents = contents.splitlines()
    for content in contents:
        list_doencas.add(content)

  file_name = 'info_doencas.txt'
  f = open(file_name,"a+")
  
  for doenca in list_doencas:
    sintomas = get_sintomas(doenca)
    sintomas_clean = ''
    descricao = get_descricao(doenca)

    for sintoma in sintomas: 
      sintomas_clean = sintomas_clean + sintoma + ";"
    
    sintomas_clean = sintomas_clean[0:len(sintomas_clean)]

    f.write(doenca + '\n')
    f.write(descricao + '\n')
    f.write(sintomas_clean + '\n\n')
  f.close()

main()