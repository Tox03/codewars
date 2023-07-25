class User():  # Класс с прокачкой уровня (ранга от -8 до 8)
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, up_rank):
        temporal2 = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        up_rank = temporal2.index(up_rank)
        rank = temporal2.index(self.rank)
        if up_rank < rank and up_rank - rank == -1:
            self.progress += 1
        elif up_rank == rank:
            self.progress += 3
        elif up_rank > rank:
            temporal = up_rank-rank
            self.progress += 10 * temporal * temporal
        while self.progress >= 100 and rank != 15:
            self.progress -= 100
            rank += 1
        if rank == 15:
            self.progress = 0
        self.rank = temporal2[rank]
        print(rank, self.rank)