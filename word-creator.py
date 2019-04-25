"""
Form pronounceable words that will get suffixed
by a typical city suffix to form what could seem
like an actual city name.

Rules:

1) Can start with either a consonant or vowel.
2) I before E except after C.
3) If the word ends in a vowel+y, as in "key" or "volley", add an s to the end.
4) If the word ends in a consonant+y & is meant to be plural, as in
    "rockys" -> "rockies", remove the y and replace with "ies".
5) If the word ends in "s", "ss" , "z", "ch", "sh", "x", add an "es" to the end.
"""
import string

def create_word():
    alphabet_lowercase = string.ascii_lowercase
    vowels = "aeiou"