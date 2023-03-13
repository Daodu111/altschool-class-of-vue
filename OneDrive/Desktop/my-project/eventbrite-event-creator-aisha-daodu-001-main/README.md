# EventBrite Event-Creator

*You'll make an app that lets you create an event on the real EventBrite.com website.*

## Introduction

Welcome to the Kibo Programming-2 final project!

The theme for this project is putting together the pieces. You'll first work on each piece, and then once each piece is finished, you will put the pieces together to complete the app.

<img src="files/puzzle.png" width="40%" height="40%" />

### Piece 1: Get an API Key

Please sign up for an eventbrite API key. Here are the steps:

* Go to eventbrite.com and create an account, then Sign In
* Under Account settings, click on Developer Links and go to the API Keys page
* Click the "Create API Key" button in the top right
* Fill out the form to request an API key, and submit it
  - For application url, enter `https://kibo.school`
  - For application name, enter `Kibo programming 2 project`
  - For description, enter `Project for programming 2`
* Wait a few seconds,
* Click "Show API Key, client secret, and tokens"
* Copy the "private token".
* Create a file in inside the `files` directory of the project (right next to the files like `cli.py`) called `apikey.txt`.
* Paste the "private token" into the `apikey.txt` file and save it.
* Note that `apikey.txt` will be ignored by git. You can't `git add` it and it won't be uploaded as part of your project.
* (There will be some Python code that reads the contents of `apikey.txt`)
* (Please reach out for assistance if you are having trouble with this part, it's just a matter of navigating the EventBrite website.)

### Piece 2: Reading helper code

(You don't have to write any code for this part, just read the code and see what it does).

Please open `helpers.py` and quickly read through the functions there. You will use the functions here when you build your project.

For example, `get_api_key` reads the contents of the apikey.txt file you created earlier.

### Piece 3: Write code that makes an API call

* Edit `eventbrite_api_helper.py`
* Complete the `get_event_information` method as the comments describe it.
* Complete the `create_event` method as the comments describe it.
* (see `get_organization_id` for an example of how to send a request)

### Piece 4: Write code that saves to a database

* Edit `event_db_helper.py`
* Complete the `SavedEvent` class as the comments describe it.
* Complete the `EventDBHelper __init__` method as the comments describe it.

### Final step: Putting the pieces together

* Now you'll create the real program.
* Please open `cli.py` in the files directory. You can read the code and see what it does.
* Try running `cli.py`. It won't work yet, because there isn't an `event_creator_and_retriever` file to import yet.
* So, create a file named `event_creator_and_retriever.py`
* Add imports for your other files: `eventbrite_api_helper`, and `event_db_helper`.
* Create a class named EventCreatorAndRetriever
  * This class will use eventbrite_api_helper and event_db_helper to create and retrieve event information.
  * Create a method called `create_event`
    * that takes a title, description, start_time_utc, and end_time_utc (and also self, which every method has as the first parameter).
    * get an instance of `eventbrite_api_helper.EventBriteAPIHelper`
    * use that instance to call create_event, passing it the title, description, start_time_utc, and end_time_utc.
    * get the results from create_event. you can access `results['id']` and `results['url']`
    * next, get an instance of `event_db_helper.EventDBHelper`
    * use that instance to call `add_saved_event` and pass in the id, title, and url

  * Create a method called `retrieve_saved_events`
    * does not need any parameters (except self, which every method has as the first parameter)
    * use an instance of `event_db_helper.EventDBHelper` to call `retrieve_saved_events`
    * and returns the results

  * Create a method called `retrieve_event_info`
    * that takes a event_id (and self, which every method has as the first parameter)
    * use an instance of `eventbrite_api_helper.EventBriteAPIHelper`
    * to call get_event_information on that event_id.
    * then, make a string that displays the results from get_event_information to the user,
    * add the title (`results['name']['text']`)
    * and the description (`results['description']['text']`)
    * and the last changed time (`results['changed']`)
    * and the currency type (`results['currency']`)
    * finally, return the string.

* Try running `cli.py` . It will now be able to create an instance of a EventCreator and run the program. The program might not work on the first try. That's OK, you can debug any issues and keep fixing it until everything works!
* When the program works, it will create real events on the eventbrite website. (And you can see them on the website as long as you are logged in).
* When you're done, add a try/catch to the `create_event` method, so any problems sending the request don't cause the app to crash.

## Rubric

| Points | Criteria                           | Description                                                                                     |
| ------ | ---------------------------------- | ----------------------------------------------------------------------------------------------- |
| 20     | Get event information                 | The get_event_information method is complete                                               |
| 20     | Create event                 | The create_event  method is complete                                               |
| 20     | SavedEvent class                | The SavedEvent class is complete                                               |
| 10     | EventDBHelper init | The EventDBHelper init method is complete                                               |
| 10     | User can create events | The EventCreatorAndRetriever create_event method is complete                                               |
| 10     | User can retrieve events from db | The EventCreatorAndRetriever retrieve_saved_events method is complete                                               |
| 10     | User can retrieve one event from api | The EventCreatorAndRetriever retrieve_event_info method is complete                                               |


### Explore more

Here are some fun ways to explore and extend your app. (These are optional and won't be graded.)

* It's common for an event organiser to create an event that is similar to an event that has already been created. You could add a new feature called "Create event based on previous event" that still asks for the date and time, but re-uses the same title and description as a SavedEvent that the user already made.
* You could read the documentation <a href="https://www.eventbrite.com/platform/api#/reference/event/publish/publish-an-event">here</a> on how to send a POST request to mark the event as "published". After the event has been published it can be seen by everyone online. You could create another account on eventbrite.com using a different email address. Then browse to the new event you created, as if you were someone wanting to attend the event. You could now click in the webpage and add yourself as "attending", since it is now a fully published event.


