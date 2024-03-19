class Record:
    def __init__(self, timestamp, deaths_num, births_num):
        self._timestamp = timestamp
        self._deaths_num = deaths_num
        self._births_num = births_num

    def get_timestamp(self):
        return self._timestamp
    def get_deaths(self):
        return self._deaths_num
    def get_births(self):
        return self._births_num