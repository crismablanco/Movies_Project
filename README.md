# Movies_Project
It shows some favorites movies. with python

## Introduction
This is a project made for Udacity Nanodegree Program of Full Stack Web Developer. 
You can see it [here](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
It generates an HTML file to see some of my favorites movies and its descriptions
It is the final project of the [Programming Foundations with Python course](https://www.udacity.com/course/viewer#!/c-ud036-nd)


## Requierments
The code has been created using Python 2.7
Just run the `entertaiment_center.py` and you will see my favorites movies.
If you edit the file you will be able to create your own movies.

## Iside the code
In this project I created a `media.py` that stores the code of a class movie with this parameters:

- title
- storyline
- image poster
- trailer
- rating
- director
- stars
- country
- year

There is another file `entertaiment_center.py` 
Here is stored all the movies information. Each movie is an object (instance) of the Movie Class (in media.py)

### Example of an instance:
`schindler = media.Movie("Schindler's List",
                        "In Poland during World War II, Oskar Schindler gradually becomes concerned"
                        "for his Jewish workforce after witnessing their persecution by the Nazis.",
                        "http://img.csfd.cz/files/images/user/profile/158/883/158883687_7e48f8.jpg",
                        "https://www.youtube.com/watch?v=dwfIf1WMhgc",
                        "8.9",
                        "Steven Spielberg",
                        "Liam Neeson, Ralph Fiennes, Ben Kingsley",
                        "USA",
                        "1993")
`
In the end of this file `entertaiment_center.py` is a call to a fresh_potatoe function 
to generate the HTML file and open it on the web browser.


## Contact
For contact send an email to crismablanco@gmail.com

Best Regards
Cristian Blanco
