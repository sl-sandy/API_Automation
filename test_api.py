__author__ = 'HSL'
import unittest
import urllib.request
import json


class TestApi(unittest.TestCase):

    def test_api(self):
        test_url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
        json_result = self.get_response_json(test_url)
        self.assertEqual(json_result['Name'], 'Carbon credits', 'Criteria 1 failed')
        self.assertEqual(json_result['CanRelist'],True,'Criteria 2 failed')
        for each_element in json_result['Promotions']:
            if 'Name' in each_element and each_element['Name'] == 'Gallery':
                self.assertIn('Description', each_element, 'Criteria 3 do not have a Description')
                self.assertIn('2x larger image', each_element['Description'], 'Criteria 3 failed')

    @staticmethod
    def get_response_json(get_url):
        res = urllib.request.urlopen(get_url).read()
        return json.loads(res.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()