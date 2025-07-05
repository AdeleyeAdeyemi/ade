import random
from flask import session

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]
        # Store sequence in session for stateless HTTP
        session['memory_sequence'] = self.sequence

    def get_sequence_from_session(self):
        return session.get('memory_sequence', [])

    def is_list_equal(self, user_sequence):
        correct_sequence = self.get_sequence_from_session()
        return user_sequence == correct_sequence

    def clear_sequence(self):
        session.pop('memory_sequence', None)

