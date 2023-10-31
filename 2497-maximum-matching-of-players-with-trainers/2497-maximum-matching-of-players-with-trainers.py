class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        player_i = 0
        trainer_i = 0
        cnt = 0

        while player_i < len(players) and trainer_i < len(trainers):
            if players[player_i] <= trainers[trainer_i]:
                cnt += 1
                player_i += 1
            trainer_i += 1

        return cnt