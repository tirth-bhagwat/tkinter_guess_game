import random
import time
from dbManager import Database

EASY = 10
MEDIUM = 15
HARD = 20


class Game:
    def __init__(self):
        self.__running_002 = False
        self.database_002 = Database()

    def start_002(
        self,
        difficulty,
        answer=None,
    ):
        if self.__running_002:
            return

        if difficulty not in [EASY, MEDIUM, HARD]:
            raise Exception("Invalid game difficulty.")

        self.__running_002 = True
        self.__attempts_remaining_002 = 3
        self.__game_result_002 = None
        self.__start_time_002 = time.time()
        self.__difficulty_002 = difficulty

        if answer is None:
            answer = random.randint(1, difficulty)

        self.__answer_002 = answer

    def stop_002(self):
        self.__running_002 = False

    def guess_002(self, guess_002):
        if not self.__running_002:
            raise Exception("Game is not running.")

        if guess_002 == self.__answer_002:

            self.__score_002 = self.__difficulty_002 * self.__attempts_remaining_002
            self.__time_taken_002 = time.time() - self.__start_time_002

            self.__running_002 = False
            self.__game_result_002 = True
            return 0

        self.__attempts_remaining_002 -= 1

        if self.__attempts_remaining_002 == 0:
            self.__running_002 = False
            self.__game_result_002 = False

        return -1 if guess_002 < self.__answer_002 else 1

    @property
    def difficulty(self):
        diff_dict = {10: "EASY", 15: "MEDIUM", 20: "HARD"}
        return diff_dict.get(self.__difficulty_002)

    @property
    def isRunning_002(self):
        return self.__running_002

    @property
    def gameResult_002(self):
        return self.__game_result_002

    @property
    def attemptsRemaining_002(self):
        return self.__attempts_remaining_002

    @property
    def score_002(self):
        if self.gameResult_002 is None:
            raise Exception("Game is not finished.")

        if self.gameResult_002 == False:
            return False

        return {
            "score": self.__score_002,
            "time": self.__time_taken_002,
        }
