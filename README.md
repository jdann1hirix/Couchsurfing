
# CouchSurfing - Test


## Installation

## General Instructions

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

## General Approach

Create a well documented and easy to use API and showing some good practices while completing the exercise goal.
Here some notes about my approach:
    * Use connexion lib to simplify swagger implementation
    * Use seed data static
    * Implemented endpoints following REST principles (except for the relationship one that does not represent a resource)
    * Considered the list to be a simple hierarchy (not a graph)

## Possible Future improvements

## Enviroment used

