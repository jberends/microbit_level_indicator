input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (SOUND_ENABLED) {
        SOUND_ENABLED = false
    } else {
        SOUND_ENABLED = true
    }
    
})
function play_strength(strength: number) {
    
    tone = Math.abs(Math.trunc(strength) - 800)
    if (SOUND_ENABLED) {
        music.play(music.createSoundExpression(WaveShape.Sine, tone, tone, SOUND_LEVEL, SOUND_LEVEL - 50, 200, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    }
    
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    reset()
})
function reset() {
    basic.clearScreen()
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.pause(2000)
    music.play(music.createSoundExpression(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
}

let length = 0
let abs_y = 0
let abs_x = 0
let y = 0
let x = 0
let tone = 0
let SOUND_ENABLED = false
let SOUND_LEVEL = 0
let lenght : number[] = []
let MAX_CENTER = 30
let INTERVAL = 100
SOUND_LEVEL = 126
SOUND_ENABLED = true
input.setAccelerometerRange(AcceleratorRange.OneG)
reset()
basic.forever(function on_forever() {
    
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    abs_x = Math.abs(x)
    abs_y = Math.abs(y)
    length = input.acceleration(Dimension.Strength)
    length
    play_strength(length)
    if (abs_x < MAX_CENTER && abs_y < MAX_CENTER) {
        basic.showIcon(IconNames.SmallSquare, INTERVAL)
    } else if (abs_x > abs_y) {
        if (x >= 0) {
            basic.showArrow(ArrowNames.East, INTERVAL)
        } else {
            basic.showArrow(ArrowNames.West, INTERVAL)
        }
        
    } else if (y >= 0) {
        basic.showArrow(ArrowNames.South, INTERVAL)
    } else {
        basic.showArrow(ArrowNames.North, INTERVAL)
    }
    
})
