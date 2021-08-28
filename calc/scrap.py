import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

def getCovidCase():
    html = requests.get('https://www.worldometers.info/coronavirus/').text
    html_soup = BeautifulSoup(html, 'html.parser')
    rows = html_soup.find_all('tr')

    def extract_text(row, tag):
        element = BeautifulSoup(row, 'html.parser').find_all(tag)
        text = [col.get_text() for col in element]
        return text

    def write_csv():
        with open('corona.csv', 'w') as store:
            Store = csv.writer(store, delimiter=',')
            Store.writerow(heading_row)
            for row in rows:
                test_data = extract_text(str(row), 'td')[1:9]
                Store.writerow(test_data)      
        store.close()      

    list_data = []
    def read_csv():
        with open('corona.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for l in csvFile:
                if len(l) ==  0 :
                    del l
                else:
                    list_data.append(l)

    coll_list = []
    def data_collect():
        for x in list_data[:231]:
            coll_list.append(x)

    def del_li():
        del coll_list[:8]
        return coll_list

    heading = rows.pop(0)
    heading_row = extract_text(str(heading), 'th')[1:9]
    write_csv()

    read_csv()
    data_collect()
    data = del_li()
    return data