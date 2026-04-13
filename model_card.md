# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> SongRecs 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

The system is trying to recommend songs of a similar mood, energy, danceability, based on the preferences stated in the user's profile. It is for people who want to discover new songs that they might like.
---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

The recommender considers genre, mood, energy, danceability, and acousticness -- how non-electronic is the music.
It compares these traits against the preferences stated in the user profile, like favorite genre, target energy level, whether they like acoustic songs, etc.
It scores the songs by awarding points for matches, multiplying by the weights, and adding them all up before ranking them from greatest to least and showing the top k songs.
---

## 4. Data
Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

The dataset is small as it contains 20 songs of a mixture of a variety of genres and moods, from pop to classical as well as reggae, metal, and folk. The moods range from happy to raging, melancholic to romantic and dreamy, along with many other moods. Originally, there were 10 songs, but I had AI generate 10 more songs to expand the dataset.
This data reflects a person who likes music and is open-minded about the different types of music out there. In other words, this suits someone who just wants to vibe along with music.

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

The recommender does work well in that it is not sensitive to changes in weights. The explanations are clear and I can see how much each attribute contributed to the score. It works well in happy cases as the mood and/or energy matches.
---

## 6. Limitations and Bias
Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

The recommender struggled with edge cases, where mood and energy, among other attributes conflict with one another. Therefore, the recommendations in those cases do not make sense. It would not match what people would intuitively look for when making recommendations, given those attributes.
Furthermore, it keeps recommending the same songs in some of the profiles, like "Sunrise City". Therefore, it would be unfair if used in a real product as some songs would get unfairly boosted, while others get ignored, even if the preferences match more closely with the user's.
---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

I checked the functionality of the system by using multiple user profiles and seeing how it behaves in edge cases, or ambiguous situations (e.g. intense, but low energy like Kendrick's diss tracks in 2024. The low energy is likely to favor songs that are more calm and pleasant, rather than intense)

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

If I had more time, I would add in more features. Perhaps I could put in a model that learns the user's preferences through behavior (interaction with the app), and adapt future recommendations and weights accordingly. That way, the recommender is more dynamic.

---

## 9. Personal Reflection
A few sentences about what you learned:

- What surprised you about how your system behaved
I'm surprised that even after changing weights, the songs recommended are mostly similar.

- How did building this change how you think about real music recommenders
Real world recommenders are more complex than I thought, especially when it comes to adapting to user preferences while also navigating through ambiguity as some preferences can be contradicting, or behavior can be different than stated preference.

- Where do you think human judgment still matters, even if the model seems "smart"
Human judgment still matters when looking at ambiguous situations or situations that require intuition and feeling.


## Output
![alt text](image.png)

### Results of Different Profiles
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)
The majority of the music recommendations do not make sense as they do not account for the edge cases. In fact, the "low_energy_hateful" profile was designed with some of Kendrick Lamar's songs in mind, for when someone wants to vibe with the diabolical pettiness and hate that he has for Drake. Instead of recommending songs with a more negative mood or low energy, most of the recommendations had high energy and/or a more positive mood (peaceful/happy).
### After changing weights of energy and genre
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)

For the most part, the system is not very sensitive to these changes as the most of the same songs were recommended in the same order, most of the time.