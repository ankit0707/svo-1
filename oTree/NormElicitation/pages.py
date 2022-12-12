from . import models
from ._builtin import Page, WaitPage
from .models import Constants

from django import forms
from otree.forms import SliderInput


class SliderPage(Page):
    form_model = 'player'
    form_fields = ['Act1', 'Act2', 'Act3', 'Act4', 'Act5']


class Introduction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True

    def vars_for_template(self):
        return {
            'participation_fee': self.session.config['participation_fee']
        }


class Instructions(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True


class Quiz(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True

    form_model = models.Player
    form_fields = ['q2', 'q3', 'q4', 'q5']


class QuizAnswers(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True

    form_model = models.Player
    form_fields = []


class NormIntro(Page):
    pass


class NormIntroEx1(Page):
    pass


class NormIntroEx2(Page):
    pass


class NormIntroEx3(Page):
    pass


class NormIntroQuiz(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True

    form_model = models.Player
    form_fields = ['NormQ1', 'NormQ2', 'NormQ3']


class NormIntroQuizAnswers(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True

    form_model = models.Player
    form_fields = []


class Situation_C(SliderPage):
    def is_displayed(self):
        return self.player.WorkerPage_first

    form_model = 'player'
    form_fields = ["Act1", "Act2", "Act3", "Act4", "Act5"]

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['response'].widget = SliderInput(
    #         min_value=1, max_value=5, initial=3, step=1
    #     )
    #     return form
    #
    # def post(self):
    #     self.player.act1 = self.form.cleaned_data['act1']
    #     self.player.act2 = self.form.cleaned_data['act2']
    #     self.player.act3 = self.form.cleaned_data['act3']
    #     self.player.act4 = self.form.cleaned_data['act4']
    #     self.player.act5 = self.form.cleaned_data['act5']
    #


class Situation_B(SliderPage):
    def is_displayed(self):
        return not self.player.WorkerPage_first

    form_model = 'player'
    form_fields = ["Act1", "Act2", "Act3", "Act4", "Act5"]


class Situation_A(SliderPage):
    form_model = 'player'
    form_fields = ['Act1', 'Act2', 'Act3', 'Act4', 'Act5']

    def vars_for_template(self):
        return {'likert_choices': Constants.likert_choices}


class NormRatingWaitingPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(self):
        return {
            'RoundPayoff': '£%.2f' % self.participant.vars['payoff'],
            'participation_fee': self.session.config['participation_fee'],
            'final_payment': '£%.2f' % (self.participant.vars['payoff'] + self.session.config['participation_fee'])
            # 'final_payment': '£%.2f' % (self.participant.vars['payoff'])
        }


class Situation_D(Page):
    form_model = 'player'
    form_fields = ["Act1", "Act2", "Act3", "Act4", "Act5"
                   ]


page_sequence = [

    # NormIntro,
    # NormIntroEx1,
    # NormIntroEx2,
    # NormIntroEx3,
    Situation_A,
    # Situation_B,
    # Situation_C,
    # Situation_D,
    # # Results
]
