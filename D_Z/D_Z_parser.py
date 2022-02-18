from bs4 import BeautifulSoup
import requests
import csv


def get_csv(data):
    with open("job_ru.csv", "w") as f:
        write = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        write.writeheader()
        for i in data:
            write.writerow(i)


def get_url(url):
    response = requests.get(url).text
    return response


def get_html(html):
    data = []
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("article", itemscope="itemscope")
    for i in p1:
        job = i.find("span", class_="vacancy-preview-card__title_border").text
        money = i.find("div", class_="vacancy-preview-card__salary vacancy-preview-card__salary-blue").text
        organization = i.find(class_="vacancy-preview-card__company-name").text
        data.append({"job": job, "money": money, "organization": organization})
    get_csv(data)


def main(url):
    print(get_html(get_url(url)))


main("https://rabota.ru")
