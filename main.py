# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json


def postCitizenRegister():
    url = "https://tapktc.pvb4.com/ktcappsit/v1/custReg/citizenRegister"
    payload= "{\n\t\"Form\":[\n\t{\"FormHead\":{\n\t\t\"FormId\":\"CC030022I1\"\n\t    },\n\t    \"FormData\":\n\t    " \
             "{\n\t    \t\"CitizenId\":\"1100200021181\"\n\t    }\n\t\t}]\n} "
    headers = {
        'Content-Type': 'application/json',
        'deviceid': '367cfb5f32da41f9a43e775112e80c7f'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.text)

postCitizenRegister()

