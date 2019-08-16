# Constants
define n = Character("Narrator")

# Globals
$ age = 0
$ name = ""

label start:
    "In the great green room, there was a telephone "
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
    "You've snoozed [snoozes](s) times."
    return

label get_up:
    "You decide to get up."
    "You know you have to go to work and deal with some bullshit today."
    "Fuck this shit."
    "..."
    "Fuck it. Time to drag yourself into the shower and commence the day."
