import requests
from bs4 import BeautifulSoup


def parse():
    url = 'https://www.omgtu.ru/general_information/faculties/'
    page = requests.get(url)
    print(page.status_code)
    faculties = []
    allFaculties = []
    file = open('result.txt', 'w')
    soup = BeautifulSoup(page.text, "html.parser")
    allFaculties = soup.find_all('div', id='pagecontent')

    for facult in allFaculties:
        faculties.append(facult.find('ul').text)

    faculties = faculties[0][0:len(faculties[0]) - 3].split('\n')

    for facult in faculties:
        if facult != '':
            file.write(facult + '\n')

    file.close()
