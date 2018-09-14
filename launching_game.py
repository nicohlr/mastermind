# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @author: Nicolas Houlier

import game
import random
import ipywidgets as wd
from IPython.display import display


class Launch:

    def __init__(self, combination: list = None):

        self.combination = [
            random.randint(1, 4)]*4 if not combination else combination

        self.trials = wd.VBox()
        self.selectors = wd.HBox()
        self.user_interact = wd.VBox()
        self.game_container = wd.VBox([self.user_interact, self.trials])
        
        self.mapping_colors = {1: 'info',
                               2: 'danger', 3: 'primary', 4: 'success'}

        self.create_gui()

        display(self.game_container)

    def create_gui(self):

        selectors_widgets = list()

        for n in range(4):
            selectors_widgets.append(wd.Dropdown(
                options={'': 0, 'sky blue': 1, 'red': 2, 'blue': 3, 'green': 4},
                value=None,
                disabled=False,
            ))
        
        confirm_button = wd.Button(description='Confirm combination')

        def create_combination_and_rate(_):

            selection=wd.HBox()

            selection_widgets = list()
            for selector in self.selectors.children:
                if selector.value != 0:
                    selection_widgets.append(
                        wd.Button(disabled=True, button_style=self.mapping_colors[selector.value]))
                    selector.value = 0
                else:
                    print('please choose a color for every positions !')

            selection.children = selection_widgets

            self.trials.children = list(self.trials.children) + [selection]

        confirm_button.on_click(create_combination_and_rate)
        self.user_interact.children = [self.selectors, confirm_button]

        self.selectors.children = selectors_widgets
