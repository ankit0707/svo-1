import random

from django.utils.safestring import mark_safe
from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
    widgets,

)
from pprint import pprint
from random import shuffle
import os

author = 'Ankit Shanker'

doc = """
Dictator game with strategy method
"""


class Constants(BaseConstants):
    name_in_url = 'fixed'
    players_per_group = None
    num_rounds = 1
    endowment = c(100)
    correct_answer = c(25)

    Plausibility_choices = {
        - 3: "Extremely Unlikely",
        -2: "Unlikely",
        -1: "Somewhat UnLikely",
        0: "Neutral",
        1: "somewhat likely",
        2: "likely",
        3: "extremely likely"
    }
    Familiarity_choices = {
        -2: " Completely Unfamiliar",
        -1: "Unfamiliar",
        0: "Unsure",
        1: "Somewhat familiar",
        2: "very familiar"
    }

    Importance_choices = {
        -2: "Extremely Unimportant",
        -1: "Unimportant",
        0: "Neutral",
        1: "Important",
        2: "extremely likely"
    }

    Worryingness_choices = {

        -2: "Not at all",
        -1: "Somewhat worrying",
        0: "Neutral",
        1: "very worrying",
        3: "extremely worrying"
    }
    ethnicity = {
        1: "White/Caucasian",
        2: "Asian/Asian British",
        3: "Black/ African/ Caribbean/ Black British",
        4: "Mixed/ Multiple ethnic groups",
        5: "Other ethnic group",
        6: "Prefer not to say",
    }
    gender_choices = {

        1: "Male",
        2: "Female",
        3: "Other"

    }


class Subsession(BaseSubsession):

    def creating_session(self):

        # Import the `random` module
        import random

        # Import the `mark_safe` function from the `django.utils.safestring` module
        from django.utils.safestring import mark_safe

        # Set the path to the folder containing the images
        IMAGE_FOLDER = 'oTree/_static/news'

        # Get the list of participants in your experiment
        participants = self.get_players()

        # Shuffle the list of participants
        random.shuffle(participants)

        # Split the list of participants into two equal-sized groups
        num_participants = len(participants)
        num_groups = 2
        group_size = num_participants // num_groups
        self.group1 = participants[:group_size]
        self.group2 = participants[group_size:]

        # Set the image paths for each player
        for player in self.group1:
            player.image_paths = [
                IMAGE_FOLDER + '{}_{}.png'.format('False', i)
                for i in range(1, 4)
            ]

            print(player.image_paths)
        for player in self.group2:
            player.image_paths = [
                IMAGE_FOLDER + '{}_{}.png'.format('True', i)
                for i in range(1, 4)
            ]

    def run(self):
        # Pass the list of players and their image paths to the template
        return {
            'group1': self.group1,
            'group2': self.group2,
        }


# def creating_session(self):
#     for player in self.get_players():
#         player.paid_part = random.choice([1, 2])
#         for question in random.sample(['ask_beverage', 'ask_colour', 'ask_birthmonth', 'ask_birthday'], k=2):
#             setattr(player, question, True)
#
# def vars_for_admin_report(self):
#     amount_offered = [
#         player.give for player in self.get_players()
#     ]
#
#     if amount_offered:
#         return dict(
#             min_contribution=min(amount_offered),
#             max_contribution=max(amount_offered),
#
#         )
#     else:
#         return dict(
#             min_contribution='(no data)',
#             max_contribution='(no data)',
#         )


class Group(BaseGroup):
    pass
    # group1 = models.ManyToManyField(Player, related_name='group1')
    # group2 = models.ManyToManyField(Player, related_name='group2')


class Player(BasePlayer):
    Plausibility = models.IntegerField(
        label="What is the likelihood that the above headline is true?",
        choices=[[k, v] for k, v in Constants.Plausibility_choices.items()],
        widget=widgets.RadioSelectHorizontal,
        blank=False,
    )

    Familiarity = models.IntegerField(
        label="Are you familiar with the above headline (have you seen or heard about it before)?",
        choices=[[k, v] for k, v in Constants.Familiarity_choices.items()],
        widget=widgets.RadioSelectHorizontal,
        blank=False,
    )

    Importance = models.IntegerField(
        label="Assuming the headline is entirely accurate, how important would this news be?",
        choices=[[k, v] for k, v in Constants.Importance_choices.items()],
        widget=widgets.RadioSelectHorizontal,
        blank=False,
    )

    Worryingness = models.IntegerField(
        label="How worrying is this headline?",
        choices=[[k, v] for k, v in Constants.Worryingness_choices.items()],
        widget=widgets.RadioSelectHorizontal,
        blank=False,
    )

    # their_birthmonth = models.IntegerField( #     label="Which month was the other participant born in?",
    #     choices=[[k, v] for k, v in Constants.birthmonth_choices.items()],
    #     widget=widgets.RadioSelect,
    #     blank=False,
    # )
    # ask_birthmonth = models.BooleanField(default=False)
    #
    # your_birthday = models.IntegerField(
    #     label="On which day of the week does/did your birthday fall in 2021?",
    #     choices=[[k, v] for k, v in Constants.birthday_choices.items()],
    #     widget=widgets.RadioSelect,
    #     blank=False,
    # )
    # their_birthday = models.IntegerField(
    #     label="On which day of the week does/did the other participant's birthday fall in 2021?",
    #     choices=[[k, v] for k, v in Constants.birthday_choices.items()],
    #     widget=widgets.RadioSelect,
    #     blank=False,
    # )
    # ask_birthday = models.BooleanField(default=False)

    your_gender = models.IntegerField(
        label="What gender do you identify as?",
        choices=[[1, "Male"], [2, "Female"], [3, "Other"]],
        widget=widgets.RadioSelect,
        blank=False,
    )

    # their_gender = models.IntegerField(
    #     label="What gender do you think the other participant identifies as?",
    #     choices=[[1, "Male"], [2, "Female"], [3, "Other"], [4, "I'm not sure"]],
    #     widget=widgets.RadioSelect,
    #     blank=False,
    # )
    # ask_gender = models.BooleanField(default=False)

    your_ethnicity = models.IntegerField(
        label="Which of these best describes your ethnic origin?",
        choices=[[k, v] for k, v in Constants.ethnicity.items()],
        widget=widgets.RadioSelect,
        blank=False,
    )

# def show_images(self):
#     # Get a list of the images in the folder
#     folder_path = 'path/to/folder'
#     image_files = os.listdir(folder_path)
#
#     # Iterate over the images in the folder
#     for image_file in image_files:
#         # Check if the image is labeled False or True
#         if image_file.startswith('False'):
#             # Show the image to group1
#             self.group.show_image(os.path.join(folder_path, image_file))
#         elif image_file.startswith('True'):
#             # Show the image to group2
#             self.group.show_image(os.path.join(folder_path, image_file))
