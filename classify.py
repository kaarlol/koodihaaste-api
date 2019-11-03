#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
import scoring

word_score = scoring.Word_scoring("words.txt")
syntax_score = scoring.Letter_scoring(data.letters)

class Message:
    def __init__(self, message):
        self.message = message
        self.shifted_message = []

        shift = 0
        while shift < 29:
            # Define empty string for a return value
            shifted = ""
            # Iterate through characters in message
            for character in self.message:
                # Define characters position in lower case alphabet
                position = data.alphabet.find(character.lower())
                # Check whether character is in alphabet
                if position != -1:
                    # Define shift amount
                    shifted_character = position + shift
                    # Check if character is in upper case and append to return value in upper case string if so
                    if character.isupper():
                        shifted += data.alphabet[shifted_character %
                                                 len(data.alphabet)].upper()
                    # Otherwise just append the character to return value as is
                    else:
                        shifted += data.alphabet[shifted_character %
                                                 len(data.alphabet)]
                # If character is not in defined alphabet just add it as is
                else:
                    shifted += character
            self.shifted_message.append({"message": shifted})
            shift += 1

        for item in self.shifted_message:
            letter_score = syntax_score.letter_score(item["message"])
            item["letter_score"] = letter_score

        self.shifted_message = sorted(
            self.shifted_message, key=lambda k: k["letter_score"], reverse=True)

        self.likely_correct_message = self.shifted_message[0]["message"]
        self.letter_score = self.shifted_message[0]["letter_score"]
        self.last_letter_score = syntax_score.last_letter_score(
            self.likely_correct_message)
        self.last_two_letter_score = syntax_score.last_two_letter_score(
            self.likely_correct_message)
        self.first_two_letter_score = syntax_score.first_two_letter_score(
            self.likely_correct_message)
        self.fonotactics_score = syntax_score.fonotactics_score(
            self.likely_correct_message)
        self.word_score = word_score.frequency_score(self.likely_correct_message)

        rules = [self.last_letter_score == 0,self.last_two_letter_score == 0,self.fonotactics_score == 0,self.first_two_letter_score == 0,self.word_score > 3e-05]

        if all(rules):
            self.is_bullshit = False
        else:
            self.is_bullshit = True
        
    def scores(self):
        all_scores = self.__dict__.keys()
        return all_scores
