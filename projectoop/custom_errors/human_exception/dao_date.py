class HumanDAODateException(Exception):
    def __init__(self, human):
        self.human = human
