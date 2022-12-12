from . import models
from ._builtin import Page, WaitPage


class Splash(Page):
    pass


class Welcome(Page):
    pass


class Introduction(Page):
    pass


class InformationSheet(Page):
    pass


page_sequence = [
    Splash,
    Welcome,
    Introduction,
    InformationSheet
]
