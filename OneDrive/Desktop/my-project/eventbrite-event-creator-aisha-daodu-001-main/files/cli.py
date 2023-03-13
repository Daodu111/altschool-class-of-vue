
import sys
import event_creator_and_retriever
import helpers

# This code is provided for you, you don't need to change any of the code here.

class EventBriteEventCreatorCli:
    '''A command-line interface for a program that creates eventbrite.com events'''
    
    def __init__(self):
        '''Students will write this EventCreatorAndRetriever class'''
        self.creator_and_retriever = event_creator_and_retriever.EventCreatorAndRetriever()
        
    def main_menu(self):
        '''Show the main menu'''
        while True:
            chosen = self.show_menu([
                'Create event',
                'Show saved events',
                'Exit',
            ])
            
            if chosen == 0:
                self.start_create_event()
            elif chosen == 1:
                self.start_show_saved_events()
            elif chosen == 2:
                return
            
    def start_create_event(self):
        '''Called when the user wants to create an event'''
        title = input('Title: ')
        description = input('Description: ')
        start_time_utc, end_time_utc = helpers.get_formatted_day_and_time()
        self.creator_and_retriever.create_event(title, description, start_time_utc, end_time_utc)
        print('\nEvent was created\n')
    
    def start_show_saved_events(self):
        '''Called when the user wants to show existing events'''
        event_db_helper = self.creator_and_retriever.retrieve_saved_events()
        titles = []
        for event in event_db_helper:
            titles.append(event.title)
        
        if not titles:
            print('\nNo saved events yet\n')
            return
        
        print('Choose an event to see all of the details:')
        chosen_number = self.show_menu(titles)
        chosen_row = event_db_helper[chosen_number]
        information = self.creator_and_retriever.retrieve_event_info(chosen_row.eventbrite_id)
        print(information)
        
        open_in_browser = input('Open in browser? y/n ')
        if open_in_browser.strip() == 'y':
            helpers.open_url_in_browser(chosen_row.url)

        input('Press Enter to continue')
    
    def show_menu(self, lst):
        '''A helper method that shows a list of choices.
        Returns an integer (the index of the chosen item).'''
        for i, item in enumerate(lst):
            print(f'{i+1}) {item}')
            
        chosen = input('Please choose from the list above: ')
        chosen = int(chosen)
        
        # when we show the user, display the first item as 1. for python though, the first item is 0.
        chosen -= 1
        
        if chosen < 0 or chosen >= len(lst):
            print('Not a valid choice')
            sys.exit(1)
            
        return chosen

if __name__ == '__main__':
    cli = EventBriteEventCreatorCli()
    cli.main_menu()

