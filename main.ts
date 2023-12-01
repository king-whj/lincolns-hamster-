radio.onReceivedNumber(function (receivedNumber) {
    radio.sendString("thanks for micro mailing your mail")
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("hotweels time")
})
radio.onReceivedString(function (receivedString) {
    basic.showString("you recived mail")
})
input.onButtonPressed(Button.B, function () {
    CutebotPro.colorLight(CutebotProRGBLight.RGBA, 0x00ffff)
    CutebotPro.fullSpeedAhead()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.Asleep)
})
basic.showIcon(IconNames.Asleep)
radio.setGroup(77)
