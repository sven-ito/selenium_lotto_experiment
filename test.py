__author__ = 'Sven'

from selenium import webdriver
from bs4 import BeautifulSoup
import random

def getMostFrequentNumbers( browser, amount ):

    # Start Selenium WebDriver with URL:
    myURL = "https://www.lotto.de/de/ergebnisse/lotto-6aus49/statistik.html"
    browser.get(myURL)
    content = browser.page_source

    # Start BeautifulSoup Parser:
    soup = BeautifulSoup(content)

    # Find node in DOM tree:
    filtered = soup.find_all("div","stats")[0].find_all("div","node")
    myTupleList = []

    for element in filtered:
        myTupleList.append((element.find_all("div","nr")[0].contents[0],element.find_all("div","menge")[0].contents[0]))

    sorted_tuples = sorted(myTupleList, key=lambda frequency: frequency[1], reverse=True)[0:amount]

    myResult = []

    for tuple in sorted_tuples:
        myResult.append(int(tuple[0]))

    return myResult

def getNumbersThatHaveNotBeenDrawnForALongTime( browser, amount ):

    # Start Selenium WebDriver with URL:
    myURL = "https://www.lotto.de/de/ergebnisse/lotto-6aus49/barometer.html"
    browser.get(myURL)
    content = browser.page_source

    # Start BeautifulSoup Parser:
    soup = BeautifulSoup(content)

    # Find node in DOM tree:
    filtered = soup.find_all("div","stats baro")[0].find_all("div","node")
    myTupleList = []

    for element in filtered:
        myTupleList.append((element.find_all("div","nr")[0].contents[0],element.find_all("div","menge")[0].contents[0]))

    sorted_tuples = sorted(myTupleList, key=lambda frequency: frequency[1], reverse=True)[0:amount]

    myResult = []

    for tuple in sorted_tuples:
        myResult.append(int(tuple[0]))

    return myResult

def getRandomlyDrawnNumbers( amount ):

    myNumbers = range(1,49+1)

    myResult = []

    for i in range(1,amount+1):
        randInd = int(random.uniform(0, len(myNumbers)))

        myResult.append(myNumbers[randInd])
        del(myNumbers[randInd])

    return myResult

browser = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.0.0-windows\bin\phantomjs.exe")

FAMILY_DEFINED_NUMBERS = sorted([5, 13, 18, 17, 34, 36])
PERSONAL_DEFINED_NUMBERS = sorted([1, 4, 13, 26, 27, 42])

personalRandomNumbers = sorted([6, 8, 24, 39, 41, 49])

print sorted(getMostFrequentNumbers(browser,6))
print sorted(getNumbersThatHaveNotBeenDrawnForALongTime(browser,6))
print sorted(getRandomlyDrawnNumbers(6))
print sorted(FAMILY_DEFINED_NUMBERS)
print sorted(PERSONAL_DEFINED_NUMBERS)
print sorted(personalRandomNumbers)

