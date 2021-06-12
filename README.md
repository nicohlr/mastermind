# mastermind

This package allows you to play Mastermind directly into a jupyter notebook/lab IDE. It has been made using the great [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/) python library.

## Install

    pip install mastermind

## How to use in a jupyter notebook

Copy and paste the following lines into a cell of a notebook and run it:

    from mastermind import MastermindNotebook
    game = MastermindNotebook()

The game should display, you can start playing by choosing one color for each position and click on "Confirm combination" button !

![GitHub Logo](mastermind/img/screenshot.png)

## How to use in jupyter lab

To use in jupyter lab, don't forget to install the jupyter widget extension:

    jupyter labextension install @jupyter-widgets/jupyterlab-manager

Once this is done, you can proceed in the same way as for the jupyter notebook use.

## State of development

* A Tkinter interface must be developed to play outside a notebook, feel free to contribute !

* Add a DB to record all the games for one user