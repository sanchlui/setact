"""
============================================
🎵 Music Playlist Analyzer - Student Activity
============================================

Your Task: Complete this Python program to analyze
music playlists using SET operations!

You'll build a command-line tool that helps users:
- Find songs they have in common with friends
- Discover new music from friends' playlists
- Track their listening history
- Generate recommendations

Skills you'll practice:
- Creating and modifying sets
- Set operations (union, intersection, difference)
- Set comparisons (subset, superset, disjoint)
- Practical applications of sets

Look for TODO comments to find where to write code.
The reference section at the bottom shows syntax examples.
"""

# ============================================
# SAMPLE DATA - Don't modify this section
# ============================================
# Pre-loaded playlists for demonstration
SAMPLE_PLAYLISTS = {
    "Alice": {"Bohemian Rhapsody", "Hotel California", "Stairway to Heaven",
              "Sweet Child O Mine", "Smells Like Teen Spirit", "Back in Black"},
    "Bob": {"Hotel California", "Imagine", "Smells Like Teen Spirit",
            "Wonderwall", "Back in Black", "Hey Jude"},
    "Carol": {"Stairway to Heaven", "Sweet Child O Mine", "November Rain",
              "Nothing Else Matters", "Bohemian Rhapsody", "Comfortably Numb"},
    "Dave": {"Imagine", "Hey Jude", "Let It Be", "Yesterday",
             "Come Together", "Here Comes the Sun"}
}

ALL_SONGS = {
    "Bohemian Rhapsody", "Hotel California", "Stairway to Heaven",
    "Sweet Child O Mine", "Smells Like Teen Spirit", "Back in Black",
    "Imagine", "Wonderwall", "Hey Jude", "November Rain",
    "Nothing Else Matters", "Comfortably Numb", "Let It Be",
    "Yesterday", "Come Together", "Here Comes the Sun",
    "Purple Rain", "Billie Jean", "Like a Rolling Stone",
    "What's Going On", "Respect", "Good Vibrations"
}

# ============================================
# GLOBAL VARIABLES - User's data
# ============================================
my_playlist = set()  # User's main playlist
recently_played = set()  # Songs played this session
favorites = set()  # User's favorite songs
friends_playlists = dict(SAMPLE_PLAYLISTS)  # Copy of sample data


# ============================================
# HELPER FUNCTION - Display formatting
# ============================================
def display_songs(songs, title="Songs"):
    """Pretty print a collection of songs."""
    print(f"\n🎵 {title} ({len(songs)} songs):")
    if not songs:
        print("   (empty)")
    else:
        for i, song in enumerate(sorted(songs), 1):
            print(f"   {i}. {song}")


def display_menu():
    """Show the main menu."""
    print("\n" + "=" * 50)
    print("🎵 PLAYLIST ANALYZER - Main Menu")
    print("=" * 50)
    print("1. View my playlist")
    print("2. Add songs to my playlist")
    print("3. Remove songs from my playlist")
    print("4. View a friend's playlist")
    print("5. Find songs in common with a friend")
    print("6. Find songs unique to me vs a friend")
    print("7. Get song recommendations")
    print("8. Combine playlists with a friend")
    print("9. Mark songs as favorites")
    print("10. View listening stats")
    print("11. Check playlist relationships")

    print("0. Exit")
    print("-" * 50)


# ============================================
# TODO #1: View My Playlist
# ============================================
# This function displays the user's current playlist.
# Use the display_songs() helper function.

def view_my_playlist():
    """Display the user's current playlist."""


    # YOUR CODE HERE:
    display_songs(my_playlist, "My Playlist")

    # TODO: Also display the number of songs using len()
    # HINT: print(f"Total: {len(my_playlist)} songs")
    print(f"total: {len(my_playlist)}")



# ============================================
# TODO #2: Add Songs to Playlist
# ============================================
# This function lets users add songs to their playlist.
# Remember: sets automatically handle duplicates!

def add_songs():
    """Add songs to the user's playlist."""
    print("\n📀 Add Songs to Your Playlist")
    print("-" * 30)

    # Show available songs
    available = ALL_SONGS - my_playlist  # Songs not in playlist yet

    if not available:
        print("You already have all available songs!")
        return

    display_songs(available, "Available Songs")

    print("\nEnter song names (one per line, empty line to finish):")

    while True:
        song = input("  Song: ").strip()
        if not song:
            break

        # TODO: Check if the song is in ALL_SONGS (valid song)
        # If valid, add it to my_playlist using .add()
        # If not valid, print an error message
        #
        # HINT: Use 'in' to check membership
        # HINT: Use my_playlist.add(song) to add

        # YOUR CODE HERE:
        if song in ALL_SONGS:
            my_playlist.add(song)
        else:
            print("song does not exist!")


    print(f"\nYour playlist now has {len(my_playlist)} songs.")


# ============================================
# TODO #3: Remove Songs from Playlist
# ============================================
# This function lets users remove songs from their playlist.
# Use discard() for safe removal (no error if song not found).

def remove_songs():
    """Remove songs from the user's playlist."""
    print("\n🗑️ Remove Songs from Your Playlist")
    print("-" * 30)

    if not my_playlist:
        print("Your playlist is empty!")
        return

    display_songs(my_playlist, "Your Current Playlist")

    print("\nEnter songs to remove (one per line, empty line to finish):")

    while True:
        song = input("  Remove: ").strip()
        if not song:
            break

        # TODO: Check if the song is in my_playlist

        # YOUR CODE HERE:
        if song in my_playlist:
            my_playlist.discard(song)
        else:
            print("it's not in this playlist!")


    print(f"\nYour playlist now has {len(my_playlist)} songs.")


# ============================================
# TODO #4: Find Common Songs (INTERSECTION)
# ============================================
# Use set intersection to find songs that appear
# in BOTH your playlist AND a friend's playlist.

def find_common_songs():
    """Find songs in common with a friend."""
    print("\n🤝 Find Songs in Common")
    print("-" * 30)

    if not my_playlist:
        print("Add some songs to your playlist first!")
        return

    # Show available friends
    print("Available friends:", ", ".join(friends_playlists.keys()))
    friend = input("Enter friend's name: ").strip()

    if friend not in friends_playlists:
        print(f"❌ {friend} not found!")
        return

    friend_songs = friends_playlists[friend]

    # TODO: Find the INTERSECTION of my_playlist and friend_songs
    # Store the result in a variable called 'common'
    #
    # HINT: Use the & operator OR .intersection() method
    # EXAMPLE: common = my_playlist & friend_songs

    # YOUR CODE HERE:
    common = set()  # Replace this with the intersection!

    # Display results
    if common:
        display_songs(common, f"Songs You Share with {friend}")

        # YOUR CODE HERE:
        (len(common) / len(my_playlist)) * 100
    else:
        print(f"\n😢 You and {friend} have no songs in common!")
        print("   Maybe check out their playlist for new music?")


# ============================================
# TODO #5: Find Unique Songs (DIFFERENCE)
# ============================================
# Use set difference to find songs that are in your
# playlist but NOT in your friend's playlist.

def find_unique_songs():
    """Find songs unique to you vs a friend."""
    print("\n🎯 Find Unique Songs")
    print("-" * 30)

    if not my_playlist:
        print("Add some songs to your playlist first!")
        return

    print("Available friends:", ", ".join(friends_playlists.keys()))
    friend = input("Enter friend's name: ").strip()

    if friend not in friends_playlists:
        print(f"❌ {friend} not found!")
        return

    friend_songs = friends_playlists[friend]

    # TODO: Find songs in YOUR playlist but NOT in friend's playlist
    # Store in 'only_mine'
    #
    # HINT: Use the - operator OR .difference() method
    # EXAMPLE: only_mine = my_playlist - friend_songs

    # YOUR CODE HERE:
    only_mine.difference(friend_songs)


    # TODO: Find songs in FRIEND's playlist but NOT in yours
    # Store in 'only_theirs'

    # YOUR CODE HERE:
    only_theirs = f"songs only {friend} has"


    # Display results
    display_songs(only_mine, f"Songs Only You Have")
    display_songs(only_theirs, f"Songs Only {friend} Has")


# ============================================
# TODO #6: Get Recommendations (DIFFERENCE)
# ============================================
# Recommend songs from friends that the user doesn't have.

def get_recommendations():
    """Suggest songs from friends' playlists."""
    print("\n💡 Song Recommendations")
    print("-" * 30)

    # TODO: Create a set of ALL songs from ALL friends' playlists
    # Use a loop and union, or set comprehension
    #
    # HINT: Start with all_friend_songs = set()
    # HINT: Loop through friends_playlists.values() and use update()
    # OR: Use set union in a loop

    # YOUR CODE HERE:
    all_friend_songs = set()
    friends_playlists.values()
    all_friend_songs.update()


    # TODO: Find songs your friends have that YOU don't have
    # These are your recommendations!
    #
    # HINT: Use difference: all_friend_songs - my_playlist

    # YOUR CODE HERE:
    difference: all_friend_songs - my_playlist

    if recommendations:
        display_songs(recommendations, "Recommended for You")
        print("\n   These songs are popular with your friends!")
    else:
        print("\n🎉 You already have all the songs your friends have!")


# ============================================
# TODO #7: Combine Playlists (UNION)
# ============================================
# Create a merged playlist with songs from both users.

def combine_playlists():
    """Combine your playlist with a friend's."""
    print("\n🔀 Combine Playlists")
    print("-" * 30)

    if not my_playlist:
        print("Add some songs to your playlist first!")
        return

    print("Available friends:", ", ".join(friends_playlists.keys()))
    friend = input("Enter friend's name: ").strip()

    if friend not in friends_playlists:
        print(f"❌ {friend} not found!")
        return

    friend_songs = friends_playlists[friend]

    # TODO: Create a UNION of both playlists
    # Store in 'combined'
    #
    # HINT: Use the | operator OR .union() method
    # EXAMPLE: combined = my_playlist | friend_songs

    # YOUR CODE HERE:
    combined.union(friend_songs)

    # Display stats
    print(f"\n📊 Playlist Stats:")
    print(f"   Your songs: {len(my_playlist)}")
    print(f"   {friend}'s songs: {len(friend_songs)}")
    print(f"   Combined (no duplicates): {len(combined)}")
    print(f"   Duplicates removed: {len(my_playlist) + len(friend_songs) - len(combined)}")

    display_songs(combined, f"Combined Playlist with {friend}")


# ============================================
# TODO #8: Mark Favorites
# ============================================
# Let users mark certain songs as favorites.
# Favorites must be songs in their playlist.

def mark_favorites():
    """Mark songs as favorites."""
    global favorites

    print("\n⭐ Mark Favorites")
    print("-" * 30)

    if not my_playlist:
        print("Add some songs to your playlist first!")
        return

    display_songs(my_playlist, "Your Playlist")
    display_songs(favorites, "Current Favorites")

    print("\nEnter songs to add to favorites (empty line to finish):")

    while True:
        song = input("  Favorite: ").strip()
        if not song:
            break

        # TODO: Check if the song is in my_playlist
        # If yes, add it to favorites set
        # If no, tell the user the song must be in their playlist
        #
        # HINT: First check 'if song in my_playlist'
        # HINT: Then use favorites.add(song)

        # YOUR CODE HERE:
        if song in my_playlist:
            favorites.add(song)
        else:
            print("song must be in their playlist!")

    display_songs(favorites, "Your Favorites")


# ============================================
# TODO #9: View Listening Stats
# ============================================
# Display various statistics about the user's music.

def view_stats():
    """Display listening statistics."""
    print("\n📊 Your Listening Stats")
    print("-" * 30)

    # Basic stats
    print(f"📀 Total songs in playlist: {len(my_playlist)}")
    print(f"⭐ Favorite songs: {len(favorites)}")

    # TODO: Check if favorites is a subset of my_playlist
    # It should be! (Can't have favorites that aren't in playlist)
    #
    # HINT: Use .issubset() or <= operator
    # EXAMPLE: favorites <= my_playlist

    # YOUR CODE HERE:
    favorites.issubset(my_playlist)

    # TODO: Calculate percentage of playlist that are favorites
    # Handle the case where playlist is empty!

    # YOUR CODE HERE:
    percent = len(favorites) / len(my_playlist)
    print(f"Percent of favorites: {percent}%")

    # Compare with friends
    print(f"\n👥 Compared to Friends:")
    for friend, songs in friends_playlists.items():
        # TODO: Calculate how many songs you share with each friend
        # Use intersection

        # YOUR CODE HERE:
        common = len(friend) / len(songs)
        print(f"   {friend}: {len(common)} songs in common")


# ============================================
# TODO #10: Check Playlist Relationships
# ============================================
# Check subset/superset relationships between playlists.

def check_relationships():
    """Check playlist subset/superset relationships."""
    print("\n🔍 Playlist Relationships")
    print("-" * 30)

    if not my_playlist:
        print("Add some songs to your playlist first!")
        return

    print("Available friends:", ", ".join(friends_playlists.keys()))
    friend = input("Enter friend's name: ").strip()

    if friend not in friends_playlists:
        print(f"❌ {friend} not found!")
        return

    friend_songs = friends_playlists[friend]

    print(f"\n📊 Comparing with {friend}:")
    print(f"   Your songs: {len(my_playlist)}")
    print(f"   {friend}'s songs: {len(friend_songs)}")

    # TODO: Check various relationships
    # 1. Is my_playlist a subset of friend_songs?
    # 2. Is my_playlist a superset of friend_songs?
    # 3. Are they disjoint (no common songs)?
    # 4. Are they equal?
    #
    # HINT: Use .issubset(), .issuperset(), .isdisjoint()
    # HINT: Use == for equality
    # HINT: Use < for proper subset, > for proper superset

    # YOUR CODE HERE:
    my_playlist.issubset(friend_songs)
    my_playlist.issuperset(friend_songs)
    my_playlist.isdisjoint(friend_songs)




# ============================================
# View Friend's Playlist - Done for you
# ============================================
def view_friend_playlist():
    """View a friend's playlist."""
    print("\n👥 View Friend's Playlist")
    print("-" * 30)
    print("Available friends:", ", ".join(friends_playlists.keys()))

    friend = input("Enter friend's name: ").strip()

    if friend in friends_playlists:
        display_songs(friends_playlists[friend], f"{friend}'s Playlist")
    else:
        print(f"❌ {friend} not found!")


# ============================================
# MAIN PROGRAM LOOP
# ============================================
def main():
    """Main program loop."""
    print("\n" + "🎵" * 25)
    print("   Welcome to the PLAYLIST ANALYZER!")
    print("🎵" * 25)
    print("\nAnalyze your music collection using the power of SETS!")

    # Pre-load some songs for easier testing
    global my_playlist
    my_playlist = {"Hotel California", "Bohemian Rhapsody", "Imagine", "Stairway to Heaven"}
    print(f"\n🎁 Started you off with {len(my_playlist)} songs!")

    while True:
        display_menu()

        try:
            choice = input("Enter choice (0-11): ").strip()

            if choice == "0":
                print("\n👋 Thanks for using Playlist Analyzer!")
                print("   Keep discovering great music! 🎵")
                break
            elif choice == "1":
                view_my_playlist()
            elif choice == "2":
                add_songs()
            elif choice == "3":
                remove_songs()
            elif choice == "4":
                view_friend_playlist()
            elif choice == "5":
                find_common_songs()
            elif choice == "6":
                find_unique_songs()
            elif choice == "7":
                get_recommendations()
            elif choice == "8":
                combine_playlists()
            elif choice == "9":
                mark_favorites()
            elif choice == "10":
                view_stats()
            elif choice == "11":
                check_relationships()
            else:
                print("❌ Invalid choice. Please enter 0-11.")

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

        input("\n[Press Enter to continue...]")


# ============================================
# REFERENCE - Syntax Examples from Today's Notes
# ============================================
"""
# Creating sets:
my_set = {'a', 'b', 'c'}
my_set = set([1, 2, 3])
empty_set = set()

# Adding elements:
my_set.add('element')        # Add single element
my_set.update([1, 2, 3])     # Add multiple elements

# Removing elements:
my_set.remove('x')           # Raises KeyError if not found
my_set.discard('x')          # No error if not found
my_set.pop()                 # Remove arbitrary element
my_set.clear()               # Remove all elements

# Set operations:
A | B                        # Union (all elements)
A.union(B)                   # Same as above

A & B                        # Intersection (common elements)
A.intersection(B)            # Same as above

A - B                        # Difference (in A, not in B)
A.difference(B)              # Same as above

A ^ B                        # Symmetric difference (in A or B, not both)
A.symmetric_difference(B)    # Same as above

# Comparisons:
A <= B                       # A is subset of B
A.issubset(B)                # Same as above

A >= B                       # A is superset of B
A.issuperset(B)              # Same as above

A < B                        # A is proper subset (smaller)
A > B                        # A is proper superset (larger)

A.isdisjoint(B)              # True if no common elements

# Membership testing (O(1) - fast!):
if 'x' in my_set:
    print('Found!')

# Iterating:
for item in my_set:
    print(item)

# Length:
len(my_set)

# Conversion:
list(my_set)                 # Set to list
set(my_list)                 # List to set (removes duplicates)
"""

# ============================================
# 🧪 TEST YOUR CODE!
# ============================================
# Change "RUN_TESTS = False" to "RUN_TESTS = True" below,
# then run this file to test your understanding.
#
# Compare your output to the EXPECTED OUTPUT in comments.
# If they match, you understand set operations! ✅

RUN_TESTS = False  # <-- Change to True to run tests!

if RUN_TESTS:

    print("\n" + "=" * 60)
    print("🧪 TESTING YOUR SET OPERATIONS")
    print("=" * 60)
    print("Compare your output to the EXPECTED OUTPUT in comments!\n")

    # ----------------------------------------
    # TEST 1: Creating Sets & Removing Duplicates
    # (Tests your understanding for TODO #2, #3)
    # ----------------------------------------
    print("-" * 60)
    print("TEST 1: Creating Sets & Removing Duplicates")
    print("-" * 60)

    numbers_list = [1, 2, 3, 2, 1, 4, 3, 5, 4]
    numbers_set = set(numbers_list)

    print(f"Original list: {numbers_list}")
    print(f"Converted to set: {numbers_set}")
    print(f"Length of set: {len(numbers_set)}")

    # EXPECTED OUTPUT:
    # Original list: [1, 2, 3, 2, 1, 4, 3, 5, 4]
    # Converted to set: {1, 2, 3, 4, 5}
    # Length of set: 5

    # ----------------------------------------
    # TEST 2: Adding Elements with add()
    # (Tests TODO #2: add_songs)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 2: Adding Elements with add()")
    print("-" * 60)

    test_playlist = {"Song A", "Song B"}
    print(f"Starting playlist: {sorted(test_playlist)}")

    test_playlist.add("Song C")
    print(f"After add('Song C'): {sorted(test_playlist)}")

    test_playlist.add("Song A")  # Adding duplicate
    print(f"After add('Song A') again: {sorted(test_playlist)}")
    print(f"Length: {len(test_playlist)}")

    # EXPECTED OUTPUT:
    # Starting playlist: ['Song A', 'Song B']
    # After add('Song C'): ['Song A', 'Song B', 'Song C']
    # After add('Song A') again: ['Song A', 'Song B', 'Song C']
    # Length: 3

    # ----------------------------------------
    # TEST 3: Removing Elements with discard()
    # (Tests TODO #3: remove_songs)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 3: Removing Elements with discard()")
    print("-" * 60)

    colors = {"red", "blue", "green", "yellow"}
    print(f"Starting set: {sorted(colors)}")

    colors.discard("green")
    print(f"After discard('green'): {sorted(colors)}")

    colors.discard("purple")  # Doesn't exist - no error!
    print(f"After discard('purple'): {sorted(colors)}")
    print(f"Length: {len(colors)}")

    # EXPECTED OUTPUT:
    # Starting set: ['blue', 'green', 'red', 'yellow']
    # After discard('green'): ['blue', 'red', 'yellow']
    # After discard('purple'): ['blue', 'red', 'yellow']
    # Length: 3

    # ----------------------------------------
    # TEST 4: Intersection (&) - Common Elements
    # (Tests TODO #4: find_common_songs)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 4: Intersection (&) - Common Elements")
    print("-" * 60)

    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    common = A & B
    print(f"A = {sorted(A)}")
    print(f"B = {sorted(B)}")
    print(f"A & B = {sorted(common)}")
    print(f"Length of intersection: {len(common)}")

    # EXPECTED OUTPUT:
    # A = [1, 2, 3, 4, 5]
    # B = [4, 5, 6, 7, 8]
    # A & B = [4, 5]
    # Length of intersection: 2

    # ----------------------------------------
    # TEST 5: Intersection with Playlist Data
    # (Tests TODO #4: find_common_songs with real data)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 5: Intersection with Playlist Data")
    print("-" * 60)

    test_my_playlist = {"Hotel California", "Bohemian Rhapsody", "Imagine", "Stairway to Heaven"}
    alice_songs = friends_playlists["Alice"]

    common_with_alice = test_my_playlist & alice_songs
    print(f"My playlist: {sorted(test_my_playlist)}")
    print(f"Songs in common with Alice: {sorted(common_with_alice)}")
    print(f"Number in common: {len(common_with_alice)}")

    percentage = (len(common_with_alice) / len(test_my_playlist)) * 100
    print(f"Percentage shared: {percentage}%")

    # EXPECTED OUTPUT:
    # My playlist: ['Bohemian Rhapsody', 'Hotel California', 'Imagine', 'Stairway to Heaven']
    # Songs in common with Alice: ['Bohemian Rhapsody', 'Hotel California', 'Stairway to Heaven']
    # Number in common: 3
    # Percentage shared: 75.0%

    # ----------------------------------------
    # TEST 6: Difference (-) - Unique Elements
    # (Tests TODO #5: find_unique_songs)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 6: Difference (-) - Unique Elements")
    print("-" * 60)

    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    only_in_A = A - B
    only_in_B = B - A

    print(f"A = {sorted(A)}")
    print(f"B = {sorted(B)}")
    print(f"A - B (only in A): {sorted(only_in_A)}")
    print(f"B - A (only in B): {sorted(only_in_B)}")

    # EXPECTED OUTPUT:
    # A = [1, 2, 3, 4, 5]
    # B = [4, 5, 6, 7, 8]
    # A - B (only in A): [1, 2, 3]
    # B - A (only in B): [6, 7, 8]

    # ----------------------------------------
    # TEST 7: Difference with Playlist Data
    # (Tests TODO #5: find_unique_songs with real data)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 7: Difference with Playlist Data")
    print("-" * 60)

    test_my_playlist = {"Hotel California", "Bohemian Rhapsody", "Imagine", "Stairway to Heaven"}
    alice_songs = friends_playlists["Alice"]

    only_mine = test_my_playlist - alice_songs
    only_alice = alice_songs - test_my_playlist

    print(f"Songs only I have: {sorted(only_mine)}")
    print(f"Songs only Alice has: {sorted(only_alice)}")

    # EXPECTED OUTPUT:
    # Songs only I have: ['Imagine']
    # Songs only Alice has: ['Back in Black', 'Smells Like Teen Spirit', 'Sweet Child O Mine']

    # ----------------------------------------
    # TEST 8: Union (|) - All Elements Combined
    # (Tests TODO #7: combine_playlists)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 8: Union (|) - All Elements Combined")
    print("-" * 60)

    A = {1, 2, 3}
    B = {3, 4, 5}

    combined = A | B
    print(f"A = {sorted(A)}")
    print(f"B = {sorted(B)}")
    print(f"A | B = {sorted(combined)}")
    print(f"Length of A: {len(A)}")
    print(f"Length of B: {len(B)}")
    print(f"Length of union: {len(combined)}")
    print(f"Duplicates removed: {len(A) + len(B) - len(combined)}")

    # EXPECTED OUTPUT:
    # A = [1, 2, 3]
    # B = [3, 4, 5]
    # A | B = [1, 2, 3, 4, 5]
    # Length of A: 3
    # Length of B: 3
    # Length of union: 5
    # Duplicates removed: 1

    # ----------------------------------------
    # TEST 9: Union with update()
    # (Tests TODO #6: get_recommendations)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 9: Union with update() - Collecting All Friend Songs")
    print("-" * 60)

    all_friend_songs = set()
    for friend_name, songs in friends_playlists.items():
        all_friend_songs.update(songs)
        print(f"After adding {friend_name}'s songs: {len(all_friend_songs)} total")

    print(f"\nTotal unique songs from all friends: {len(all_friend_songs)}")

    # EXPECTED OUTPUT:
    # After adding Alice's songs: 6 total
    # After adding Bob's songs: 9 total
    # After adding Carol's songs: 12 total
    # After adding Dave's songs: 16 total
    #
    # Total unique songs from all friends: 16

    # ----------------------------------------
    # TEST 10: Recommendations (Union + Difference)
    # (Tests TODO #6: get_recommendations)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 10: Recommendations (Union + Difference)")
    print("-" * 60)

    test_my_playlist = {"Imagine", "Hey Jude"}

    all_friend_songs = set()
    for songs in friends_playlists.values():
        all_friend_songs.update(songs)

    recommendations = all_friend_songs - test_my_playlist

    print(f"My playlist: {sorted(test_my_playlist)}")
    print(f"Number of recommendations: {len(recommendations)}")
    print(f"'Imagine' in recommendations: {'Imagine' in recommendations}")
    print(f"'Bohemian Rhapsody' in recommendations: {'Bohemian Rhapsody' in recommendations}")

    # EXPECTED OUTPUT:
    # My playlist: ['Hey Jude', 'Imagine']
    # Number of recommendations: 14
    # 'Imagine' in recommendations: False
    # 'Bohemian Rhapsody' in recommendations: True

    # ----------------------------------------
    # TEST 11: Subset (<=) and Superset (>=)
    # (Tests TODO #9, #10: view_stats, check_relationships)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 11: Subset (<=) and Superset (>=)")
    print("-" * 60)

    small = {1, 2}
    big = {1, 2, 3, 4, 5}
    same = {2, 1}

    print(f"small = {sorted(small)}")
    print(f"big = {sorted(big)}")
    print(f"same = {sorted(same)}")
    print()
    print(f"small <= big (subset): {small <= big}")
    print(f"small < big (proper subset): {small < big}")
    print(f"big >= small (superset): {big >= small}")
    print(f"big > small (proper superset): {big > small}")
    print(f"small <= same (subset): {small <= same}")
    print(f"small < same (proper subset): {small < same}")
    print(f"small == same (equal): {small == same}")

    # EXPECTED OUTPUT:
    # small = [1, 2]
    # big = [1, 2, 3, 4, 5]
    # same = [1, 2]
    #
    # small <= big (subset): True
    # small < big (proper subset): True
    # big >= small (superset): True
    # big > small (proper superset): True
    # small <= same (subset): True
    # small < same (proper subset): False
    # small == same (equal): True

    # ----------------------------------------
    # TEST 12: issubset() and issuperset()
    # (Tests TODO #9: view_stats)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 12: issubset() and issuperset()")
    print("-" * 60)

    test_favorites = {"Song A", "Song B"}
    test_my_playlist = {"Song A", "Song B", "Song C", "Song D"}

    print(f"favorites = {sorted(test_favorites)}")
    print(f"my_playlist = {sorted(test_my_playlist)}")
    print()
    print(f"favorites.issubset(my_playlist): {test_favorites.issubset(test_my_playlist)}")
    print(f"my_playlist.issuperset(favorites): {test_my_playlist.issuperset(test_favorites)}")

    fav_percent = (len(test_favorites) / len(test_my_playlist)) * 100
    print(f"Percentage of playlist that are favorites: {fav_percent}%")

    # EXPECTED OUTPUT:
    # favorites = ['Song A', 'Song B']
    # my_playlist = ['Song A', 'Song B', 'Song C', 'Song D']
    #
    # favorites.issubset(my_playlist): True
    # my_playlist.issuperset(favorites): True
    # Percentage of playlist that are favorites: 50.0%

    # ----------------------------------------
    # TEST 13: isdisjoint() - No Overlap
    # (Tests TODO #10: check_relationships)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 13: isdisjoint() - No Overlap")
    print("-" * 60)

    rock = {"AC/DC", "Led Zeppelin", "Queen"}
    pop = {"Taylor Swift", "Beyonce", "Adele"}
    classic_rock = {"Queen", "Pink Floyd", "The Beatles"}

    print(f"rock.isdisjoint(pop): {rock.isdisjoint(pop)}")
    print(f"rock.isdisjoint(classic_rock): {rock.isdisjoint(classic_rock)}")

    # EXPECTED OUTPUT:
    # rock.isdisjoint(pop): True
    # rock.isdisjoint(classic_rock): False

    # ----------------------------------------
    # TEST 14: Symmetric Difference (^)
    # (Bonus - good to know!)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 14: Symmetric Difference (^)")
    print("-" * 60)

    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    sym_diff = A ^ B
    print(f"A = {sorted(A)}")
    print(f"B = {sorted(B)}")
    print(f"A ^ B (in one but not both): {sorted(sym_diff)}")

    # EXPECTED OUTPUT:
    # A = [1, 2, 3, 4]
    # B = [3, 4, 5, 6]
    # A ^ B (in one but not both): [1, 2, 5, 6]

    # ----------------------------------------
    # TEST 15: Membership Testing (in)
    # (Tests TODO #2, #8: add_songs, mark_favorites)
    # ----------------------------------------
    print("\n" + "-" * 60)
    print("TEST 15: Membership Testing (in)")
    print("-" * 60)

    valid_songs = {"Bohemian Rhapsody", "Hotel California", "Imagine"}

    test_songs = ["Bohemian Rhapsody", "Unknown Song", "Imagine", "Random"]

    for song in test_songs:
        result = song in valid_songs
        print(f"'{song}' in valid_songs: {result}")

    # EXPECTED OUTPUT:
    # 'Bohemian Rhapsody' in valid_songs: True
    # 'Unknown Song' in valid_songs: False
    # 'Imagine' in valid_songs: True
    # 'Random' in valid_songs: False

    # ----------------------------------------
    # SUMMARY
    # ----------------------------------------
    print("\n" + "=" * 60)
    print("🎉 TESTS COMPLETE!")
    print("=" * 60)
    print("""
✅ If your outputs match the EXPECTED OUTPUT comments,
   you understand set operations!

📝 Operations tested:
   • set() - Create from list, removes duplicates
   • add() - Add single element  
   • discard() - Remove safely (no error if missing)
   • & - Intersection (common elements)
   • - - Difference (unique to one set)
   • | - Union (all elements combined)
   • update() - Add multiple elements from iterable
   • <= / issubset() - Check if subset
   • >= / issuperset() - Check if superset
   • isdisjoint() - Check for no overlap
   • ^ - Symmetric difference
   • in - Fast membership testing

🚀 Now complete the TODOs in the activity above!
""")

# ============================================
# RUN THE PROGRAM
# ============================================
# If not running tests, start the main activity
if __name__ == "__main__" and not RUN_TESTS:
    main()
