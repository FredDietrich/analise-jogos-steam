#!/usr/bin/python3
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime

def getDataFromDom(gameDom):
    labels = [{"keyInPage": "Release dates", "finalKey": "release_date"}, {"keyInPage": "Developers", "finalKey": "developer"}, {"keyInPage": "Publishers", "finalKey": "publisher"}]
    foundData = {}
    for label in labels:
        elem = gameDom.xpath(f'//th[contains(text(), "{label["keyInPage"]}")]/../following-sibling::tr[1]/td[2]')[0]
        data = ""
        if (len(elem.getchildren()) > 0):
            data = elem.getchildren()[len(elem.getchildren()) - 1].text
        else:
            data = elem.text
        foundData[label["finalKey"]] = data
    genres = ""
    for genre in gameDom.xpath("//td[contains(text(), 'Genres')]/following-sibling::td/a/abbr"):
        genres += genre.text + ","
    foundData["genres"] = genres
    return foundData

def getReleaseDateForGamePage(page: str):
    gameSoup = BeautifulSoup(page, 'html.parser')
    gameDom = etree.HTML(str(gameSoup))
    try:
        return getDataFromDom(gameDom)
    except:
        return ""


def getMissingDataForGameByName(gameName: str, retryCount=0):
    if (retryCount > 0):
        gameName = re.sub('[^A-Za-z0-9]+', ' ', gameName)
    if (retryCount > 2):
        return ""
    gamePage = requests.get(
        'https://www.pcgamingwiki.com/w/index.php?search=' + gameName).text
    gameSoup = BeautifulSoup(gamePage, 'html.parser')
    gameDom = etree.HTML(str(gameSoup))
    try:
        return getDataFromDom(gameDom)
    except:
        try:
            gameUrl = gameDom.xpath(
                "(//span[contains(text(), 'Page title matches')]/../..//ul[1]//a)[1]")[0].get('href')
            gamePage = requests.get(f"https://www.pcgamingwiki.com/{gameUrl}").text
            return getReleaseDateForGamePage(gamePage)
        except:
            return getMissingDataForGameByName(gameName, retryCount=retryCount + 1)


gamesDF = pd.read_csv('inputData/games_data.csv',
                      delimiter=',', low_memory=False)

missingDateCounter = 0

try:
    for line in gamesDF.itertuples():
        if (line.Index > 20):
            break
        if (pd.isna(line.release_date)):
            missingDateCounter += 1
            missingData = getMissingDataForGameByName(line.title)
            for missingDataI in missingData:
                if missingDataI == "release_date":
                    missingData[missingDataI] = datetime.strptime(missingData[missingDataI], "%B %d, %Y").strftime("%Y-%m-%d")
                gamesDF.loc[line.Index, missingDataI] = missingData[missingDataI]
            print(f"Processando jogo {line.Index} - {line.title}")
    gamesDF.to_csv("outputData/processado.csv", index=False)
except KeyboardInterrupt:
    gamesDF.to_csv("outputData/processado.csv", index=False)
