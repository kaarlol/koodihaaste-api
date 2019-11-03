#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define class to score messages based on indivudual characters
class Letter_scoring(object):
    def __init__(self, rules):
        self.rules = rules
        non_ending_character = []
        for character in rules:
            if character["can_end"] == False:
                non_ending_character.append(character["letter"])
        self.non_ending_character = non_ending_character
        consonant = []
        for character in rules:
            if character["type"] == "consonant":
                consonant.append(character["letter"])
        self.consonant = consonant

    # Count a score based on letter frequency in Finnish language
    def letter_score(self, message):
        letter_score = 0
        for item in self.rules:
            letter_score += message.count(item["letter"]) * item["frequency"]
        return letter_score

    # Check that words' last letters are not invalid for Finnish language
    def last_letter_score(self, message):
        words = message.split()
        last_letter_score = 0
        for word in words:
            if word.endswith(tuple(self.non_ending_character)):
                last_letter_score -= 1
        return last_letter_score

    # Check words' last two letters
    def last_two_letter_score(self, message):
        words = message[:-1].split()
        last_two_letter_score = 0
        for word in words:
            if word.endswith(tuple(self.consonant)) and word[:-1].endswith(tuple(self.consonant)):
                last_two_letter_score -= 1
        return last_two_letter_score

    # Check that first two letters don't break Finnish language rules
    def first_two_letter_score(self, message):
        words = message[:-1].split()
        first_two_letter_score = 0
        for word in words:
            if word.lower().startswith(tuple(self.consonant)) and word[1].startswith(tuple(self.consonant)):
                first_two_letter_score -= 1
        return first_two_letter_score

    # Check for words fonotactics, for example "a" and "ä" can't be in same word
    def fonotactics_score(self, message):
        words = message.split()
        fonotactics_score = 0
        for word in words:
            if len(word) < 8:
                f = False
                b = False
                for item in self.rules:
                    if "fonotactics" in item and item["fonotactics"] == "front":
                        if word.lower().find(item["letter"]) > -1:
                            f = True
                    if "fonotactics" in item and item["fonotactics"] == "back":
                        if word.lower().find(item["letter"]) > -1:
                            b = True
                if f and b:
                    fonotactics_score -= 1
        return fonotactics_score

# Define class to score messages based on words in the
class Word_scoring(object):
    def __init__(self, wordfile, sep=' '):
        self.words = {}
        file = open(wordfile, "r")
        for line in file:
            key, count = line.split(sep)
            self.words[key] = int(count)
        file.close()
        self.N = sum(self.words.values())
        for key in self.words.keys():
            self.words[key] = self.words[key] / self.N
   
    # Score message based on Finnish word frequency
    def frequency_score(self, message):
        score = 0
        words = message[:-1].split()
        for word in words:
            if word.lower() in self.words:
                score += self.words[word.lower()]
        return score
        
