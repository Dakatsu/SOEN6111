import json
import requests
import time 
import pandas as pd
import os

url_to_get_all_apps = "https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json"
url_to_get_app_information="https://store.steampowered.com/api/appdetails?appids="
dictionnary = {}
path = os.getcwd()
directory_path=os.path.abspath(os.path.join(path, os.pardir))

def generateData():
    response = requests.get(url_to_get_all_apps)
    time.sleep(2.5)
    jsonObjectArray = response.json()['applist']['apps']
    for app in jsonObjectArray:
        appid = str(app['appid'])
        fetch_url = url_to_get_app_information+appid
        
        response = requests.get(fetch_url)
        try:
            response = response.json()
        except:
            continue
        if response == None:
            continue
        response = response[appid]
        if response['success']:
            dataVal = response['data']
            if dataVal['type'] == 'game':
                if dataVal['is_free']:
                    price = 0
                else: 
                    if 'price_overview' in dataVal:
                        price = dataVal['price_overview']['initial']/100
                    else:
                        price = 0
                if  "metacritic" not in dataVal:
                    metacritic = 0
                else:
                    metacritic = dataVal['metacritic']['score']
                if "recommendation" not in dataVal:
                    dataVal['recommendations']={'total':0}
                if "developers" not in dataVal:
                    continue
                objectVal = {
                    "name": dataVal['name'],
                    "price":price,
                    "required_age": dataVal['required_age'],
                    "developers": ','.join([str(elem) for elem in dataVal['developers']]),
                    "publishers": ','.join([str(elem) for elem in dataVal['publishers']]),
                    "rating": metacritic,
                    "genres":','.join([str(elem['description']) for elem in dataVal['genres']]),
                    "release_date": dataVal['release_date']['date'],
                    "numberOfRecommendations": dataVal['recommendations']['total']
                }
                print("***"*100)
                try:
                    print(objectVal)
                except:
                    print('\n')
                dictionnary[appid]= objectVal
        time.sleep(5)
    df = pd.DataFrame.from_dict(dictionnary, orient='index')
    df.to_csv(directory_path + '/datasets/games.csv') 





if __name__ == '__main__':
    generateData()