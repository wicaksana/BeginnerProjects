__author__ = 'arif'

from urllib.request import urlopen
from bs4 import BeautifulSoup

# https://www.reddit.com/r/beginnerprojects/comments/3hrjkq/project_capital_cities/
# Goals:
# Create a program that will take the name of a state or province and tell the user its capital city.
# Support the reverse operation as well. Can you expand this to national capitals?
# Hint
# Instead of typing all the information yourself, try automating the process by scraping it from a website.


def get_capital(country, lists):
    try:
        print('\nthe capital of {} is {}'.format(country,lists[country]))
    except KeyError:
        print('\n{} is not listed as a country'.format(country))


def get_country(capital, lists):
    country = ''
    for k,v in lists.items():
        if v == capital:
            country = k
    if country:
        print('\nthe country of {} is {}'.format(capital, country))
    else:
        print('\n{} is not exist'.format(capital))


def get_data():
    countries_capitals = {}
    # data retrieved from https://en.wikipedia.org/wiki/List_of_national_capitals_by_population
    url = 'https://en.wikipedia.org/wiki/List_of_national_capitals_by_population'
    html = urlopen(url)
    bsObj = BeautifulSoup(html)

    rows = bsObj.find("table",attrs={"class":"wikitable sortable"}).find_all('tr')

    for row in rows:
        cell = row.find_all('td')
        if cell:
            country = cell[1].find('a').get_text()
            capital = cell[2].find('a').get_text()
            countries_capitals[country] = capital

    return countries_capitals


def main():
    lists = get_data()

    while True:
        print('')
        print('1. search the capital of a country')
        print('2. search the country of a capital\n')

        try:
            choice = int(input('enter your choice (1 or 2): '))
            if choice == 1:
                country = input('\nenter the country: ')
                get_capital(country,lists)
            elif choice == 2:
                capital = input('\nenter the capital: ')
                get_country(capital, lists)
            else:
                pass

        except ValueError:
            print('\nplease enter the correct value (1 or 2)')


if __name__=='__main__':
    main()
