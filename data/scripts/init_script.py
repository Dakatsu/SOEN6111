import json
import time 
import pandas as pd
import os

url_to_get_all_apps = "https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json"
url_to_get_app_information="https://store.steampowered.com/api/appdetails?appids="
dictionnary = {}
path = os.getcwd()
directory_path=os.path.abspath(os.path.join(path, os.pardir))
parentPath = os.path.abspath(os.path.join(directory_path,os.pardir))


def generateData():
    with open('successful_appIDs.txt') as file:
        valid_appIds = [app_id.strip() for app_id in file.readlines()]

    for app_id in valid_appIds:
        json_obj = json.load(open(path+"/appdetails/appID_" + app_id+'.json'))
        if 'type' not in json_obj or json_obj['type']!= 'game' or 'developers' not in json_obj or 'required_age' not in json_obj or 'publishers' not in json_obj or 'genres' not in json_obj:
            continue
        if json_obj['is_free'] == False and 'price_overview' in json_obj :
            price = json_obj['price_overview']['final']/100
        else:
            price = 0
        dictionnary[app_id] = {
                    "name": json_obj['name'],
                    "free_to_play":json_obj['is_free'],
                    "price":price,
                    "required_age": json_obj['required_age'],
                    "developers": '-'.join([str(elem) for elem in json_obj['developers']]),
                    "publishers": '-'.join([str(elem) for elem in json_obj['publishers']]),
                    "genres":'-'.join([str(elem['description']) for elem in json_obj['genres']]),
                    "release_date": json_obj['release_date']['date'],
        }
    
    df = pd.DataFrame.from_dict(dictionnary, orient='index')
    df.index.name = 'appID'
    path_to_write = './data/datasets'
    if not os.path.exists(path_to_write):
        os.mkdir('./data/datasets')
    
    df.to_csv('./data/datasets/games.csv') 


def fetchMissingData(dataframe:pd.DataFrame):
    return dataframe


if __name__ == '__main__':
    generateData()