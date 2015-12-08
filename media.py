import webbrowser

class Movie():
    """ This is a class to help create differents movies."""

    VALID_RATINGS=["ATP","+13","+18","+21"]
    
    def __init__(self, movie_title, movie_storyline, movie_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
        
