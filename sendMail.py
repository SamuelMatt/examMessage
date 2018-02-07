#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib

fromAddrList = ['ms_achencer@189.cn', 'ms_achencer@wo.cn']
fromPasswd = 'mojiezuo_1991'
toAddr = ['mas_chencer@qq.com']
ccAddr = ['ms_achencer@qq.com', '164555837@qq.com']


def getFromServer(addr):
    return f'smtp.{addr.split("@")[-1]}'


def edit(fromAddr, Dict):
    text = f"""{Dict['WBTime']}
{Dict['PhotoTime']}
{Dict['ExamTime']}
{Dict['ZYTime']}"""
    message = MIMEText(text, 'plain', 'utf-8')
    message['Subject'] = 'Exam Message'
    message['From'] = fromAddr
    message['To'] = ','.join(toAddr)
    message['Cc'] = ','.join(ccAddr)
    return send(fromAddr, message)


def send(fromAddr, message):
    fromServer = getFromServer(fromAddr)
    server = smtplib.SMTP(fromServer, 25)
    server.login(fromAddr, fromPasswd)
    server.sendmail(fromAddr, toAddr + ccAddr, message.as_string())
    server.quit()


def sendMail(Dict):
    while  fromAddrList:
        fromAddr = fromAddrList.pop(0)
        try:
            edit(fromAddr, Dict)
            break
        except Exception:
            continue


def main():
    testDict = {
        'WBTime': 'Hello Matt,',
        'PhotoTime': 'Good morning;',
        'ExamTime': 'Hi Chencer,',
        'ZYTime': 'Good evening.'}
    sendMail(testDict)


if __name__ == '__main__':
    main()
