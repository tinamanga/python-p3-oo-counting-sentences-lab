import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Triggers the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        parts = re.split(r'[.!?]+', self.value)
        sentences = [s.strip() for s in parts if s.strip()]
        return len(sentences)
