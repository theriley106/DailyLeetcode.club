<h1 align="center"><a href="http://dailyleetcode.club/">http://www.DailyLeetcode.club/</a></h1>

Website that redirects to a random leetcode question that rotates each day

# How are the questions picked?

The process of "randomly" selecting question is unnecessarily complex for no reason...

Well, so of...

Similar to the reasons raised in this [Quora post](https://www.quora.com/Is-Spotifys-shuffle-feature-truly-random-I-keep-hearing-the-same-songs-in-my-library-too-often-for-it-to-be-a-mere-coincidence-Does-Spotify-use-some-kind-of-special-algorithm-to-determine-what-song-plays-If-so-why/answer/Mattias-Petter-Johansson) discussing the complexity of Spotify's shuffling algorithm, I've found that entirely random question selection results in a bad user experience.

A user could simply click the "Shuffle" button on Leetcode and visit a random question, but there's a non-zero chance that one of Leetcode's notoriously bad questions will be chosen.  DailyLeetcodes "random" question selection tries to filter out these bad questions.

The shuffling is done with a program I made a while ago called [EliteCode](https://github.com/theriley106/EliteCode), which strategically shuffles Leetcode questions to optimize DS&A study time.  The questions are shuffles based on "weights" that you can provide, which give priority to certain level questions.

For instance:

```javascript
{'medium': 30, 'hard': 10, 'easy': 60}
```

Will generate random unsolved questions that most likely fall under easy or medium difficulty, with a small chance of the question being categorized as hard.

Meanwhile,

```javascript
{'medium': 50, 'hard': 10, 'easy': 10}
```

Will generate unsolved questions that most likely fall under the medium difficulty, with a small chance of the question being categorized as easy or hard.

```javascript
{'medium': 0, 'hard': 0, 'easy': 50}
```

Will only generate unsolved Leetcode questions that are categorized as easy.

DailyLeetcode.club uses the following weights to generate questions:

```javascript
{'medium': 30, 'hard': 10, 'easy': 60}
```