input.onButtonPressed(Button.A, function () {
    threshold += -5
})
function anal3 () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 263, 1021, 255, 0, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
}
function playsound () {
    temp = randint(0, sounds.length)
    music.playSoundEffect(sounds[temp], SoundExpressionPlayMode.UntilDone)
    basic.pause(100)
}
input.onButtonPressed(Button.B, function () {
    threshold += 5
})
function anal () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 486, 129, 114, 255, 500, SoundExpressionEffect.Vibrato, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
}
function anal2 () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 486, 575, 70, 255, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
}
let temp = 0
let sounds: string[] = []
OLED.init(128, 64)
let threshold = 50
let strip = neopixel.create(DigitalPin.P12, 1, NeoPixelMode.RGBW)
sounds = [
music.createSoundEffect(WaveShape.Sawtooth, 464, 598, 255, 0, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Curve),
music.createSoundEffect(WaveShape.Noise, 508, 63, 255, 0, 500, SoundExpressionEffect.Vibrato, InterpolationCurve.Curve),
music.createSoundEffect(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear),
music.createSoundEffect(WaveShape.Triangle, 152, 1891, 255, 255, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic),
music.createSoundEffect(WaveShape.Noise, 1, 1, 255, 255, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Curve),
music.createSoundEffect(WaveShape.Square, 107, 107, 255, 255, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic)
]
basic.showIcon(IconNames.Happy)
basic.forever(function () {
    if (smarthome.ReadNoise(AnalogPin.P3) > threshold) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        smarthome.motorFan(AnalogPin.P9, true)
        OLED.writeStringNewLine("that boy finna pullup in a hulk machine")
        playsound()
    } else {
        OLED.clear()
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        smarthome.motorFan(AnalogPin.P9, false)
    }
    basic.pause(10)
})
