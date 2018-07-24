#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def getTime(url):
    userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'
    headers = {'User_agent': userAgent}
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'lxml')
        soup = soup.find('ol')
        WBTime = soup.find('li', {'id': 'WBTime'}).get_text()
        PhotoTime = soup.find('li', {'id': 'PhotoTime'}).get_text()
        ExamTime = soup.find('li', {'id': 'ExamTime'}).get_text()
        ZYTime = soup.find('li', {'id': 'ZYTime'}).get_text()
        timeDict = {
            'WBTime': WBTime,
            'PhotoTime': PhotoTime,
            'ExamTime': ExamTime,
            'ZYTime': ZYTime}
        return judge(timeDict)


def judge(Dict):
    count = 0
    for item in Dict.values():
        if '2016' not in item:
            count += 1
    if count > 0:
        return Dict


def main():
    url = 'http://czwb.heao.gov.cn/CZService/default.aspx'
    timeDict = getTime(url)
    print(f"""{timeDict['WBTime']}
{timeDict['PhotoTime']}
{timeDict['ExamTime']}
{timeDict['ZYTime']}""")


if __name__ == '__main__':
    main()
