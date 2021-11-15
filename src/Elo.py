
class ELO:
    def __init__(self):
        self.k = 32
        self.n = 0

   
    def calculate_new_rating(self, player_rating, opponent_rating, result):
        self.n += 1
        expected_score_a = self.calculate_expected_score(
            player_rating, opponent_rating)
        new_rating_a = player_rating + self.k * (result - expected_score_a)
        return new_rating_a

    
    def calculate_expected_score(self, player_rating, opponent_rating,):
        expected_score_a = 1 / \
            (1 + 10 ** ((opponent_rating - player_rating) / 400))
        return expected_score_a

    def calculate_result(self, rating_a, rating_b):
        expected_score_a = self.calculate_expected_score(rating_a, rating_b)
        expected_score_b = self.calculate_expected_score(rating_b, rating_a)
        result = 0.5 * (expected_score_a + expected_score_b)
        # result = 1 if expected_score > 0.5 else 0
        return result

elo = ELO()

res = elo.calculate_result(1000, 1000)

rating = elo.calculate_new_rating(1000, 1000, 1)

print(rating)
