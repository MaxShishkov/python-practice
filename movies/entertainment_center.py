import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story about a boy and his toys that come to live",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A story about a marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=uZNHIU3uHT4")

school_of_rock = media.Movie("School of Rock", "A story about kids becoming Rock Stars",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")


movies = [toy_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
