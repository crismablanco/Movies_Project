import fresh_tomatoe
import media

toy_story = media.Movie("Toy Story",
                        "The story of a boy and his toys",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "",
                     "http://img.csfd.cz/files/images/user/profile/159/129/159129345_9e5fe4.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

dreams = media.Movie("What dreams may come",
                     "Chris Neilson dies to find himself in a heaven more amazing than he could have ever dreamed of. There is one thing missing: his wife. After he dies, his wife, Annie killed herself and went to hell. Chris decides to risk eternity in hades for the small chance that he will be able to bring her back to heaven",
                     "https://upload.wikimedia.org/wikipedia/en/9/91/Whatdreamsposter.jpeg",
                     "https://www.youtube.com/watch?v=JqKfW4jTn54")

matrix = media.Movie("Matrix",
                     "The Matrix es una película de ciencia ficción escrita y dirigida por Lana y Andy Wachowski y protagonizada por Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss y Hugo Weaving.",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

libertad = media.Movie("Sueños de libertad",
                     "The Shawshank Redemption es una película estadounidense del año 1994, escrita y dirigida por Frank Darabont y protagonizada por Tim Robbins y Morgan Freeman",
                     "http://frasesdelapelicula.com/wp-content/uploads/2010/10/Sueno-de-fuga.jpg",
                     "https://www.youtube.com/watch?v=raRbQkJ2pD4")

jw = media.Movie("Jurasik World",
                     "La película, cuarta parte de la franquicia de Parque Jurásico iniciada en 1993, está producida por Steven Spielberg, Frank Marshall y Patrick Crowley.",
                     "https://merlinsmusings.files.wordpress.com/2015/06/jurassicworldtrex.jpg",
                     "https://www.youtube.com/watch?v=RFinNxS5KN4")


movies = [dreams, avatar, toy_story, matrix, libertad, jw]
fresh_tomatoe.open_movies_page(movies)

#print(media.Movie.__name__)
#print(media.Movie.__module__)
