import fresh_tomatoe
import media

schindler = media.Movie("Schindler's List",
                        "In Poland during World War II, Oskar Schindler gradually becomes concerned"
                        "for his Jewish workforce after witnessing their persecution by the Nazis.",
                        "http://img.csfd.cz/files/images/user/profile/158/883/158883687_7e48f8.jpg",
                        "https://www.youtube.com/watch?v=dwfIf1WMhgc",
                        "8.9",
                        "Steven Spielberg",
                        "Liam Neeson, Ralph Fiennes, Ben Kingsley",
                        "USA",
                        "1993")

intouchables = media.Movie("Intouchables",
                           "After he becomes a quadriplegic from a paragliding accident, an aristocrat"
                           " hires a young man from the projects to be his caregiver.",
                           "http://fo4mw16y1z42edr6j2m4n6vt.wpengine.netdna-cdn.com/wp-content/uploads/Intouchables-poster.jpg",
                           "https://www.youtube.com/watch?v=R8wUIez--WE",
                           "8.6",
                           "Olivier Nakache, Eric Toledano",
                           "Francois Cluzet, Omar Sy, Anne Le Ny",
                           "France",
                           "2011")

dreams = media.Movie("What dreams may come",
                     "After dying in a car crash a man searches the afterlife for his wife.",
                     "https://upload.wikimedia.org/wikipedia/en/9/91/Whatdreamsposter.jpeg",
                     "https://www.youtube.com/watch?v=JqKfW4jTn54",
                     "7",
                     "Vincent Ward",
                     "Robin Williams, Cuba Gooding Jr., Annabella Sciorra",
                     "USA - New Zealand",
                     "1998")

matrix = media.Movie("Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his "
                     "reality and his role in the war against its controllers.",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                     "8.7",
                     "Wachowski Brothers",
                     " Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                     "USA",
                     "1999")

freedom = media.Movie("The Shawshank Redemption",
                       "Two imprisoned men bond over a number of years, finding solace and eventual"
                       " redemption through acts of common decency.",
                       "http://frasesdelapelicula.com/wp-content/uploads/2010/10/Sueno-de-fuga.jpg",
                       "https://www.youtube.com/watch?v=raRbQkJ2pD4",
                       "9.3",
                       "Frank Darabont",
                       "Tim Robbins, Morgan Freeman, Bob Gunton",
                       "USA",
                       "1994")

lion = media.Movie("The Lion King",
                   "Lion cub and future king Simba searches for his identity. His eagerness to "
                   "please others and penchant for testing his boundaries sometimes gets him into trouble.",
                   "http://ecx.images-amazon.com/images/I/51M7QPXDNPL.jpg",
                   "https://www.youtube.com/watch?v=4sj1MT05lAA",
                   "8.5",
                   "Roger Allers, Rob Minkoff",
                   "Matthew Broderick, Jeremy Irons, James Earl Jones",
                   "USA",
                   "1994")


movies = [dreams, schindler, intouchables, matrix, freedom, lion]
fresh_tomatoe.open_movies_page(movies)

#print(media.Movie.__name__)
#print(media.Movie.__module__)
