from typing import List

from ._builtin import Page, WaitPage
from . import models


#
# class Overview(Page):
#     def vars_for_template(self):
#         return {'title': "Overview",
#                 'button_text': "Next"}
#
#
# class Part1(Page):
#     def vars_for_template(self):
#         return {'title': "Instructions for Part 1",
#                 'button_text': "Next"}
#
#
# class Matching(Page):
#     def vars_for_template(self):
#         return {'title': "Matching",
#                 'button_text': "Next"}
#
#
# class AboutYou(Page):
#     form_model = 'player'
#
#     def vars_for_template(self):
#         return {'title': "A bit about you...",
#                 'button_text': "Next"}
#
#
#


class Head_1(Page):
    form_model = 'player'
    template_name = "Head1.html"
    form_fields = ['Plausibility', 'Familiarity', 'Importance', 'Worryingness']

    def before_next_page(self):
        # Store the responses in the `participant.vars` dictionary
        self.player.participant.vars['Plausibility'] = self.player.Plausibility
        self.player.participant.vars['Familiarity'] = self.player.Familiarity
        self.player.participant.vars['Importance'] = self.player.Importance
        self.player.participant.vars['Worryingness'] = self.player.Worryingness

        # Reset the values of the form fields
        self.player.Plausibility = None
        self.player.Familiarity = None
        self.player.Importance = None
        self.player.Worryingness = None

    def vars_for_template(self):
        return {'title': "Covid-19 News",
                'button_text': "Next"}


class Head_2(Page):
    form_model = 'player'
    template_name = "Head2.html"
    form_fields = ['Plausibility', 'Familiarity', 'Importance', 'Worryingness']

    def before_next_page(self):
        # Store the responses in the `participant.vars` dictionary
        self.player.participant.vars['Plausibility'] = self.player.Plausibility
        self.player.participant.vars['Familiarity'] = self.player.Familiarity
        self.player.participant.vars['Importance'] = self.player.Importance
        self.player.participant.vars['Worryingness'] = self.player.Worryingness

        # Reset the values of the form fields
        self.player.Plausibility = None
        self.player.Familiarity = None
        self.player.Importance = None
        self.player.Worryingness = None

    def vars_for_template(self):
        return {'title': "Covid-19 News",
                'button_text': "Next"}


class Head_3(Page):
    form_model = 'player'
    template_name = "Head3.html"
    form_fields = ['Plausibility', 'Familiarity', 'Importance', 'Worryingness']

    def before_next_page(self):
        # Store the responses in the `participant.vars` dictionary
        self.player.participant.vars['Plausibility'] = self.player.Plausibility
        self.player.participant.vars['Familiarity'] = self.player.Familiarity
        self.player.participant.vars['Importance'] = self.player.Importance
        self.player.participant.vars['Worryingness'] = self.player.Worryingness

        # Reset the values of the form fields
        self.player.Plausibility = None
        self.player.Familiarity = None
        self.player.Importance = None
        self.player.Worryingness = None

    def vars_for_template(self):
        return {'title': "Covid-19 News",
                'button_text': "Next"}


class Head_4(Page):
    form_model = 'player'
    template_name = "Head4.html"
    form_fields = ['Plausibility', 'Familiarity', 'Importance', 'Worryingness']

    def before_next_page(self):
        # Store the responses in the `participant.vars` dictionary
        self.player.participant.vars['Plausibility'] = self.player.Plausibility
        self.player.participant.vars['Familiarity'] = self.player.Familiarity
        self.player.participant.vars['Importance'] = self.player.Importance
        self.player.participant.vars['Worryingness'] = self.player.Worryingness

        # Reset the values of the form fields
        self.player.Plausibility = None
        self.player.Familiarity = None
        self.player.Importance = None
        self.player.Worryingness = None

    def vars_for_template(self):
        return {'title': "Covid-19 News",
                'button_text': "Next"}

    # def vars_for_admin_report(self):
    #     # include other variables here as needed
    #     plausibility_responses = [player.Plausibility for player in self.get_players()]
    #
    #     return dict(
    #         plausibility_responses=plausibility_responses,
    #     )


class YourGender(Page):
    form_model = 'player'
    template_name = 'global/SimplePage.html'
    form_fields = ['your_gender']

    def vars_for_template(self):
        return {'title': "Covid-19 News",
                'button_text': "Next"}


class YourEthnicity(Page):
    form_model = 'player'
    template_name = 'global/SimplePage.html'
    form_fields = ['your_ethnicity']

    def vars_for_template(self):
        return {'title': "Covid-19 News",
                'button_text': "Next"}


#
# class AboutThem(Page):
#     form_model = 'player'
#     template_name = "Misinfo/AboutThem.html"
#
#     def vars_for_template(self):
#         return {'title': "About the participant with whom you are matched...",
#                 'correct_answer': models.Constants.correct_answer,
#                 'button_text': "Continue to questions"
#                 }
#
#
# # class TheirQuestions(Page):
# #     form_model = 'player'
# #     template_name = "global/SimplePage.html"
#
#     # def vars_for_template(self):
#     #     return {'title': "About the participant with whom you are matched..."}
#
#
# class TheirBeverage(TheirQuestions):
#     form_fields = ['their_beverage']
#
#     def is_displayed(self):
#         return self.player.ask_beverage
#
#
# class TheirColour(TheirQuestions):
#     form_fields = ['their_colour']
#
#     def is_displayed(self):
#         return self.player.ask_colour
#
#
# class TheirBirthMonth(TheirQuestions):
#     form_fields = ['their_birthmonth']
#
#     def is_displayed(self):
#         return self.player.ask_birthmonth
#
#
# class TheirGender(TheirQuestions):
#     form_fields = ['their_gender']
#
#     def is_displayed(self):
#         return self.player.ask_gender
#
#
# class TheirBirthDay(TheirQuestions):
#     form_fields = ['their_birthday']
#
#     def is_displayed(self):
#         return self.player.ask_birthday


class Part1Results(Page):
    pass
    # def vars_for_template(self):
    #     return {
    #         "button_text": "Next",
    #         "question_value": models.Constants.correct_answer,
    #         "summary": [
    #             {"question": "Beverage",
    #              "response": models.Constants.beverage_choices.get(self.player.their_beverage, ""),
    #              "correct": models.Constants.beverage_choices.get(self.player.get_matched_player().your_beverage, "")
    #              },
    #             {"question": "Colour",
    #              "response": models.Constants.colour_choices.get(self.player.their_colour, ""),
    #              "correct": models.Constants.colour_choices.get(self.player.get_matched_player().your_colour, "")
    #              },
    #             {"question": "Birth month",
    #              "response": models.Constants.birthmonth_choices.get(self.player.their_birthmonth, ""),
    #              "correct": models.Constants.birthmonth_choices.get(self.player.get_matched_player().your_birthmonth,
    #                                                                 "")
    #              },
    #             {"question": "Birth day",
    #              "response": models.Constants.birthday_choices.get(self.player.their_birthday, ""),
    #              "correct": models.Constants.birthday_choices.get(self.player.get_matched_player().your_birthday, "")
    #              },
    #         ]
    #     }
    #
    # def before_next_page(self):
    #     if self.player.paid_part == 1:
    #         self.player.payoff = self.player.quiz_earnings
    #


#
# class Part2(Page):
#     def vars_for_template(self):
#         return {'title': "your decision",
#                 'button_text': "Next"}


class Part2Decision(Page):
    form_model = 'player'
    form_fields = ['give']

    def vars_for_template(self):
        return {'button_text': "Confirm"}

    def error_message(self, values):
        if values['give'] < 0 or values['give'] > 100:
            return 'You can specify any amount between 0 and 200 to give to the other participant.'


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(self):
        return {
            "button_text": "Next",
            "question_value": models.Constants.correct_answer,
            "summary": [
                {"question": "Beverage",
                 "response": models.Constants.beverage_choices.get(self.player.their_beverage, ""),
                 "correct": models.Constants.beverage_choices.get(self.player.get_matched_player().your_beverage, "")
                 },
                {"question": "Colour",
                 "response": models.Constants.colour_choices.get(self.player.their_colour, ""),
                 "correct": models.Constants.colour_choices.get(self.player.get_matched_player().your_colour, "")
                 },
                {"question": "Birth month",
                 "response": models.Constants.birthmonth_choices.get(self.player.their_birthmonth, ""),
                 "correct": models.Constants.birthmonth_choices.get(self.player.get_matched_player().your_birthmonth,
                                                                    "")
                 },
                {"question": "Birth day",
                 "response": models.Constants.birthday_choices.get(self.player.their_birthday, ""),
                 "correct": models.Constants.birthday_choices.get(self.player.get_matched_player().your_birthday, "")
                 },
            ]
        }

    def before_next_page(self):
        if self.player.paid_part == 1:
            self.player.payoff = self.player.quiz_earnings
        else:
            self.player.payoff = self.player.dictator_earnings


class Debrief(Page):
    pass


class Earnings(Page):
    pass


class Instructions2(Page):
    pass


page_sequence = [
    # Questions about yourself
    Instructions2,
    Head_1,
    Head_2,
    Head_3,
    Head_4,
    YourGender,
    YourEthnicity,
    #
    # # instructions starts here
    # Overview,
    # Part1,
    # Matching,
    #
    # # Quizzing about other participant
    # AboutThem,
    # TheirBeverage,
    # TheirColour,
    # TheirBirthMonth,
    # TheirBirthDay,
    #
    # # part 2
    # Part2,
    # Part2Decision,
    # ResultsWaitPage,
    #
    # # Final debrief: ask assessment of gender
    # Debrief,

    # Results,
    # Earnings
]
