<h1 align="center"><a href="http://dailyleetcode.club/">http://www.DailyLeetcode.club/</a></h1>

Website that redirects to a random leetcode question that rotates each day

# How are the questions picked?

The process of "randomly" selecting question is unnecessarily complex for no reason...

Well, so of...

Similar to the reasons raised in this [Quora post](https://www.quora.com/Is-Spotifys-shuffle-feature-truly-random-I-keep-hearing-the-same-songs-in-my-library-too-often-for-it-to-be-a-mere-coincidence-Does-Spotify-use-some-kind-of-special-algorithm-to-determine-what-song-plays-If-so-why/answer/Mattias-Petter-Johansson) discussing the complexity of Spotify's shuffling algorithm, I've found that entirely random question selection results in a bad user experience.

A user could simply click the "Shuffle" button on Leetcode and visit a random question, but there's a non-zero chance that one of Leetcode's notoriously bad questions will be chosen.  DailyLeetcodes "random" question selection tries to filter out these bad questions.