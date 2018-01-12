## Divercity
Divercity is a web application that helps you find gender-free bathrooms.
Gender-free bathrooms can provide a safer environment for transgender people or people that don't want to define their gender.

## Motivations
The idea of the project comes from a big problem that cities have nowadays, which is the separation of bathrooms by gender (Men/Women). Our aim is to increase the number of gender-free bathrooms, to which everybody can go to without the need of defining their gender. 

## License
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
## Logo
![alt text](https://github.com/Divercity/Divercity/blob/master/static/img/logo.jpg)

## Used technologies/frameworks
The website is running on Flask (a Python micro framework), HTML5, JavaScript and Bootstrap. The database we have chosen for storing the data is MongoDB.

<b>Done with:</b>
- [Flask](http://flask.pocoo.org/)
- [Bootstrap](https://getbootstrap.com/)
- [MongoDB](https://www.mongodb.com)

## Características
The website uses the Google Maps API for locating the bathrooms that have been provided by the users.

## Code style

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Code example
The following code snippet shows the way the application behaves whenever the user calls for the main view ("GET Request"):
```
if request.method == "GET":
        restrooms = []
        restroom = {}
        cursor = mongo.db.collection.find()
        for record in cursor:
            restrooms.append(record)
        return render_template("index.html", restrooms=restrooms, r=restroom)
```
## Installation
For the use of the application on your own PC we recommend you use a virtual environment, like [virtualenv](https://virtualenv.pypa.io), for a safer installation of the needed libraries.
<br>
In order to deploy the application on a server, the easiest way is to do it through [Heroku](https://www.heroku.com). You can find a short cheatsheet for deploying apps on Heroku [here](https://github.com/AxelJunes/MLaaS/blob/master/heroku_cheatsheet.txt).

## Mode of use
The website has two views:
- The main view has a map that contains markers with all the gender-free bathrooms that are registered in the database. This view has two buttons: "Add a bathroom", which lets the user add a new bathroom to the application (with a form), and "Bathrooms near me", that checks which bathrooms are close to the user and zooms to the users position.
- The "About Divercity" view, which contains all the information about the application.

## Credits
This website has been developed for the subject of "Ethics, Legislation and Profession (ELP)", belonging to the fourth year of the Computer Science and Engineering degree in the Universidad Complutense de Madrid (UCM), in the year 2018.
