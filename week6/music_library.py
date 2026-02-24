# Week 6 - Exercise 1
# Music Library Manager

print("=== Welcome to Music Library Manager ===\n")

songs = []
genre_count = {}

# Collect 5 songs
for i in range(1, 6):
    print(f"Enter Song {i}")
    title = input("Song title: ")
    genre = input("Genre: ")
    print()

    songs.append((title, genre))

    # Count genres safely
    genre_count[genre] = genre_count.get(genre, 0) + 1


# Display all songs
print("=== YOUR MUSIC LIBRARY ===")
for index, (title, genre) in enumerate(songs, 1):
    print(f"{index}. {title} ({genre})")

print()

# Display statistics
print("=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} song(s)")

# Find most popular genre
most_popular = max(genre_count, key=genre_count.get)
print(f"\nMost popular genre: {most_popular}")