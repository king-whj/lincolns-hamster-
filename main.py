def on_received_number(receivedNumber):
    radio.send_string("thanks for micro mailing your mail")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("hotweels time")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string("you recived mail")
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    basic.show_string("HOTWEELS")
    basic.show_leds("""
        . . . . .
        . . . . .
        # # . . .
        . . # # #
        . . # . #
        """)
    basic.show_string(" ")
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

basic.show_icon(IconNames.ASLEEP)
radio.set_group(77)