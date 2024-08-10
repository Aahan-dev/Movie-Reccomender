class MovieRecommendationSystem:
    def __init__(self):
        """Initialize the movie recommendation system with a sample dataset."""
        self.movies = [
            {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"]},
            {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "actors": ["Christian Bale", "Heath Ledger"]},
            {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "actors": ["Tom Hanks", "Robin Wright"]},
            {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "actors": ["Keanu Reeves", "Laurence Fishburne"]},
            {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9, "actors": ["John Travolta", "Uma Thurman"]},
            {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "actors": ["Tim Robbins", "Morgan Freeman"]}
        ]

    def recommend_by_genre(self, genre):
        """
        Recommend movies based on the specified genre.

        Args:
            genre (str): The genre to filter movies by.

        Returns:
            list: A list of recommended movie titles.
        """
        recommended = [movie['title'] for movie in self.movies if movie['genre'].lower() == genre.lower()]
        return recommended

    