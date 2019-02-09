# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request

URL = 'https://www.codewars.com/users/leaderboard'


def solution():
    # do it
    return Leaderboard()


class dotdict(dict):
    __getattr__ = dict.get


class Leaderboard:
    def __init__(self):
        self.position = {}
        for i, tr_tag in enumerate(
                BeautifulSoup(urllib.request.urlopen(URL).read(), 'html.parser')("tr", limit=11)[1:]):
            user = {'name': tr_tag['data-username']}
            # print(tr_tag)
            user['clan'], user['honor'] = [tag.text for tag in tr_tag('td')[2:]]
            user['honor'] = int(user['honor'].replace(',', ''))
            self.position[i + 1] = dotdict(user)
            # print(user)

        print(len(self.position), self.position[10])


if __name__ == '__main__':
    leaderboard = Leaderboard()
