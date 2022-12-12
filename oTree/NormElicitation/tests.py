from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Introduction
        yield pages.Instructions
        yield pages.Quiz, {
                        # 'q1': 'No',
                        'q2': Constants.NOT_INSPECT_HIGH_payoff,
                        'q3': Constants.HIGH_NOT_INSPECT_payoff,
                        'q4': Constants.INSPECT_LOW_payoff,
                        'q5': Constants.LOW_INSPECT_payoff
                        }
        yield pages.QuizAnswers,
        yield pages.NormIntro,
        yield pages.NormIntroEx1,
        yield pages.NormIntroEx2,
        yield pages.NormIntroEx3,
        yield pages.NormIntroQuiz, {'NormQ1': 6,
                                    'NormQ2': -0.4,
                                    'NormQ3': 1.2
                                    }
        yield pages.NormIntroQuizAnswers,

        if self.player.WorkerPage_first == 1:
            if random.uniform(0, 1) < 0.5:
                yield pages.NormRatingWorker, {'NormRateLI': 1,
                                               'NormRateHI': 2,
                                               'NormRateLN': 3,
                                               'NormRateHN': 4,
                                               'MajorRateLI': 1,
                                               'MajorRateHI': 1,
                                               'MajorRateLN': 1,
                                               'MajorRateHN': 1
                                               }

                yield pages.NormRatingEmployer, {'NormRateIL': 1,
                                                 'NormRateNL': 2,
                                                 'NormRateIH': 3,
                                                 'NormRateNH': 4,
                                                 'MajorRateIL': 1,
                                                 'MajorRateNL': 1,
                                                 'MajorRateIH': 1,
                                                 'MajorRateNH': 1
                                                 }
            else:
                yield pages.NormRatingWorker, {'NormRateLI': 6,
                                               'NormRateHI': 3,
                                               'NormRateLN': 2,
                                               'NormRateHN': 1,
                                               'MajorRateLI': 1,
                                               'MajorRateHI': 1,
                                               'MajorRateLN': 1,
                                               'MajorRateHN': 1
                                               }

                yield pages.NormRatingEmployer, {'NormRateIL': 1,
                                                 'NormRateNL': 2,
                                                 'NormRateIH': 3,
                                                 'NormRateNH': 4,
                                                 'MajorRateIL': 4,
                                                 'MajorRateNL': 4,
                                                 'MajorRateIH': 4,
                                                 'MajorRateNH': 4
                                                 }
        else:
            if random.uniform(0, 1) < 0.5:
                yield pages.NormRatingEmployer, {'NormRateIL': 1,
                                                 'NormRateNL': 2,
                                                 'NormRateIH': 3,
                                                 'NormRateNH': 4,
                                                 'MajorRateIL': 4,
                                                 'MajorRateNL': 4,
                                                 'MajorRateIH': 4,
                                                 'MajorRateNH': 4
                                                 }

                yield pages.NormRatingWorker_Copy, {'NormRateLI': 6,
                                                    'NormRateHI': 3,
                                                    'NormRateLN': 2,
                                                    'NormRateHN': 1,
                                                    'MajorRateLI': 1,
                                                    'MajorRateHI': 1,
                                                    'MajorRateLN': 1,
                                                    'MajorRateHN': 1
                                                    }
            else:
                yield pages.NormRatingEmployer, {'NormRateIL': 6,
                                                 'NormRateNL': 3,
                                                 'NormRateIH': 2,
                                                 'NormRateNH': 1,
                                                 'MajorRateIL': 4,
                                                 'MajorRateNL': 4,
                                                 'MajorRateIH': 4,
                                                 'MajorRateNH': 4
                                                 }

                yield pages.NormRatingWorker_Copy, {'NormRateLI': 1,
                                                    'NormRateHI': 2,
                                                    'NormRateLN': 3,
                                                    'NormRateHN': 4,
                                                    'MajorRateLI': 1,
                                                    'MajorRateHI': 1,
                                                    'MajorRateLN': 1,
                                                    'MajorRateHN': 1
                                                    }