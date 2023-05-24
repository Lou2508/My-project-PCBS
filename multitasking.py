#Multi-tasking experiment from Stoet et al (2020)

#packages
import random
from expyriment import design, control, stimuli

#Settings
N_TRIALS = 20
MID_N=10
QUART_N=5
SIZE_FRAME=(300, 600)
SIZE_MID_FRAME=(300, 264)
SIZE_ONE_OBJECT=(60, 60)
SIZE_FIG=(40, 40)
RADIUS=5
BLACK= (0, 0, 0)
WHITE=(255, 255, 255)
YELLOW=(255, 255, 0)
LINE_WIDTH= 2
POS_UP=(0, +134)
POS_DOWN=(0, -134)
POS_INSTRU_SHAPE=(0, +280)
POS_INSTRU_FILL=(0, -280)
POS_FEEDBACK_SHAPE=(0, +67)
POS_FEEDBACK_FILL= (0, -67)
MAX_RESPONSE_DELAY=4000
RECT_RESPONSE_KEY = 'e'
DIAM_RESPONSE_KEY = 'i'
TWO_FILL_RESPONSE_KEY = 'c'
THREE_FILL_RESPONSE_KEY = 'n'
M_RESPONSE_KEY= 'm'
F_RESPONSE_KEY= 'f'
O_RESPONSE_KEY= 'o'

exp = design.Experiment(name="Multi-tasking", text_size=30, background_colour= BLACK)
control.initialize(exp)

#asking for gender
gender_question=stimuli.TextLine("What gender do you identify to?", text_colour=WHITE, text_size=30)

#prepare the features
def draw_rectangle(rect_size, col, trait):
    r=stimuli.Rectangle(size=rect_size, colour=col, line_width=trait)
    return r

def draw_diamond(trait, col):
    l1=stimuli.Line(start_point=(0, 28), end_point=(28, 0), line_width=trait, colour=col)
    l2=stimuli.Line(start_point=(28, 0), end_point=(0, -28), line_width=trait, colour=col)
    l3=stimuli.Line(start_point=(0, -28), end_point=(-28, 0), line_width=trait, colour=col)
    l4=stimuli.Line(start_point=(-28, 0), end_point=(0, 28), line_width=trait, colour=col)
    return l1, l2, l3, l4

def two_circles(r, col, pos_top, pos_down):
    c1=stimuli.Circle(radius=r, colour=col, position=pos_top)
    c2=stimuli.Circle(radius=r, colour=col, position=pos_down)
    return c1, c2

def three_circles(r,col, pos_top, pos_mid, pos_down):
    c1=stimuli.Circle(radius=r, colour=col, position=pos_top)
    c2=stimuli.Circle(radius=r, colour=col, position=pos_mid)
    c3=stimuli.Circle(radius=r, colour=col, position=pos_down)
    return c1, c2, c3

#prepare the stimuli
def diam_two(pos):
    frame=stimuli.Canvas(SIZE_FRAME, colour=BLACK)
    up_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_UP, colour=YELLOW)
    up_frame.plot(frame)
    down_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_DOWN, colour=YELLOW)
    down_frame.plot(frame)
    shape_instruction=stimuli.TextLine("SHAPE", position=POS_INSTRU_SHAPE, text_colour=WHITE)
    shape_instruction.plot(frame)
    filling_instruction=stimuli.TextLine("FILLING", position=POS_INSTRU_FILL, text_colour=WHITE)
    filling_instruction.plot(frame)
    canva=stimuli.Canvas(SIZE_ONE_OBJECT, position = pos, colour=YELLOW)
    L1, L2, L3, L4 = draw_diamond(LINE_WIDTH, BLACK)
    L1.plot(canva)
    L2.plot(canva)
    L3.plot(canva)
    L4.plot(canva)
    C1, C2=two_circles(RADIUS, BLACK, (0, +6), (0, -6))
    C1.plot(canva)
    C2.plot(canva)
    canva.plot(frame)
    return frame

def diam_three(pos):
    frame=stimuli.Canvas(SIZE_FRAME, colour=BLACK)
    up_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_UP, colour=YELLOW)
    up_frame.plot(frame)
    down_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_DOWN, colour=YELLOW)
    down_frame.plot(frame)
    shape_instruction=stimuli.TextLine("SHAPE", position=POS_INSTRU_SHAPE, text_colour=WHITE)
    shape_instruction.plot(frame)
    filling_instruction=stimuli.TextLine("FILLING", position=POS_INSTRU_FILL, text_colour=WHITE)
    filling_instruction.plot(frame)
    canva=stimuli.Canvas(SIZE_ONE_OBJECT, position=pos, colour=YELLOW)
    L1, L2, L3, L4 = draw_diamond(LINE_WIDTH, BLACK)
    L1.plot(canva)
    L2.plot(canva)
    L3.plot(canva)
    L4.plot(canva)
    C1, C2, C3=three_circles(RADIUS, BLACK, (0, +11), (0, 0), (0, -11))
    C1.plot(canva)
    C2.plot(canva)
    C3.plot(canva)
    canva.plot(frame)
    return frame

def rect_two(pos):
    frame=stimuli.Canvas(SIZE_FRAME, colour=BLACK)
    up_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_UP, colour=YELLOW)
    up_frame.plot(frame)
    down_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_DOWN, colour=YELLOW)
    down_frame.plot(frame)
    shape_instruction=stimuli.TextLine("SHAPE", position=POS_INSTRU_SHAPE, text_colour=WHITE)
    shape_instruction.plot(frame)
    filling_instruction=stimuli.TextLine("FILLING", position=POS_INSTRU_FILL, text_colour=WHITE)
    filling_instruction.plot(frame)
    canva=stimuli.Canvas(SIZE_ONE_OBJECT, position=pos, colour=YELLOW)
    rectangle=draw_rectangle(SIZE_FIG, BLACK, LINE_WIDTH)
    C1, C2=two_circles(RADIUS, BLACK, (0, +6), (0, -6))
    C1.plot(rectangle)
    C2.plot(rectangle)
    rectangle.plot(canva)
    canva.plot(frame)
    return frame

def rect_three(pos):
    frame=stimuli.Canvas(SIZE_FRAME, colour=BLACK)
    up_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_UP, colour=YELLOW)
    up_frame.plot(frame)
    down_frame=stimuli.Canvas(SIZE_MID_FRAME, position=POS_DOWN, colour=YELLOW)
    down_frame.plot(frame)
    shape_instruction=stimuli.TextLine("SHAPE", position=POS_INSTRU_SHAPE, text_colour=WHITE)
    shape_instruction.plot(frame)
    filling_instruction=stimuli.TextLine("FILLING", position=POS_INSTRU_FILL, text_colour=WHITE)
    filling_instruction.plot(frame)
    canva=stimuli.Canvas(SIZE_ONE_OBJECT, position=pos, colour=YELLOW)
    rectangle=draw_rectangle(SIZE_FIG, BLACK, LINE_WIDTH)
    C1, C2, C3=three_circles(RADIUS, BLACK, (0, +11), (0, 0), (0, -11))
    C1.plot(rectangle)
    C2.plot(rectangle)
    C3.plot(rectangle)
    rectangle.plot(canva)
    canva.plot(frame)
    return frame

blankscreen = stimuli.BlankScreen()

#block design
up_shape =(rect_two(POS_UP),diam_three(POS_UP),rect_three(POS_UP), diam_two(POS_UP))
block_up = design.Block()
for ic, shape in enumerate(up_shape):
    t = design.Trial()
    t.set_factor("type", ic)
    t.set_factor("is_rect", ic in [0, 2])
    t.add_stimulus(shape)
    block_up.add_trial(t, QUART_N)
block_up.shuffle_trials()

down_shape = (rect_two(POS_DOWN),diam_three(POS_DOWN), rect_three(POS_DOWN), diam_two(POS_DOWN))
block_bot=design.Block()
for ic,  shape in enumerate(down_shape):
    t = design.Trial()
    t.set_factor("type", ic)
    t.set_factor("is_two", ic in [0, 3])
    t.add_stimulus(shape)
    block_bot.add_trial(t, QUART_N)
block_bot.shuffle_trials()

block_mixed=design.Block()
for ic, shape in enumerate(up_shape):
    t = design.Trial()
    t.set_factor("type", ic)
    t.set_factor("is_rect", ic in [0, 2])
    t.add_stimulus(shape)
    block_mixed.add_trial(t, QUART_N)
for ic, shape in enumerate(down_shape):
    T=design.Trial()
    T.set_factor("type", ic)
    T.set_factor("is_two", ic in [0, 3])
    T.add_stimulus(shape)
    block_mixed.add_trial(T, QUART_N)
block_mixed.shuffle_trials()

#Feedback messages
feedback_time=stimuli.TextLine("Time is up", text_colour=WHITE, text_size=30)
feedback_wrong=stimuli.TextLine("That was the wrong key", text_colour=WHITE, text_size=30)
mapping_reminder_shape=stimuli.TextLine("Press E for rectangle and I for diamond", position=POS_FEEDBACK_SHAPE, text_colour=WHITE,text_size=30)
mapping_reminder_fill=stimuli.TextLine("Press C for two circles and N for three circles", position=POS_FEEDBACK_FILL, text_colour=WHITE, text_size=30)

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

exp.add_data_variable_names(['gender', 'type', 'key', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

#gender question
blankscreen.present()
gender_question.present()
gender, delay = exp.keyboard.wait_char([M_RESPONSE_KEY, F_RESPONSE_KEY, O_RESPONSE_KEY], duration=MAX_RESPONSE_DELAY)

blankscreen.present()

#first block
for t in block_up.trials:
    t.stimuli[0].present()
    key, rt = exp.keyboard.wait_char([RECT_RESPONSE_KEY, DIAM_RESPONSE_KEY],
                                    duration=MAX_RESPONSE_DELAY)
    if key is None:
        feedback_time.present(clear=True, update=False)
        mapping_reminder_shape.present(clear=False, update=True)
        exp.clock.wait(5000)
    else:
        is_correct_answer = (t.get_factor('is_rect') and key == RECT_RESPONSE_KEY) or \
                        (not t.get_factor('is_rect') and key ==  DIAM_RESPONSE_KEY)
        if not is_correct_answer:
            feedback_wrong.present(clear=True, update=False)
            mapping_reminder_shape.present(clear=False, update=True)
            exp.clock.wait(5000)
    exp.data.add([gender, t.get_factor('type'), key, rt])

#second block
for t in block_bot.trials:
    t.stimuli[0].present()
    key, rt = exp.keyboard.wait_char([TWO_FILL_RESPONSE_KEY, THREE_FILL_RESPONSE_KEY],
                                    duration=MAX_RESPONSE_DELAY)
    if key is None:
        feedback_time.present(clear=True, update=False)
        mapping_reminder_fill.present(clear=False, update=True)
        exp.clock.wait(5000)
    else:
        is_correct_answer = (t.get_factor('is_two') and key == TWO_FILL_RESPONSE_KEY) or \
                        (not t.get_factor('is_two') and key ==  THREE_FILL_RESPONSE_KEY)
        if not is_correct_answer:
            feedback_wrong.present(clear=True, update=False)
            mapping_reminder_fill.present(clear=False, update=True)
            exp.clock.wait(5000)
    exp.data.add([gender, t.get_factor('type'), (key, rt])

#mixing block
for t in block_mixed.trials:
    t.stimuli[0].present()
    key, rt = exp.keyboard.wait_char([TWO_FILL_RESPONSE_KEY, THREE_FILL_RESPONSE_KEY, RECT_RESPONSE_KEY, DIAM_RESPONSE_KEY], 
        duration=MAX_RESPONSE_DELAY)
    if key is None:
        feedback_time.present(clear=True, update=False)
        mapping_reminder_fill.present(clear=False, update=False)
        mapping_reminder_shape.present(clear=False, update=True)
        exp.clock.wait(5000)
    else:
        if t.stimuli[0] in up_shape:
            is_correct_anwer = (t.get_factor('is_rect') and key == RECT_RESPONSE_KEY) or\
                        (not t.get_factor('is_rect') and key == DIAM_RESPONSE_KEY)
            if not is_correct_answer:
                feedback_wrong.present(clear=True, update=False)
                mapping_reminder_shape.present(clear=False, update=True)
                exp.clock.wait(500)
        if t.stimuli[0] in down_shape:
            is_correct_answer = (t.get_factor('is_two') and key == TWO_FILL_RESPONSE_KEY) or \
                        (not t.get_factor('is_two') and key ==  THREE_FILL_RESPONSE_KEY)
            if not is_correct_answer:
                feedback_wrong.present(clear=True, update=False)
                mapping_reminder_fill.present(clear=False, update=True)
                exp.clock.wait(5000)
    exp.data.add([gender, t.get_factor('type'), key, rt])

exp.data.save("multitasking_data.csv")
