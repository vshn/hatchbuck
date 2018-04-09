import sys
sys.path.append('..')

from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.update('TmpmT0QyUGE3UGdGejZMay1xbDNyUHJFWU91M2VwN0hCdGtZZFFCaWRZczE1', {
    "firstName": "Hawar",
    "lastName": "Afrin",
    "title": "Hawar1",
    "company": "HAWAR",
    "emails": [
        {
            "address": "bashar.said.2018@gmail.com",
            "type": "work",
        }
    ],
    "phones": [
        {
            "number": "0041 76 803 77 34",
            "type": "work",
        }
    ],
    "status": {
        "name": "Employee",
    },
    "temperature": {
        "name": "Hot",
    },
    "addresses": [
        {
            "street": "Neugasse 10",
            "city": "Zürich",
            "state": "ZH",
            "zip": "8005",
            "country": "Switzerland",
            "type": "work",
        }
    ],
    "timezone": "W. Europe Standard Time",
    "socialNetworks": [
        {
            "address": "'https://twitter.com/bashar_2018'",
            "type": "Twitter",
        }
    ],
})
pp.pprint(profile)