
from urllib import request
import json
import helpers


class EventBriteAPIHelper:
    '''Methods that send/receive data to the eventbrite.com api'''
    
    def get_organization_id(self):
        # (gets the "organization id" of our eventbrite.com account)
        token = helpers.get_api_key()
        url = f'https://www.eventbriteapi.com/v3/users/me/organizations/?token={token}'
        request_object = request.Request(url, method="GET")
        request_object.add_header('Content-Type', 'application/json')
        opened_request = request.urlopen(request_object, data=None)
        result = opened_request.read().decode('utf-8')
        parsed = json.loads(result)
        
        return parsed['organizations'][0]['id']

    def get_event_information(self, event_id):
        # TODO:
        # write a method to use the eventbrite api to retrieve information about an event:
        # use the same code as get_organization_id()
        # except the url is f'https://www.eventbriteapi.com/v3/events/{event_id}/?token={token}'
        # and return the entire parsed dict from json.loads
        '''Retrieve information about an event'''
        token = helpers.get_api_key()
        url = f'https://www.eventbriteapi.com/v3/events/{event_id}/?token={token}'
        request_object = request.Request(url, method="GET")
        request_object.add_header('Content-Type', 'application/json')
        opened_request = request.urlopen(request_object, data=None)
        result = opened_request.read().decode('utf-8')
        parsed = json.loads(result)

        return parsed
        
        # TODO:
        # write a method to use the eventbrite api to retrieve information about an event:
        # use the same code as get_organization_id()
        # except the url is f'https://www.eventbriteapi.com/v3/events/{event_id}/?token={token}'
        # and return the entire parsed dict from json.loads

    
    def create_event(self, title, description, start_time_utc, end_time_utc):
        '''Create a new event'''
        organization_id = self.get_organization_id()
        
        # the reason we place the data in a dictionary that looks like this is that
        # the eventbrite api documents the structure here,
        # https://www.eventbrite.com/platform/api#/reference/event/create/create-an-event
        data = {
        "event": {
            "currency": "USD",
            "name": {
                "html": title
            },
            "description": {
                "html": description
            },
            "start": {
                "timezone": "UTC",
                "utc": start_time_utc
            },
            "end": {
                "timezone": "UTC",
                "utc": end_time_utc
            },
        }
    }

        data = json.dumps(data)
        data = data.encode()

        token = helpers.get_api_key()
        url = f'https://www.eventbriteapi.com/v3/organizations/{organization_id}/events/?token={token}'
        request_object = request.Request(url, method="POST")
        request_object.add_header('Content-Type', 'application/json')
        opened_request = request.urlopen(request_object, data=data)
        result = opened_request.read().decode('utf-8')
        parsed = json.loads(result)

        return parsed

        # TODO:
        # add code here to use the eventbrite api to tell it to create a new event:
        # use the same code as get_organization_id()
        # except the url is f'https://www.eventbriteapi.com/v3/organizations/{organization_id}/events/?token={token}'
        # and when calling request.Request use method='POST' instead of method='GET'
        # and when calling request.urlopen use data=data instead of data=None
        # return the entire parsed dict from json.loads
        
