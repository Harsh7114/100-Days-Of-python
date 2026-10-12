
from bs4 import BeautifulSoup
import re

# 1. Read the downloaded HTML file
with open("movies.html", "r", encoding="utf-8") as file:
    content = file.read()

# 2. Parse the HTML using BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# 3. Find all movie headings
headings = soup.select("main span[data-test='content'] h2 strong")

movies = []

# 4. Extract movie names
for heading in headings:
    text = heading.get_text(strip=True)

    # Match headings like: 100) Avatar (2009)
    match = re.match(
        r"^\d{1,3}\s*[)—-]\s*(.*?)\s*\(\d{4}\)$",
        text
    )

    if match:
        movie_name = match.group(1).strip()
        movies.append(movie_name)

# 5. Display the extracted movies
for index, movie in enumerate(movies, start=1):
    print(f"{index}. {movie}")

print(f"\nTotal movies extracted: {len(movies)}")

# 6. Save the movie names to a text file
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie + "\n")

print("Movie names saved successfully to movies.txt!")

movies.reverse()
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie + "\n")
