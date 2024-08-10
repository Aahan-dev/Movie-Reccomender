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

    def recommend_by_rating(self, min_rating):
        """
        Recommend movies that have a rating above the specified minimum rating.


        Args:
            min_rating (float): The minimum rating to filter movies by.


        Returns:
            list: A list of recommended movie titles.
        """
        recommended = [movie['title'] for movie in self.movies if movie['rating'] >= min_rating]
        return recommended


    def recommend_by_actor(self, actor):
        """
        Recommend movies featuring a specific actor.


        Args:
            actor (str): The actor's name to filter movies by.


        Returns:
            list: A list of recommended movie titles.
        """
        recommended = [movie['title'] for movie in self.movies if actor in movie['actors']]
        return recommended


    def run(self):
        """Run the movie recommendation system."""
        print("Welcome to the Movie Recommendation System!")
       
        while True:
            print("\nChoose a recommendation method:")
            print("1. By Genre")
            print("2. By Minimum Rating")
            print("3. By Actor")
            print("4. Exit")




            choice = input("Enter your choice (1-4): ")




            if choice == "1":
                genre = input("Enter the genre (e.g., Sci-Fi, Drama): ")
                recommendations = self.recommend_by_genre(genre)
            elif choice == "2":
                try:
                    min_rating = float(input("Enter the minimum rating (0-10): "))
                    recommendations = self.recommend_by_rating(min_rating)
                except ValueError:
                    print("Invalid rating. Please enter a number.")
                    continue
            elif choice == "3":
                actor = input("Enter the actor's name: ")
                recommendations = self.recommend_by_actor(actor)
            elif choice == "4":
                print("Exiting the movie recommendation system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
                continue








            if recommendations:
                print("Recommended Movies:")
                for title in recommendations:
                    print(f"- {title}")
            else:
                print("No recommendations found.")








if __name__ == "__main__":
    # Create an instance of MovieRecommendationSystem and run it
    movie_recommender = MovieRecommendationSystem()
    movie_recommender.run()
                
                
                
                
                