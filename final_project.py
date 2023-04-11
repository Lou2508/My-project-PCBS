#Multi-tasking experiment

#packages
import random
from expyriment import design, control, stimuli

#Settings
N_TRIALS = 20
SIZE_FRAME=(80, 80)
SIZE_FIG=(20, 20)
BLACK= (0, 0, 0)
WHITE=(255, 255, 255)
YELLOW=(255, 255, 0)
LINE_WIDTH= 2
MAX_RESPONSE_DELAY=2000
RECT_RESPONSE_KEY = 'e'
DIAM_RESPONSE_KEY = 'i'
2_FILL_REPONSE_KEY = 'c'
3_FILL_RESPONSE_KEY = 'n'

exp = design.Experiment(name="Multi-tasking", text_size=30)
control.initialize(exp)

#prepare the frame
rectangle=stimuli.Rectangle(SIZE_FRAME, YELLOW)

#prepare the stimuli

#Introductory screen
instructions = stimuli.TextScreen("Instructions",
    f""".During this experiment, you have to carry out two tasks:

    For the top of the frame, you have to press {RECT_RESPONSE_KEY.upper()} when a rectangle appear
    and {DIAM_RESPONSE_KEY.upper()} when a diamond appear.

    For the bottom of the frame, you have to press {2_FILL_RESPONSE_KEY.upper()} when there is 2 circles
    inside the figure and {3_FILL_RESPONSE_KEY.upper()} when there is 3 circles.

    Try to do those tasks simultaneously.

    There will be {N_TRIALS} trials in total.

    Press the spacebar to start.""")

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

#experiment






control.end()
