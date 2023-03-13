import unittest
import inspect
import event_creator_and_retriever
import event_db_helper
import eventbrite_api_helper


class TestEventCreatorAndRetriever(unittest.TestCase):
    def test_create_event(self):
        instance = event_creator_and_retriever.EventCreatorAndRetriever()
        source = inspect.getsource(instance.create_event)
        
        if '.create_event(' not in source:
            raise AssertionError('We expected the create_event method to call a method called create_event (on an api_helper instance)')
        
        if '.add_saved_event(' not in source:
            raise AssertionError('We expected the create_event method to call a method called add_saved_event (on a db_helper instance)')
        
    def test_retrieve_saved_events(self):
        instance = event_creator_and_retriever.EventCreatorAndRetriever()
        source = inspect.getsource(instance.retrieve_saved_events)
        if '.retrieve_saved_events(' not in source:
            raise AssertionError('We expected the retrieve_saved_events method to call a method called retrieve_saved_events (on an db_helper instance)')
    
    def test_retrieve_event_info(self):
        instance = event_creator_and_retriever.EventCreatorAndRetriever()
        source = inspect.getsource(instance.retrieve_event_info)
        if '.get_event_information(' not in source:
            raise AssertionError('We expected the retrieve_event_info method to call a method called get_event_information (on an api_helper instance)')
        
class TestEventDBHelper(unittest.TestCase):
    def test_SavedEvent(self):
        instance = event_db_helper.SavedEvent()
        assert instance.__tablename__ == "SavedEvents"
        assert 'eventbrite_id' in dir(instance)
        assert 'title' in dir(instance)
        assert 'url' in dir(instance)
    
    def test_EventDBHelper(self):
        instance = event_db_helper.EventDBHelper()
        source = inspect.getsource(instance.__init__)
        
        if 'self.session' not in source:
            raise AssertionError('We expected the init method of EventDBHelper to refer to self.session')

class TestEventBriteAPIHelper(unittest.TestCase):    
    def test_get_organization_id(self):
        instance = eventbrite_api_helper.EventBriteAPIHelper()
        source = inspect.getsource(instance.get_organization_id)
        
        if "'get'" not in source.lower() and '"get"' not in source.lower():
            raise AssertionError('We expected the get_organization_id method of EventBriteAPIHelper to refer to "GET"')
        
        if 'Request(' not in source:
            raise AssertionError('We expected the get_organization_id method of EventBriteAPIHelper to create a Request')
        
        if 'urlopen(' not in source:
            raise AssertionError('We expected the get_organization_id method of EventBriteAPIHelper to call urlopen')
    
    def test_get_event_information(self):
        instance = eventbrite_api_helper.EventBriteAPIHelper()
        source = inspect.getsource(instance.get_event_information)
        
        if 'Request(' not in source:
            raise AssertionError('We expected the get_event_information method of EventBriteAPIHelper to create a Request')
        
        if 'urlopen(' not in source:
            raise AssertionError('We expected the get_event_information method of EventBriteAPIHelper to call urlopen')
    
    def test_create_event(self):
        instance = eventbrite_api_helper.EventBriteAPIHelper()
        source = inspect.getsource(instance.create_event)
        
        if "'post'" not in source.lower() and '"post"' not in source.lower():
            raise AssertionError('We expected the get_organization_id method of EventBriteAPIHelper to refer to "POST"')
        
        if 'Request(' not in source:
            raise AssertionError('We expected the get_organization_id method of EventBriteAPIHelper to create a Request')
        
        if 'urlopen(' not in source:
            raise AssertionError('We expected the get_organization_id method of EventBriteAPIHelper to call urlopen')
    

if __name__ == "__main__":
    unittest.main()
