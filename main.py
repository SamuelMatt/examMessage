#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collection import getTime
from sendMail import sendMail


def main():
    url = 'http://czwb.heao.gov.cn/CZService/default.aspx'
    timeDict = getTime(url)
    if timeDict:
        sendMail(timeDict)


if __name__ == '__main__':
    main()
