#!/usr/bin/env python3
import ipdb 
import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, new_value):
    if type(new_value) is str:
      self._value = new_value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def is_sentence(self):
    if self.value[-1] == ".":
      return True
    else:
      return False

  def is_question(self):
    if self.value[-1] == "?":
      return True
    else:
      return False

  def is_exclamation(self):
    if self.value[-1] == "!":
      return True
    else: 
      return False

  def count_sentences(self):
    no_questions = self.value.replace("?", ".")
    no_exclamations = no_questions.replace("!", ".")
    sentence_list = no_exclamations.split(".")
    sentence_set = list(set(sentence_list))
    sentence_set.remove("")
    return len(sentence_set)
 