
"""A simple movie review system with ratings and review IDs."""

import hashlib
import secrets
import os

STREAM_HOST = "127.0.0.1"
STREAM_PORT = 8000
MODERATOR_PASSWORD = os.environ.get("MODERATOR_PASSWORD", "")
movies = {}


def add_movie(title, genre, year):
    """Add a movie to the movie collection."""
    if not title or not genre:
        raise ValueError("Title and genre cannot be empty.")
    if not isinstance(year, int) or isinstance(year, bool) or year < 1888:
        raise ValueError("Enter a valid movie release year.")

    movies[title] = {
        "genre": genre,
        "year": year,
        "ratings": [],
        "reviews": [],
    }


def rate_movie(title, stars, review_text=""):
    """Add a rating and optional review for a movie."""
    if title not in movies:
        raise ValueError("Movie not found.")

    if (
        not isinstance(stars, int)
        or isinstance(stars, bool)
        or not 1 <= stars <= 5
    ):
        print(f"Rating must be between 1 and 5, got {stars}")
        return False

    movies[title]["ratings"].append(stars)

    if review_text:
        movies[title]["reviews"].append(review_text)

    return True


def average_rating(title):
    """Calculate the average rating for a movie."""
    ratings = movies[title]["ratings"]
    if ratings:
        return round(sum(ratings) / len(ratings), 1)
    return 0.0


def top_movies(count=2):
    """Return the highest-rated movies."""
    if (
        not isinstance(count, int)
        or isinstance(count, bool)
        or count < 0
    ):
        raise ValueError("Count must be a non-negative integer.")

    ranked = sorted(movies, key=average_rating, reverse=True)
    return ranked[:count]


def pick_featured():
    """Select a featured movie randomly."""
    if not movies:
        return None

    return secrets.choice(sorted(movies))


def review_id(title, review_text):
    """Generate a SHA-256-based review identifier."""
    review_data = f"{title}:{review_text}".encode("utf-8")
    return hashlib.sha256(review_data).hexdigest()[:10]


def print_all_reviews():
    """Print movie titles and their average ratings."""
    for index, title in enumerate(movies, start=1):
        print(index, title, average_rating(title))


def stream_address():
    """Return the configured streaming address."""
    return f"{STREAM_HOST}:{STREAM_PORT}"


def main():
    """Run the movie-review demonstration."""
    add_movie("The Long Road", "Drama", 2021)
    add_movie("Laugh Track", "Comedy", 2019)
    add_movie("Star Drift", "Sci-Fi", 2023)

    rate_movie("The Long Road", 5, "Beautiful story")
    rate_movie("The Long Road", 4, "A bit slow but worth it")
    rate_movie("Laugh Track", 2, "Not very funny")
    rate_movie("Star Drift", 6, "Out of range rating")
    rate_movie("Star Drift", 4)

    print_all_reviews()
    print("Top movies:", top_movies())
    print("Featured today:", pick_featured())
    print(
        "Review id:",
        review_id("Laugh Track", "Not very funny"),
    )
    print("Streaming from", stream_address())
    print("Genres:", sorted(movie["genre"] for movie in movies.values()))


if __name__ == "__main__":
    main()
