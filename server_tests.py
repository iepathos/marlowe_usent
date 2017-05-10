#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import server
import unittest


class ServerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()

    def tearDown(self):
        pass

    def test_objectivity(self):
        data = {
            'text': 'This is some random text.',
        }
        expected_data = {
            "objectivity": 1.0
        }
        response = self.app.post('/', data=data, follow_redirects=True)
        response_json = json.loads(response.data)
        assert(response_json == expected_data)

    def test_integer_objectivity(self):
        data = {
            'text': 100,
        }
        expected_data = {
            "objectivity": 1.0
        }
        response = self.app.post('/', data=data, follow_redirects=True)
        response_json = json.loads(response.data)
        assert(response_json == expected_data)

    def test_ascii_objectivity(self):
        data = {
            'text': u'\u2019',
        }
        expected_data = {
            "objectivity": 1.0
        }
        response = self.app.post('/', data=data, follow_redirects=True)
        response_json = json.loads(response.data)
        assert(response_json == expected_data)

    def test_empty_text(self):
        data = {
            'wrong': 'Empty text field',
        }
        expected_data = {
            "objectivity": 1.0
        }
        response = self.app.post('/', data=data, follow_redirects=True)
        response_json = json.loads(response.data)
        assert(response_json == expected_data)

    def test_sentence_starting_with_whitespace(self):
        data = {
            'wrong': ' try to get loud please',
        }
        expected_data = {
            "objectivity": 1.0
        }
        response = self.app.post('/', data=data, follow_redirects=True)
        response_json = json.loads(response.data)
        assert(response_json == expected_data)


if __name__ == '__main__':
    unittest.main()
