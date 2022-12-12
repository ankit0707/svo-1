from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

from django.forms.widgets import Input


class Constants(BaseConstants):
    name_in_url = 'NormElicitation'
    players_per_group = None
    num_rounds = 1
    minutes = 30  # Duration of the experiment

    # Likert scale categories
    likert_choices = [
        'Very Socially inappropriate',
        'Socially Inappropriate',
        'Not sure',
        'Socially Appropriate',
        'Very Socially Appropriate'
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    random_choice = models.StringField()


class Player(BasePlayer):
    def other_player(self):
        return self.get_others_in_group()[0]

    # Variables for the quiz of Norm rating task
    Act1 = models.IntegerField(
        label="Get vaccinated when vaccine becomes available",
        choices=list(enumerate(Constants.likert_choices)),
        blank=False,
        widget=widgets.Slider(attrs={'step': 1, 'min': 0, 'max': 4, 'tick_interval': 1})
    )
    Act2 = models.IntegerField(
        label="Wear Masks",
        choices=list(enumerate(Constants.likert_choices)),
        blank=False,
        widget=widgets.Slider(attrs={'step': 1, 'min': 0, 'max': 4})
    )
    Act3 = models.IntegerField(
        label="Self isolate if you experience symptoms",
        choices=list(enumerate(Constants.likert_choices)),
        blank=False,
        widget=widgets.Slider(attrs={'step': 1, 'min': 0, 'max': 4})
    )

    Act4 = models.IntegerField(
        label="Avoid unnecessary public gatherings",
        choices=list(enumerate(Constants.likert_choices)),
        blank=False,
        widget=widgets.Slider(attrs={'step': 1, 'min': 0, 'max': 4})
    )

    Act5 = models.IntegerField(
        label="Maintain 2m distance in Public places",
        choices=list(enumerate(Constants.likert_choices)),
        blank=False,
        widget=widgets.Slider(attrs={'step': 1, 'min': 0, 'max': 4})
    )
