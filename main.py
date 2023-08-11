def on_button_pressed_a():
    global SOUND_ENABLED
    if SOUND_ENABLED:
        SOUND_ENABLED = False
    else:
        SOUND_ENABLED = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def play_strength(strength: number):
    global tone
    tone = int(strength) - 800
    if SOUND_ENABLED:
        music.play(music.create_sound_expression(WaveShape.SINE,
                tone,
                tone,
                SOUND_LEVEL,
                SOUND_LEVEL - 50,
                200,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.IN_BACKGROUND)

def on_button_pressed_ab():
    reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def reset():
    basic.clear_screen()
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(2000)
    music.play(music.create_sound_expression(WaveShape.SINE,
            200,
            600,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
length = 0
abs_y = 0
abs_x = 0
y = 0
x = 0
tone = 0
SOUND_ENABLED = False
SOUND_LEVEL = 0
lenght: List[number] = []
MAX_CENTER = 30
INTERVAL = 100
SOUND_LEVEL = 126
SOUND_ENABLED = True
input.set_accelerometer_range(AcceleratorRange.ONE_G)
reset()

def on_forever():
    global x, y, abs_x, abs_y, length
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    abs_x = abs(x)
    abs_y = abs(y)
    length = input.acceleration(Dimension.STRENGTH)
    length = float(math.sqrt(x**2 + y**2))
    play_strength(length)
    if abs_x < MAX_CENTER and abs_y < MAX_CENTER:
        basic.show_icon(IconNames.SMALL_SQUARE, INTERVAL)
    elif abs_x > abs_y:
        if x >= 0:
            basic.show_arrow(ArrowNames.EAST, INTERVAL)
        else:
            basic.show_arrow(ArrowNames.WEST, INTERVAL)
    elif y >= 0:
        basic.show_arrow(ArrowNames.SOUTH, INTERVAL)
    else:
        basic.show_arrow(ArrowNames.NORTH, INTERVAL)
basic.forever(on_forever)
