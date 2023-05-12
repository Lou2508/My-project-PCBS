#Multi-tasking experiment

#packages
import random
from expyriment import design, control, stimuli

#Settings
N_TRIALS = 20
MID_N=10
QUART_N=5
SIZE_FRAME=(300, 264)
SIZE_ONE_OBJECT=(50, 50)
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
    return l1, l2, l3, l4
def two_circles(r, col, pos_top, pos_down):
    C1=stimuli.Circle(radius=r, colour=col, position=pos_top)
    C2=stimuli.Circle(radius=r, colour=col, position=pos_down)
    return c1, c2

def three_circles(r,col, pos_top, pos_mid, pos_down):
    C1=stimuli.Circle(radius=r, colour=col, position=pos_top)
    C2=stimuli.Circle(radius=r, colour=col, position=pos_mid)
    C3=stimuli.Circle(radius=r, colour=col, position=pos_down)
    return c1, c2, c3

#prepare the stimuli
def diam_two(pos):
    one_object=stimuli.Canvas(SIZE_ONE_OBJECT)
    L1, L2, L3, L4 = draw_diamond(LINE_WIDTH, BLACK)
    L1.plot(one_object)
    L2.plot(one_object)
    L3.plot(one_object)
    L4.plot(one_object)
    C1, C2=two_circles(RADIUS, BLACK, (0, +6), (0, -6))
    C1.plot(one_object)
    C2.plot(one_object)
    return one_object

def diam_three(pos):
    one_object=stimuli.Canvas(SIZE_ONE_OBJECT)
    L1, L2, L3, L4 = draw_diamond(LINE_WIDTH, BLACK)
    L1.plot(one_object)
    L2.plot(one_object)
    L3.plot(one_object)
    L4.plot(one_object)
    C1, C2, C3=three_circles(RADIUS, BLACK, (0, +11), (0, 0), (0, -11))
    C1.plot(one_object)
    C2.plot(one_object)
    C3.plot(one_object)
    return one_object

def rect_two(pos):
    rectangle=draw_rectangle(SIZE_FIG, BLACK, LINE_WIDTH)
    C1, C2=two_circles(RADIUS, BLACK, (0, +6), (0, -6))
    C1.plot(rectangle)
    C2.plot(rectangle)
    return rectangle

def rect_three(pos):
    rectangle=draw_rectangle(SIZE_FIG, BLACK, LINE_WIDTH)
    C1, C2, C3=three_circles(RADIUS, BLACK, (0, +11), (0, 0), (0, -11))
    C1.plot(rectangle)
    C2.plot(rectangle)
    C3.plot(rectangle)
    return rectangle

blankscreen = stimuli.BlankScreen()

#block design
def design_cong(shape1, shape2, frame, block_name):
    t=design.Trial()
    shape1.plot(frame)
    shape2.plot(frame)
    t.add_stimulus(shape1)
    T=design.Trial()
    T.add_stimulus(shape2)
    block_name.add_trial(t, QUART_N)
    block_name.add_trial(T, QUART_N)
def design_incong(shape1, shape2, frame, block_name):
    t=design.Trial()
    shape1.plot(frame)
    shape2.plot(frame)
    t.add_stimulus(shape1)
    T=design.Trial()
    T.add_stimulus(shape2)
    block_name.add_trial(t, QUART_N)
    block_name.add_trial(T, QUART_N)

block_up=design.Block()
design_cong(rect_two(),diam_three(), up_frame, block_up)
design_incong(rect_three(), diam_two(), up_frame, block_up)
block_up.shuffle_trials()

block_bot=design.Block()
design_cong(rect_two(), diam_three(), down_frame, block_bot)
design_incong(rect_three(),diam_two(), down_frame, block_bot)
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

    The {MID_N} first trials, you will only have to do the shape task.
    The {MID_N} next trials, you will only have to do the filling task.
    Then, both tasks will be mixed for {N_TRIALS} trials 

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
