# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @author: Nicolas Houlier


import time


class GameOfMastermind:

    def __init__(self, good_ans):
        self.good_ans = good_ans

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

    def play(self):
        """
        This method allows you to play a game of mastermind
        """
        
        i = 0
        try_return = [0, 0]

        while i <= 12:  # number of turns in the game limited to 12
            duplicate = []
            avoid = []
            already_checked = []
            player_try = list(input("Enter a list of 4 digits from 1 to 6:"))  # the player is asked to return his or
            # her try.

            for s in player_try:  # check the format of the input entered by the player
                if int(s) > 6 or int(s) < 1:
                    return "Please enter EXACTLY 4 digits between 1 and 6"

            if len(player_try) != 4:  # check the format of the input entered by the player
                return "Please enter EXACTLY 4 digits between 1 and 6"

            print('Your try :', player_try)  # the attempt is displayed

            for j in range(0, 4):  # we first check if there are any pieces of the right value well placed.
                if player_try[j] == self.good_ans[j]:
                    try_return[1] += 1
                    already_checked += [player_try[j]]
                    avoid += [j]

            for p in range(0, 4):
                for s in range(0, 4):
                    if not GameOfMastermind.belong(p, avoid):
                            if player_try[s] == self.good_ans[p] and not GameOfMastermind.belong(
                                                                                                player_try[s],
                                                                                                already_checked
                                                                                                ):
                                try_return[0] += 1
                                duplicate += [player_try[s]]
                                if duplicate.count(player_try[s]) > 1:
                                    try_return[0] -= 1

            # the result of the attempt is displayed
            print("Number of counter (s) of the correct value not placed correctly:", try_return[0])
            print("Number of counter (s) of the correct value placed correctly:", try_return[1])
            i += 1  # we pass the turn
            if try_return == [0, 4]:  # see if the player wins.
                print('You win, the answer is:', self.good_ans, 'you found in', i, 'move(s).')
                return
            else:  # if the player has not won, we reset the counter of well/misplaced checkers and wait 7 seconds
                # before asking for another attempt.
                try_return = [0, 0]
            time.sleep(7)
