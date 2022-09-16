init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)
        renpy.random.shuffle(items)
        return renpy_menu(items)
