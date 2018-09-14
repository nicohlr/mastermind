<img src="./img/logo.png" width="256" height="112" />

This package allows to play some mastermind games in a jupyter notebook

## Install

    pip install mastermind

## How to use in a jupyter notebook

Copy and paste the following lines into a cell of a notebook and run it:

    from mastermind import MastermindNotebook
    game = MastermindNotebook()

The game should display, you can start playing by choosing one color for each position and click on "Confirm combination" button !

![GitHub Logo](/img/game_capture.png)

## State of development

* A Tkinter interface must be developed to play outside a notebook, feel free to contribute !

* Add a DB to record all the games for one user