import json


class ConfigReader:
    def __init__(self):
        self.daily_run_time = ""
        self.hosts = []

    def read(self, file_path):
        with open(file_path) as data_file:
            config = json.load(data_file)

        self.daily_run_time = config["dailyRunTime"]
        self.hosts = config["hosts"]