import eventbrite_api_helper
import event_db_helper
from event_db_helper import EventDBHelper
from eventbrite_api_helper import EventBriteAPIHelper

class EventCreatorAndRetriever:
    '''A class that creates and retrieves event information'''

    def create_event(self, title, description, start_time_utc, end_time_utc):
        '''Creates an event using the Eventbrite API and adds it to the saved events database'''
        api_helper = eventbrite_api_helper.EventBriteAPIHelper()
        results = api_helper.create_event(title, description, start_time_utc, end_time_utc)

        event_id = results['id']
        event_url = results['url']

        db_helper = event_db_helper.EventDBHelper()
        db_helper.add_saved_event(event_id, title, event_url)


    def retrieve_saved_events(self):
        event_db_helper = EventDBHelper()
        return event_db_helper.retrieve_saved_events()

    def retrieve_event_info(self, event_id):
        eventbrite_api = EventBriteAPIHelper()
        results = eventbrite_api.get_event_information(event_id)

        event_title = results['name']['text']
        event_description = results['description']['text']
        last_changed_time = results['changed']
        currency_type = results['currency']

        event_info_string = f"Title: {event_title}\nDescription: {event_description}\nLast Changed Time: {last_changed_time}\nCurrency Type: {currency_type}"

        return event_info_string