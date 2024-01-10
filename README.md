
# CouchSurfing - Test


## Installation and running instructions
To run the application you need to have Python (> 3.7) on your machine. Follow steps above:
    * pip install -r requirements.txt
    * connexion run swagger.yml
Test application and check behavior at http://127.0.0.1:5000/api/ui/

## General Approach

Create a well documented and easy to use API and showing some good practices while completing the exercise goal.
Here some notes about my approach:
    * Use connexion lib to simplify swagger implementation
    * Use seed data static
    * Implemented endpoints following REST principles (except for the relationship one that does not represent a resource)
    * Considered the list to be a simple hierarchy (not a graph)
    * Use lower ammount possible of external libs and a light web framework

## Possible Future improvements

To be fair, I ended my development with approximately 3 hours of coding due to breaks to attend to my current work.
I was unable to complete some requirements that I believe were necessary for the first version. Are they:
    * Check the relationship_id in the POST and PUT method to avoid circular references
    * Create a unit testing layer
    * Split the data access layer from business rule methods (user.py)

# Given Instructions

## General

    * Create a new repo on github.com
    * Please complete the following without leveraging code interpreter, copilot, etc.. to complete the key parts of the exercise. We want to see your style coming through.
    * Complete the exercise in whatever language you feel most comfortable in
    * Please limit the scope to the ask as much as possible and no more than 2 hours.
    * Reply to the email once complete with the link to the repo within 2 to 3 days.
    
## Requirements

Create a basic REST API that runs as a docker container and does the following:

    * Has a resource that is a user
    * User should have an attribute that describes its relationship to other user (think friends)
    * Seeds user data (static list or DB whichever is preferred)
    * Serves CRUD endpoints for the user resource
    * Has an additional endpoint that finds the relationship distance from one user to another user (this user is a 2nd, 3rd, distance relationship)
