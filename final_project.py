#Multi-tasking experiment

#packages
import random
from expyriment import design, control, stimuli

#Settings
N_TRIALS = 20
SIZE_FRAME=(300, 264)
SIZE_FIG=(40, 40)
RADIUS=5
BLACK= (0, 0, 0)
WHITE=(255, 255, 255)
YELLOW=(255, 255, 0)
LINE_WIDTH= 2
MAX_RESPONSE_DELAY=2000
RECT_RESPONSE_KEY = 'e'
DIAM_RESPONSE_KEY = 'i'
TWO_FILL_RESPONSE_KEY = 'c'
THREE_FILL_RESPONSE_KEY = 'n'
M_RESPONSE_KEY= 'm'
F_RESPONSE_KEY= 'f'
O_RESPONSE_KEY= 'o'

exp = design.Experiment(name="Multi-tasking", text_size=30, background_colour= BLACK)
control.initialize(exp)

#prepare the frame
up_frame=stimuli.Canvas(SIZE_FRAME, position=(0, +134), colour=YELLOW)
down_frame=stimuli.Canvas(SIZE_FRAME, position=(0, -134), colour=YELLOW)
frame=[up_frame, down_frame]
shape_instruction=stimuli.TextLine("SHAPE", position=(0, +280), text_colour=WHITE)
filling_instruction=stimuli.TextLine("FILLING", position=(0,-280), text_colour=WHITE)

#asking for gender
gender=stimuli.TextLine("What gender do you identify to?", text_colour=WHITE, text_size=30)

#prepare the features
def draw_rectangle(size, colour, line_width):
    stimuli.rectangle(size, colour, line_width)

def draw_diamond(trait, col):
    stimuli.Line(start_point=(150, 104), end_point=(178, 132), line_width=trait, colour=col)
    stimuli.Line(start_point=(178, 132), end_point=(150, 160), line_width=trait, colour=col)
    stimuli.Line(start_point=(150, 160), end_point=(122, 132), line_width=trait, colour=col)
    stimuli.Line(start_point=(122, 132), end_point=(150, 104), line_width=trait, colour=col)

def two_circles(r, col, pos_top, pos_down):
    stimuli.Circle(radius=r, colour=col, position=pos_top)
    stimuli.Circle(radius=r, colour=col, position=pos_down)

def three_circles(r,col, pos_top, pos_mid, pos_down):
    stimuli.Circle(radius=r, colour=col, position=pos_top)
    stimuli.Circle(radius=r, colour=col, position=pos_mid)
    stimuli.Circle(radius=r, colour=col, position=pos_down)

#prepare the stimuli
def diam_two(pos):
    diamond=draw.diamond(LINE_WIDTH, BLACK)
    diamond.plot(frame[pos])
    circles=two_circles(RADIUS, BLACK, (0, +6), (0, -6))
    circles.plot(diamond)

def diam_three(pos):
    diamond=draw.diamond(LINE_WIDTH, BLACK)
    diamond.plot(frame[pos])
    circles=three_circles(RADIUS, BLACK, (0, +11), (0, 0), (0, -11))
    circles.plot(diamond)

def rect_two(pos):
    rectangle=draw_rectangle(SIZE_FIG, BLACK, LINE_WIDTH)
    rectangle.plot(frame[pos])
    circles=two_circles(RADIUS, BLACK, (0, +6), (0, -6))
    circles.plot(rectangle)

def rect_three(pos):
    rectangle=draw_rectangle(SIZE_FIG, BLACK, LINE_WIDTH)
    rectangle.plot(frame[pos])
    circles=three_circles(RADIUS, BLACK, (0, +11), (0, 0), (0, -11))
    circles.plot(rectangle)

blankscreen = stimuli.BlankScreen()

#randomisation of incongruent

#Feedback messages


#Introductory screen
instructions = stimuli.TextScreen("Instructions",
    f""".During this experiment, you have to carry out two tasks:

    For the top of the frame, you have to press {RECT_RESPONSE_KEY.upper()} when a rectangle appear
    and {DIAM_RESPONSE_KEY.upper()} when a diamond appear.

    For the bottom of the frame, you have to press {TWO_FILL_RESPONSE_KEY.upper()} when there is 2 circles
    inside the figure and {THREE_FILL_RESPONSE_KEY.upper()} when there is 3 circles.

    Try to do those tasks simultaneously.

    There will be {N_TRIALS} trials in total.

    The first question asks for your gender: you can press {M_RESPONSE_KEY.upper()} for male, 
    {F_RESPONSE_KEY.upper()} for female, {O_RESPONSE_KEY.upper()} for other.

    Press the spacebar to start.""")

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

#gender question
blankscreen.present()
gender.present()
key, rt = exp.keyboard.wait_char([M_RESPONSE_KEY, F_RESPONSE_KEY, O_RESPONSE_KEY],
                                     duration=MAX_RESPONSE_DELAY)
#experiment
blankscreen.present()
exp.clock.wait(1000)
up_frame.present(clear=True, update=False)
down_frame.present(clear=False, update=False)
shape_instruction.present(clear=False, update=False)
filling_instruction.present(clear=False, update=True)
exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)

control.end()
