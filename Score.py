class Score:
    def __init__(self, initial_score) -> None:
        self.inital_score = initial_score
        self.current_score = self.inital_score


    def update_score(self):
        self.current_score = self.current_score + 1
    

    def return_score(self):
        return self.current_score
