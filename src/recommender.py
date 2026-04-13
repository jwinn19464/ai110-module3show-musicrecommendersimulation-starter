from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_danceability: Optional[float] = None


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the Recommender with a list of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs for the given user profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        if user.target_danceability is not None:
            user_prefs["danceability"] = user.target_danceability

        scored_songs = []
        for song in self.songs:
            score, _ = score_song(user_prefs, song.__dict__)
            scored_songs.append((score, song))

        scored_songs.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate an explanation for why a song is recommended."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        if user.target_danceability is not None:
            user_prefs["danceability"] = user.target_danceability

        score, reasons = score_song(user_prefs, song.__dict__)
        if not reasons:
            return f"No strong attribute matches found. Score: {score:.2f}."
        return f"Score: {score:.2f}. " + "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return a list of dictionaries."""
    songs: List[Dict] = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    print(f"Loading songs from {csv_path}...")
    print(f"Loaded {len(songs)} songs.")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return score and matching reasons."""
    weights = {
        "genre": 0.25 / 2,
        "mood": 0.20,
        "energy": 0.20 * 2,
        "danceability": 0.15,
        "acousticness": 0.20,
    }

    score = 0.0
    reasons: List[str] = []

    if "genre" in user_prefs and user_prefs["genre"]:
        if song.get("genre", "").strip().lower() == str(user_prefs["genre"]).strip().lower():
            score += weights["genre"] * 3
            reasons.append(f"genre match (+{weights['genre'] * 3:.2f})")

    if "mood" in user_prefs and user_prefs["mood"]:
        if song.get("mood", "").strip().lower() == str(user_prefs["mood"]).strip().lower():
            score += weights["mood"] * 1.5
            reasons.append(f"mood match (+{weights['mood'] * 1.5:.2f})")

    if "energy" in user_prefs and isinstance(user_prefs["energy"], (int, float)):
        energy_diff = abs(song.get("energy", 0.0) - float(user_prefs["energy"]))
        if energy_diff <= 0.20:
            score += weights["energy"] * 2
            reasons.append(f"energy close (+{weights['energy'] * 2:.2f})")

    if "danceability" in user_prefs and isinstance(user_prefs["danceability"], (int, float)):
        dance_diff = abs(song.get("danceability", 0.0) - float(user_prefs["danceability"]))
        if dance_diff <= 0.20:
            score += weights["danceability"]
            reasons.append(f"danceability close (+{weights['danceability']:.2f})")

    if "likes_acoustic" in user_prefs:
        likes_acoustic = bool(user_prefs["likes_acoustic"])
        acousticness = float(song.get("acousticness", 0.0))
        if likes_acoustic and acousticness >= 0.50:
            score += weights["acousticness"]
            reasons.append(f"acousticness match (+{weights['acousticness']:.2f})")
        elif not likes_acoustic and acousticness <= 0.50:
            score += weights["acousticness"]
            reasons.append(f"acousticness match (+{weights['acousticness']:.2f})")

    return score, reasons


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    return []

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k recommended songs for a user based on their preferences."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else f"No preferred attribute matches. Score: {score:.2f}."
        scored.append((song, score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
