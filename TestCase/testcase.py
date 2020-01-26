from Lib.marvel_function import MarvelFunction
from testconfig import config
import unittest
from random import randint
from nose.plugins.attrib import attr
from nose.tools import with_setup
import nose


class TestMarvelApi(unittest.TestCase):

    def setUp(self):
        self.marvel_fun_object = MarvelFunction()

    @attr(type='smoke')
    def test_get_character_id_With_Description_and_series(self):
        """Test to get characters which has description and the list of Series those characters involved"""

        list_character_id = self.marvel_fun_object.get_character_id_with_description()
        list_series = self.marvel_fun_object.get_series_with_character_id(list_character_id)
        print(list_series)

    @attr(type='smoke')
    def test_get_list_of_characters_with_description_in_two_series(self):
        """Test to get characters which has description from the random two series from series list"""

        two_random_series_list = []
        list_character_id = self.marvel_fun_object.get_character_id_with_description()
        list_series = self.marvel_fun_object.get_series_with_character_id(list_character_id)

        value = randint(0, len(list_series))
        two_random_series_list.append(list_series[value])

        value = randint(0, len(list_series))
        two_random_series_list.append(list_series[value])
        while two_random_series_list[0] != two_random_series_list[1]:

            value = randint(0, len(list_series))
            two_random_series_list[1] = list_series[value]

        result = self.marvel_fun_object.get_list_of_characters_in_series(two_random_series_list)
        print(result)

    @attr(type='smoke')
    def test_get_list_of_stories_with_character_without_description(self):

        """Test to get the stories which has characters without description"""

        list_of_character_id_with_description = self.marvel_fun_object.get_character_id_with_description()
        result = self.marvel_fun_object.\
            get_list_of_stories_with_character_without_description()
        print(result)

