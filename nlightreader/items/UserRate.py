class UserRate:
    def __init__(self, rate_id, user_id, target_id, score, status, chapters):
        self.id = rate_id
        self.user_id = user_id
        self.target_id = target_id
        self.score = score
        self.status = status
        self.chapters = chapters
