def on_button_pressed_a():
    global threshold
    threshold += -5
input.on_button_pressed(Button.A, on_button_pressed_a)

def anal3():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
            263,
            1021,
            255,
            0,
            500,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.UNTIL_DONE)
def playsound():
    global temp
    temp = randint(0, len(sounds))
    music.play_sound_effect(sounds[temp], SoundExpressionPlayMode.UNTIL_DONE)
    basic.pause(100)

def on_button_pressed_b():
    global threshold
    threshold += 5
input.on_button_pressed(Button.B, on_button_pressed_b)

def anal():
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            486,
            129,
            114,
            255,
            500,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
def anal2():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
            486,
            575,
            70,
            255,
            500,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
temp = 0
sounds: List[str] = []
OLED.init(128, 64)
threshold = 50
strip = neopixel.create(DigitalPin.P12, 1, NeoPixelMode.RGBW)
sounds = [music.create_sound_effect(WaveShape.SAWTOOTH,
        464,
        598,
        255,
        0,
        500,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.CURVE),
    music.create_sound_effect(WaveShape.NOISE,
        508,
        63,
        255,
        0,
        500,
        SoundExpressionEffect.VIBRATO,
        InterpolationCurve.CURVE),
    music.create_sound_effect(WaveShape.SINE,
        200,
        600,
        255,
        0,
        150,
        SoundExpressionEffect.NONE,
        InterpolationCurve.LINEAR),
    music.create_sound_effect(WaveShape.TRIANGLE,
        152,
        1891,
        255,
        255,
        500,
        SoundExpressionEffect.WARBLE,
        InterpolationCurve.LOGARITHMIC),
    music.create_sound_effect(WaveShape.NOISE,
        1,
        1,
        255,
        255,
        500,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.CURVE),
    music.create_sound_effect(WaveShape.SQUARE,
        107,
        107,
        255,
        255,
        500,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.LOGARITHMIC)]
basic.show_icon(IconNames.HAPPY)

def on_forever():
    if smarthome.read_noise(AnalogPin.P3) > threshold:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        smarthome.motor_fan(AnalogPin.P9, True)
        OLED.write_string_new_line("that boy finna pullup in a hulk machine")
        playsound()
    else:
        OLED.clear()
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        smarthome.motor_fan(AnalogPin.P9, False)
    basic.pause(10)
basic.forever(on_forever)
