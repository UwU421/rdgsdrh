input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    radio.sendString("hi")
    threshold += -5
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.UntilDone)
    basic.showString("Hello!")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    threshold += 5
})
radio.setGroup(23)
OLED.init(128, 64)
let threshold = 50
let points = [43, 86, 21, 42]
basic.showIcon(IconNames.Heart)
basic.forever(function on_forever() {
    if (smarthome.ReadNoise(AnalogPin.P3) > threshold) {
        smarthome.motorFan(AnalogPin.P9, true)
        OLED.writeStringNewLine("that boy finna pullup in a hulk machine")
    } else {
        OLED.clear()
        smarthome.motorFan(AnalogPin.P9, false)
    }
    
    basic.pause(10)
})
