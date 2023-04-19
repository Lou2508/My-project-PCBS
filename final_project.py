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
def draw_rectangle(rect_size, col, trait):
    R=stimuli.Rectangle(size=rect_size, colour=col, line_width=trait)
    return R

def draw_diamond(trait, col):
    L1=stimuli.Line(start_point=(150, 104), end_point=(178, 132), line_width=trait, colour=col)
    L2=stimuli.Line(start_point=(178, 132), end_point=(150, 160), line_width=trait, colour=col)
    L3=stimuli.Line(start_point=(150, 160), end_point=(122, 132), line_width=trait, colour=col)
    L4=stimuli.Line(start_point=(122, 132), end_point=(150, 104), line_width=trait, colour=col)
    return L1
    return L2
    return L3
    return L4

def two_circles(r, col, pos_top, pos_down):
    C1=stimuli.Circle(radius=r, colour=col, position=pos_top)
    C2=stimuli.Circle(radius=r, colour=col, position=pos_down)
    return C1
    return C2

def three_circles(r,col, pos_top, pos_mid, pos_down):
    C1=stimuli.Circle(radius=r, colour=col, position=pos_top)
    C2=stimuli.Circle(radius=r, colour=col, position=pos_mid)
    C3=stimuli.Circle(radius=r, colour=col, position=pos_down)
    return C1
    return C2
    return C3

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

#block design
congruent_top=[rect_two(0), diam_three(0)]
congruent_bot=[rect_two(1), diam_three(1)]
incongruent_top=[rect_three(0), diam_two(0)]
incongruent_bot=[rect_three(1), diam_two(1)]

def design_cong(list_pos, block_name):
    for fig in enumerate(list_pos):
        t=design.Trial()
        t.add_stimulus(fig)
        block_name.add_trial(t, (N_TRIALS/4))
def design_incong(list_pos, block_name):
    for fig in enumerate(list_pos):
        t=design.Trial()
        t.add_stimulus(fig)
        block_name.add_trial(t, (N_TRIALS/4))

block_up=design.Block()
design_cong(congruent_top, block_up)
design_incong(incongruent_top, block_up)
block_up.shuffle_trials()

block_bot=design.Block()
design_cong(congruent_bot, block_bot)
design_incong(incongruent_bot, block_bot)
block_bot.shuffle_trials()

#Feedback messages
feedback_time=stimuli.TextLine("Time is up", text_colour=WHITE, text_size=30)
feedback_wrong=stimuli.TextLine("That was the wrong key", text_colour=WHITE, text_size=30)

#Introductory screen
instructions = stimuli.TextScreen("Instructions",
    f""".During this experiment, you have to carry out two tasks:

    For the top of the frame, you have to press {RECT_RESPONSE_KEY.upper()} when a rectangle appear
    and {DIAM_RESPONSE_KEY.upper()} when a diamond appear.

    For the bottom of the frame, you have to press {TWO_FILL_RESPONSE_KEY.upper()} when there is 2 circles
    inside the figure and {THREE_FILL_RESPONSE_KEY.upper()} when there is 3 circles.

    The {N_TRIALS/2} first trials, you will only have to do the shape task.
    The {N_TRIALS/2} next trials, you will only have to do the filling task.
    Then, you both tasks will be mixed for {N_TRIALS} 

    There will be {N_TRIALS *2} trials in total. You have 4s to respond for each trial.

    The first question asks for your gender: you can press {M_RESPONSE_KEY.upper()} for male, 
    {F_RESPONSE_KEY.upper()} for female, {O_RESPONSE_KEY.upper()} for other.

    Press the spacebar to start.""")

exp.add_data_variable_names(['gender', 'key', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

#gender question
blankscreen.present()
gender.present()
key, rt = exp.keyboard.wait_char([M_RESPONSE_KEY, F_RESPONSE_KEY, O_RESPONSE_KEY],
                                     duration=MAX_RESPONSE_DELAY)
exp.data.add(gender)

#experiment
blankscreen.present()
exp.clock.wait(1000)
up_frame.present(clear=True, update=False)
down_frame.present(clear=False, update=False)
shape_instruction.present(clear=False, update=False)
filling_instruction.present(clear=False, update=True)
exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)

#first block
for t in block_up.trials:
    t.present()
    key, rt = exp.keyboard.wait_char([RECT_RESPONSE_KEY, DIAM_RESPONSE_KEY],
                                     duration=MAX_RESPONSE_DELAY)
    exp.data.add([key, rt])
  
control.end()

control.end()
