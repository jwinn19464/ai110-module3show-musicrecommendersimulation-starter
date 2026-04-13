"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    """Run the music recommender simulation with a sample user profile."""
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    starter_profile = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.7,
        "likes_acoustic": False,
    }

    # Adversarial / edge-case user profiles designed to test scoring logic
    adversarial_profiles = [
        {
            "name": "high_energy_sad",
            "profile": {
                "genre": "pop",
                "mood": "sad",
                "energy": 0.9,
                "danceability": 0.2,
                "likes_acoustic": False,
            },
        },
        {
            "name": "acoustic_dance_conflict",
            "profile": {
                "genre": "electronic",
                "mood": "happy",
                "energy": 0.15,
                "danceability": 0.95,
                "likes_acoustic": True,
            },
        },
        {
            "name": "low_energy_hateful",
            "profile": {
                "genre": "rap",
                "mood": "hateful",
                "energy": 0.0,
                "danceability": 0.0,
                "likes_acoustic": False,
            },
        },
    ]

    all_profiles = [
        {"name": "starter", "profile": starter_profile},
        *adversarial_profiles,
    ]

    for variant in all_profiles:
        name = variant["name"]
        user_prefs = variant["profile"]
        print(f"\n=== Recommendations for profile: {name} ===")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"  genre: {song['genre']}, mood: {song['mood']}, energy: {song['energy']:.2f}, danceability: {song['danceability']:.2f}, acousticness: {song['acousticness']:.2f}")
            print(f"  Because: {explanation}")
            print()

        print("User profile:")
        for key, value in user_prefs.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    main()