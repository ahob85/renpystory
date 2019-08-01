# Constants
define n = Character("Narrator")

# Globals
$ age = 0
$ name = ""

label start:
    $ snoozes = 0;
    menu snooze_choice:
        "That's the alarm. Time to wake up."
        "Hit snooze.":
            $ snoozes += 1
            call snooze(snoozes)
            jump snooze_choice
        "Get up.":
            jump get_up

label snooze(snoozes):
    "You hit the snooze button and your alarm stops."
    "Time goes by..."
    "..."
    "..."
    "You've snoozed [snoozes] times."
    return

label get_up:
    "You decide to get up."
    "You know you have to go to work and deal with some bullshit today."
    "You'll have to listen to people talk about their lives, shit that's going on with them that you don't give a fuck about." 
    "But you have to pretend you care, so you don't stand out."
