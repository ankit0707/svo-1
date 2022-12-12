from otree.api import widgets
from otree.forms.widgets import Slider

from django.forms.widgets import Input


class Slider(Input):
    input_type = 'range'


# class RadioSelectBipolar(widgets.RadioSelect):
#     template_name = 'NormElicitation/RadioSelectBipolar.html'
#
#     def __init__(self, min, max, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.min = min
#         self.max = max
#         self.slider = Slider()


# class RadioSelectBipolar(RadioSelectHorizontal):
#     template_name = 'NormElicitationStandard/RadioSelectBipolar.html'
#     left = 'left'
#     right = 'right'
#
#     class Media:
#         css = {
#             'all': ('static/RadioSelectHorizontal.css',),
#         }
#
#     def __init__(self, *args, **kwargs):
#         left = kwargs.pop('left', None)
#         if left is not None:
#             self.left = left
#         right = kwargs.pop('right', None)
#         if right is not None:
#             self.right = right
#         self.choices = kwargs.pop('choices', None)
#         super(RadioSelectBipolar, self).__init__(*args, **kwargs)
#
#     def get_context(self, *args, **kwargs):
#         context = super(RadioSelectBipolar, self).get_context(*args, **kwargs)
#         context['left'] = self.left
#         context['right'] = self.right
#         context['choices'] = self.choices
#         return context


class Slider(widgets.Input):
    input_type = 'range'
    template_name = 'widgets/slider.html'

    def __init__(self, attrs=None, min_value=None, max_value=None, step=None, marks=None):
        super().__init__(attrs)
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.marks = marks
