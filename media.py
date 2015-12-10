import webbrowser

class Movie():
    """ This is a class that represent movies with their:
            - title
            - storyline
            - image poster
            - trailer
            - rating
            - director
            - stars
            - country
            - year

            **** made by crismablanco@gmail.com to Udacity Nanodegree Program

    """
    #constructor definition
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_image,
                 movie_trailer,
                 movie_rating,
                 movie_director,
                 movie_stars,
                 movie_country,
                 movie_year):
        
        self.title                  = movie_title
        self.storyline              = movie_storyline
        self.poster_image_url       = movie_image
        self.trailer_youtube_url    = movie_trailer
        self.rating                 = movie_rating
        self.director               = movie_director
        self.stars                  = movie_stars
        self.country                = movie_country
        self.year                   = movie_year

    # Function show_trailer that open a browser with the youtube URL.
    # This is just for testing purpose
    def show_trailer(self):
        webbrowser.open(self.trailer)
        
