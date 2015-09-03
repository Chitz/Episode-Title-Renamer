__author__ = 'chiteshtewani'

import urllib2, os, re, distutils.util
from bs4 import BeautifulSoup


def populateEpisodeList(episodeListURL):
    # get page
    html_page = urllib2.urlopen(episodeListURL)
    # instantiate BeautifulSoup object
    bSoup = BeautifulSoup(html_page, 'html.parser')
    seasonCount = 0
    for seasonTable in bSoup.find_all('table'):
        # assumption: Desired table has 8 columns; true in many cases
        if len(seasonTable.tr.find_all('th')) != 8:
            next
        else:
            episodeList.append([])
            # assumption: that title of the show is in class="summary"; true in many cases
            for episodeRow in seasonTable.select('[class~=summary]'):
                if len(episodeRow.contents) == 1:
                    episodeTitle = episodeRow.string
                else:
                    for refTag in episodeRow.select('[class~=reference]'):
                        refTag.clear()
                    episodeTitle = ''.join(episodeRow.stripped_strings)
                # print(episodeTitle)
                episodeList[seasonCount].append(episodeTitle)
            seasonCount += 1


def automateRename(parent_folder):
    for seasonFolder in os.walk(parent_folder).next()[1]:
        seasonIndex = int(re.search('[0-9]+', seasonFolder).group())
        for episode in os.walk(parent_folder + "/" + seasonFolder).next()[2]:
            episodeOG = filter(None, re.split('[^0-9]+', episode))
            episodeOG = list(set([int(i) for i in episodeOG]))
            episodeIndex = -1
            if len(episodeOG) != 1:
                for episodeOg_token in episodeOG:
                    if not (int(episodeOg_token) == seasonIndex or int(episodeOg_token) > 24):
                        episodeIndex = int(episodeOg_token)
            else:
                episodeIndex = int(episodeOG[0])
            if episodeIndex == -1:
                continue
            # rename
            confirm = raw_input("Do you wish to rename " + episode + " to " + episodeList[seasonIndex - 1][
                episodeIndex - 1] + " in season " + str(seasonIndex))
            print(episodeList[seasonIndex - 1][episodeIndex - 1])
            episodeRename = "s" + str(seasonIndex) + "e" + str(episodeIndex) + "-" + str(
                episodeList[seasonIndex - 1][episodeIndex - 1]).strip('"')
            if distutils.util.strtobool(confirm):
                os.rename(parent_folder + "/" + seasonFolder + "/" + episode,
                          parent_folder + "/" + seasonFolder + "/" + episodeRename)
            else:
                continue


# https://en.wikipedia.org/wiki/List_of_The_Big_Bang_Theory_episodes
# https://en.wikipedia.org/wiki/List_of_How_I_Met_Your_Mother_episodes
# https://en.wikipedia.org/wiki/List_of_Friends_episodes
parent_folder = "/Users/chiteshtewani/PycharmProjects/Automate-Episodes-TV-Shows/TV_SHOW"
episodeListURL = "https://en.wikipedia.org/wiki/List_of_How_I_Met_Your_Mother_episodes"
episodeList = []
populateEpisodeList(episodeListURL)
automateRename(parent_folder)
