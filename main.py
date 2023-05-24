def on_button_pressed_a():
    global threshold
    radio.send_string("hi")
    threshold += -5
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.show_string("Hello!")
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global threshold
    threshold += 5
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    basic.show_string("Hello!")
radio.on_received_value(on_received_value)

radio.set_group(50)
OLED.init(128, 64)
threshold = 50
points = [43, 86, 21, 42]
basic.show_icon(IconNames.HEART)

def on_forever():
    if smarthome.read_noise(AnalogPin.P3) > threshold:
        smarthome.motor_fan(AnalogPin.P9, True)
        OLED.write_string_new_line("that boy finna pullup in a hulk machine")
        music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                1110,
                1110,
                255,
                255,
                200,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        OLED.clear()
        smarthome.motor_fan(AnalogPin.P9, False)
    basic.pause(10)
basic.forever(on_forever)
