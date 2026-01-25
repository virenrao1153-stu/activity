import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

init(autoreset=True)

# ---------------- LOAD DATA ----------------
def load_data(file_path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        sys.exit()

movies_df = load_data()

# ---------------- TF-IDF ----------------
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# ---------------- GENRES ----------------
def list_genres(df):
    return sorted(
        set(
            genre.strip()
            for sublist in df['Genre'].dropna().str.split(', ')
            for genre in sublist
        )
    )

genres = list_genres(movies_df)

# ---------------- PROCESSING ANIMATION ----------------
def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# ---------------- RECOMMEND MOVIES ----------------
def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df.copy()

    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]

    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]

    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    recommendations = []

    for _, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue

        polarity = TextBlob(overview).sentiment.polarity

        if mood:
            mood_polarity = TextBlob(mood).sentiment.polarity
            if mood_polarity < 0 and polarity <= 0:
                continue

        recommendations.append((row['Series_Title'], polarity))

        if len(recommendations) == top_n:
            break

    return recommendations if recommendations else "No suitable movie recommendations found."

# ---------------- DISPLAY ----------------
def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\nAI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        print(f"{Fore.CYAN}{idx}. {title} (Polarity: {polarity:.2f}, {sentiment})")

# ---------------- MAIN FLOW ----------------
def handle_ai(name):
    print(Fore.BLUE + "\nLet's find the perfect movie for you!\n")

    print(Fore.GREEN + "Available Genres:")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")

    while True:
        genre_input = input(Fore.YELLOW + "\nEnter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input) - 1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(Fore.RED + "Invalid input. Try again.")

    mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()

    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "positive" if polarity > 0 else "negative"
    print(f"\n{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f})")

    while True:
        rating_input = input(Fore.YELLOW + "\nEnter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range.")
        except ValueError:
            print(Fore.RED + "Invalid input.")

    print(Fore.BLUE + f"\nFinding movies for {name}", end="", flush=True)
    processing_animation()

    while True:
        recs = recommend_movies(genre, mood, rating)
        if isinstance(recs, str):
            print(Fore.RED + recs)
        else:
            display_recommendations(recs, name)

        action = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if action == 'no':
            print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿")
            break

# ---------------- ENTRY POINT ----------------
def main():
    print(Fore.BLUE + "Welcome to your Personal Movie Recommendation Assistant! 🎬🍿\n")
    name = input(Fore.YELLOW + "What's your name? ").strip()
    print(Fore.GREEN + f"\nGreat to meet you, {name}!")
    handle_ai(name)

main()