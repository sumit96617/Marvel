import requests
from testconfig import config
import json
import math
import time


class MarvelFunction:

    def __init__(self):
        self.params = {'apikey': config['authorization_key']['public_authorization_key'],
                       'ts': config['time']['time_stamp'],
                       'hash': config['hash']['hash_key'], 'limit': config['limit']['default_limit']}

    def get_character_id_with_description(self):
        """Getting the Character id which has no description in the response """

        list_of_character_id = []
        url = config['url']['base_url'] + config['character_url']['get_characters']
        response = requests.get(url, params=self.params).json()

        total_number_of_entry_in_table = response['data']['total']

        per_page_limit = response['data']['limit']
        total_number_of_offset = math.ceil(total_number_of_entry_in_table / per_page_limit)

        for i in range(total_number_of_offset):

            self.params['offset'] = i
            response = requests.get(url, params=self.params).json()
            total_number_of_characters = len(response['data']['results'])

            for j in range(total_number_of_characters):

                if response['data']['results'][j]['description'] != "":
                    list_of_character_id.append(response['data']['results'][j]['id'])

        return list_of_character_id

    def get_series_with_character_id(self, character_list=None):

        list_of_series_id = []
        for i in range(len(character_list)):

            url = config['url']['base_url'] + config['character_url']['get_characters'] + '/' + str(
                character_list[i]) + config['series_url']['base_series']
            response = requests.get(url, params=self.params).json()
            total_number_of_entry_in_table = response['data']['total']

            per_page_limit = response['data']['limit']
            total_number_of_offset = math.ceil(total_number_of_entry_in_table / per_page_limit)

            for j in range(total_number_of_offset):
                self.params['offset'] = j
                response = requests.get(url, params=self.params).json()
                total_number_of_series = len(response['data']['results'])

                if len(response['data']['results']) != 0:

                    for k in range(len(response['data']['results'])):
                        list_of_series_id.append(response['data']['results'][k]['id'])

        return list_of_series_id

    def get_list_of_characters_in_series(self, series_list):

        list_of_character_id_in_series = []

        for i in range(len(series_list)):

            url = config['url']['base_url'] + config['series_url']['get_series'] + '/' + str(
                series_list[i]) + config['character_url']['base_characters']

            response = requests.get(url, params=self.params).json()
            total_number_of_entry_in_table = response['data']['total']

            per_page_limit = response['data']['limit']
            total_number_of_offset = math.ceil(total_number_of_entry_in_table / per_page_limit)

            for i in range(total_number_of_offset):
                self.params['offset'] = i
                response = requests.get(url, params=self.params).json()
                total_number_of_series = len(response['data']['results'])

                if len(response['data']['results']) != 0:

                    for j in range(len(response['data']['results'])):
                        list_of_character_id_in_series.append(response['data']['results'][j]['id'])

        return list_of_character_id_in_series

    def get_list_of_stories_with_character_without_description(self, charcters_with_description_list=None):

        list_of_stories_without_character_description = []

        url = config['url']['base_url'] + config['stories_url']['base_stories']
        response_stories = requests.get(url, params=self.params).json()
        total_number_of_stories = len(response_stories['data']['results'])

        for i in range(total_number_of_stories):

            url = config['url']['base_url'] + config['stories_url']['base_stories'] + '/' \
                  + str(response_stories['data']['results'][i]['id']) + config['character_url']['base_characters']

            response_characters = requests.get(url, params=self.params).json()
            total_number_of_entry_in_table = response_characters['data']['total']
            per_page_limit = response_characters['data']['limit']
            total_number_of_offset = math.ceil(total_number_of_entry_in_table / per_page_limit)

            for j in range(total_number_of_offset):
                self.params['offset'] = j
                response = requests.get(url, params=self.params).json()

                if len(response['data']['results']) != 0:

                    for k in range(len(response['data']['results'])):
                        count = 0
                        if response['data']['results'][k]['id'] in charcters_with_description_list:
                            count = 1
                            break

                    if count == 1:
                        list_of_stories_without_character_description.append(total_number_of_stories[i])

        return list_of_stories_without_character_description
