import random

movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "mood": "Thriller"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "mood": "Intense"},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "mood": "Emotional"},
    {"title": "3 Idiots", "genre": "Comedy", "rating": 8.4, "mood": "Motivational"},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4, "mood": "Exciting"},
    {"title": "Titanic", "genre": "Romance", "rating": 7.9, "mood": "Emotional"},
    {"title": "Joker", "genre": "Drama", "rating": 8.4, "mood": "Dark"},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7, "mood": "Funny"}
]

def show_movie(movie):
    print("\nRecommended Movie")
    print("Title:", movie["title"])
    print("Genre:", movie["genre"])
    print("IMDB Rating:", movie["rating"])
    print("Mood:", movie["mood"])
    print("-" * 30)

def ai_recommend():
    genre = input("Enter preferred genre: ").title()
    mood = input("Enter your mood: ").title()
    filtered = [m for m in movies if m["genre"] == genre or m["mood"] == mood]
    if filtered:
        movie = max(filtered, key=lambda x: x["rating"])
    else:
        movie = random.choice(movies)
    show_movie(movie)

def random_recommend():
    movie = random.choice(movies)
    show_movie(movie)

def main():
    print("Movie Recommendation System")
    print("1. AI Recommendation")
    print("2. Random Recommendation")
    choice = input("Choose option (1/2): ")
    if choice == "1":
        ai_recommend()
    elif choice == "2":
        random_recommend()
    else:
        print("Invalid choice")

main()