import unittest
import sys
sys.path.append('..')

from hatchbuck import Hatchbuck

class TestHatchbuck(unittest.TestCase):
    global testProfile
    testProfile = {'addresses': [{'city': 'Zürich',
                                  'country': 'Switzerland',
                                  'countryId': 'QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1',
                                  'id': 'Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1',
                                  'state': 'ZH',
                                  'street': 'Neugasse 10',
                                  'type': 'Work',
                                  'typeId': 'SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1',
                                  'zip': '8005'}],
                   'campaigns': [],
                   'company': 'VSHN AG',
                   'contactId': 'SUFYbGdOaEQ0cWR2N1JfV183UFNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1',
                   'customFields': [{'name': 'Comments', 'type': 'MText', 'value': ''},
                                    {'name': 'Invoiced', 'type': 'Number', 'value': ''},
                                    {'name': 'Language', 'type': 'Text', 'value': ''},
                                    {'name': 'working at company since',
                                     'type': 'Text',
                                     'value': '1.1.2018'},
                                    {'name': 'company size', 'type': 'Text', 'value': '25'},
                                    {'name': 'Birthday', 'type': 'Date', 'value': ''}],
                   'emails': [{'address': 'bashar.said@vshn.ch',
                               'id': 'S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5ZFVENGVHTG1DODE1',
                               'type': 'Work',
                               'typeId': 'VmhlQU1pZVJSUFFJSjZfMHRmT1laUmwtT0FMNW9hbnBuZHd2Q1JTdE0tYzE1'}],
                   'firstName': 'Bashar',
                   'instantMessaging': [],
                   'lastName': 'Said',
                   'phones': [{'id': 'OHh4U0ZWc3FNVXVBQVF4cjdsak9McWc4TVppZlF4NklrNmZfSnBhaDZwQTE1',
                               'number': '+(414) 454-5 53 00',
                               'type': 'Work',
                               'typeId': 'QTBncHV0dndnaGNnRVMzLTR0SGtFRmRvZjdqNm4zcVphQi1XX1Z2MXVtRTE1'}],
                   'referredBy': '',
                   'salesRep': {'id': 'VGpwQTRGTmw4MExVODl1b1BmXzBodTBwWnZXS2dUZzVvSkJKZUx4UlFpdzE1',
                                'username': 'aarno.aukia'},
                   'socialNetworks': [{'address': 'https://twitter.com/bashar_2018',
                                       'id': 'S1pEM2NMWlhmZ1VUcDhTUWVvQy1kU21xMjlSbDg5Z3piMERVbEFsam42azE1',
                                       'typeId': 'ZGRlMHpBaXY3M05YUGc4a0pIY3lRdUFKN1JYaDd2VEphbzhSRkdzM2x4bzE1'}]}

    def setUp(self):
        pass

    def test_profile_add_address(self):
        hatchbuck = Hatchbuck('abc123')
        existingaddress = {'street': "Neugasse 10",
             'zip_code': "8005",
             'city': "Zürich",
             'country': "Switzerland"}
        # We're trying to add an address that is already there
        # Check that the address is there already
        self.assertTrue(hatchbuck.address_exists(testProfile, {
            'street': existingaddress['street'],
            'zip': existingaddress['zip_code'],
            'city': existingaddress['city'],
            'country': existingaddress['country'],
            'type': 'Work',
        }))

        # try to add the address again
        profile = hatchbuck.profile_add_address(testProfile,
                                                existingaddress,
                                                "Work"
        )

        # Check that the address is still there
        self.assertTrue(hatchbuck.address_exists(profile, {
            'street': existingaddress['street'],
            'zip': existingaddress['zip_code'],
            'city': existingaddress['city'],
            'country': existingaddress['country'],
            'type': 'Work',
        }))

        # check that the profile was not modified by trying to add an existing address
        self.assertTrue(profile == testProfile)

        # We can't test adding an address offline
        # # adding a new address
        # newaddress = {'street': "Bahnhofstrasse 1",
        #      'zip_code': "8001",
        #      'city': "Zürich",
        #      'country': "Switzerland"}
        #
        # self.assertFalse(hatchbuck.address_exists(profile, {
        #     'street': newaddress['street'],
        #     'zip': newaddress['zip_code'],
        #     'city': newaddress['city'],
        #     'country': newaddress['country'],
        #     'type': 'Home',
        # }))
        #
        # profile = hatchbuck.profile_add_address(testProfile,
        #                                         newaddress,
        #                                         "Home"
        # )
        # print(len(profile['addresses']))
        # print(profile)
        # self.assertTrue(len(profile['addresses']) == 2)
        #
        # self.assertTrue(hatchbuck.address_exists(profile, {
        #     'street': newaddress['street'],
        #     'zip': newaddress['zip_code'],
        #     'city': newaddress['city'],
        #     'country': newaddress['country'],
        #     'type': 'Home',
        # }))


    def test_profile_contains(self):
        hatchbuck = Hatchbuck('abc123')
        profile = hatchbuck.profile_contains({
            "contactId": "SUFYbGdOaEQ0cWR2N1JfV183UFNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1",
            "phones": [
                {
                    "number": "+(414) 454-5 53 00",
                    "type": "work",
                }
            ]
        }, "phones", "number", "+(414) 454-5 53 00")
        self.assertTrue(profile, testProfile)


    def test_add_tag(self):
        hatchbuck = Hatchbuck('abc123')
        profile = hatchbuck.add_tag('SUFYbGdOaEQ0cWR2N1JfV183UFNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1', '')
        self.assertFalse(profile, testProfile)

    def test_profile_add_birthday(self):
        hatchbuck = Hatchbuck('abc123')
        profile = hatchbuck.profile_add_birthday({
            "contactId": "TmpmT0QyUGE3UGdGejZMay1xbDNyUHJFWU91M2VwN0hCdGtZZFFCaWRZczE1"},
            {'month': '1', 'day': '1', 'year': '1984'})
        self.assertTrue(profile, testProfile)


if __name__ == '__main__':
    unittest.main()
