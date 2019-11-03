#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import data module to get scoring rules and Finnish alphabet
import data
# Import module to score messages based on letters and words
import scoring

# Initialize word and letter scoring classes with word and letter frequency data, and rules
word_score = scoring.Word_scoring("words.txt")
syntax_score = scoring.Letter_scoring(data.letters)

# Define class that stores all the scores for the message
class Message:
    def __init__(self, message):
        self.message = message

        # Create a list of messages with all letters shifted through alphabet
        self.shifted_message = []
        shift = 0
        while shift < 29:
            shifted = ""
            for character in self.message:
                position = data.alphabet.find(character.lower())
                if position != -1:
                    shifted_character = position + shift
                    if character.isupper():
                        shifted += data.alphabet[shifted_character %
                                                 len(data.alphabet)].upper()
                    else:
                        shifted += data.alphabet[shifted_character %
                                                 len(data.alphabet)]
                else:
                    shifted += character
            self.shifted_message.append({"message": shifted})
            shift += 1

        # Calculate score based on letter frequency for each shifted message
        for item in self.shifted_message:
            letter_score = syntax_score.letter_score(item["message"])
            item["letter_score"] = letter_score

        # Sort shifted messages based on letter scores to break the Caesat encryption
        self.shifted_message = sorted(
            self.shifted_message, key=lambda k: k["letter_score"], reverse=True)

        # Set best scored shifted message as most likely to be non-bullshit
        self.likely_correct_message = self.shifted_message[0]["message"]
        
        # Set best scored shifted message's letter score
        self.letter_score = self.shifted_message[0]["letter_score"]

        # Calculate last letter score for most likely message
        self.last_letter_score = syntax_score.last_letter_score(
            self.likely_correct_message)

        # Calculate last two letter score for most likely message
        self.last_two_letter_score = syntax_score.last_two_letter_score(
            self.likely_correct_message)
        
        # Calculate first two letter score for most likely message
        self.first_two_letter_score = syntax_score.first_two_letter_score(
            self.likely_correct_message)

        # Calculate fonotactics score for most likely message
        self.fonotactics_score = syntax_score.fonotactics_score(
            self.likely_correct_message)

        # Calculate word score for most likely message
        self.word_score = word_score.frequency_score(self.likely_correct_message)

        # Define rules that filter bullshit messages from correct ones
        rules = [self.last_letter_score == 0,self.last_two_letter_score == 0,self.fonotactics_score == 0,self.first_two_letter_score == 0,self.word_score > 3e-05]
        if all(rules):
            self.is_bullshit = False
        else:
            self.is_bullshit = True

    # Return all scores from the class    
    def scores(self):
        all_scores = self.__dict__.keys()
        return all_scores
