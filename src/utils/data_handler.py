import json
from src.activity.activity_model import Activity
from src.utils.constants import ACTIVITIES_JSON_PATH


class DataHandler:
    @staticmethod
    def get_activities():
        # load json data from file
        jsonData = json.load(open(ACTIVITIES_JSON_PATH))
        activities = []

        # convert json data to Activity objects
        for act in jsonData:
            activities.append(Activity(act))
            
        # delete the json data from memory
        del jsonData

        return activities