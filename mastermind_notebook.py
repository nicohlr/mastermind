# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @author: Nicolas Houlier

import game
import random
import ipywidgets as wd
from IPython.display import display


class MastermindNotebook:

    def __init__(self, answer: list = None):

        self.answer = [
            random.randint(1, 4)]*4 if not answer else answer

        self.trials = wd.VBox()
        self.selectors = wd.HBox()
        self.user_interact = wd.VBox()
        self.console = wd.HBox()
        self.game_container = wd.VBox(
            [self.trials, self.user_interact, self.console])

        self.confirm_button = wd.Button(description='Confirm combination')

        self.new_game_button = wd.Button(description='New game', layout={'margin': '0px 0px 0px 20px'})

        self.new_game_button.on_click(self.new_game_function())

        self.turn = 0
        self.duplicate = []
        self.avoid = []
        self.already_checked = []
        self.try_return = [0, 0]

        self.mapping_colors = {1: 'warning',
                               2: 'danger', 3: 'primary', 4: 'success'}

        self.create_gui()

        display(self.game_container)

    def create_gui(self):

        selectors_widgets = list()

        for n in range(4):

            selectors_widgets.append(wd.Dropdown(
                options={'': 0, 'orange': 1, 'red': 2, 'blue': 3, 'green': 4},
                value=0,
                disabled=False,
            ))

        self.confirm_button.on_click(self.create_combination_and_rate_function())
        self.user_interact.children = [self.selectors, self.confirm_button]

        self.selectors.children = selectors_widgets

    def check_combination(self, combination):

        # we first check if there are any pieces of the right value well placed.
        for j in range(0, 4):
            if combination[j] == self.answer[j]:
                self.try_return[1] += 1
                self.already_checked += [combination[j]]
                self.avoid += [j]

        for p in range(0, 4):
            for s in range(0, 4):
                if not self.belong(p, self.avoid):
                    if combination[s] == self.answer[p] and not self.belong(
                        combination[s],
                        self.already_checked
                    ):

                        self.try_return[0] += 1
                        self.duplicate += [combination[s]]
                        if self.duplicate.count(combination[s]) > 1:
                            self.try_return[0] -= 1

    @staticmethod
    def belong(n, tab):
        """
        Args:
            n (int): element to be finded in the array
            tab (list): array

        This method makes it possible to find if an element n
        belongs to an array tab, it will be used in the play method"""

        response = False
        for i in tab:
            if n == i:
                response = True
                break
        return response

    def new_game_function(self):

        def new_game(_):
            self.console.children = []
            self.trials.children = []
            self.turn = 0
            for selector in self.selectors.children:
                selector.disabled = False
            self.confirm_button.disabled = False
            self.try_return = [0, 0]

        return new_game

    def create_combination_and_rate_function(self):

        def create_combination_and_rate(_):

            self.console.children = []

            selection = wd.HBox()

            selection_widgets = list()
            if not 0 in (dropdown.value for dropdown in self.selectors.children):
                
                self.turn += 1

                user_try = list()

                for selector in self.selectors.children:
                    selection_widgets.append(
                        wd.Button(disabled=True, button_style=self.mapping_colors[selector.value]))

                    user_try.append(selector.value)
                    selector.value = 0

                self.duplicate = []
                self.avoid = []
                self.already_checked = []

                self.check_combination(combination=user_try)

                selection_widgets.append(
                    wd.Button(description='Turn {0} - Well placed: {1} \n - Misplaced: {2}'.format(self.turn,
                                                                                                   self.try_return[1], self.try_return[0]),
                              disabled=True,
                              layout={'width': 'auto'}
                              )
                )

                if self.try_return == [0, 4]:  # see if the player wins.

                    self.console.children = [wd.Label(value='You win !'), self.new_game_button]
                    for selector in self.selectors.children:
                        selector.disabled = True
                    self.confirm_button.disabled = True

                else:  # if the player has not won, we reset the counter of well/misplaced checkers and wait 7 seconds
                    # before asking for another attempt.
                    if self.turn == 12:

                        self.console.children = [wd.Label(value='You loose !'),  self.new_game_button]
                        for selector in self.selectors.children:
                            selector.disabled = True
                        self.confirm_button.disabled = True
                    
                    else:
                        self.try_return = [0, 0]

            else:
                self.console.children = [
                    wd.Label(value='Please choose a color for every positions !')]

            selection.children = selection_widgets

            self.trials.children = list(self.trials.children) + [selection]

        return create_combination_and_rate