class TheLamp:
    def __init__(self):
        self.is_on = False
        self.color = (0, 0, 0)
        self.tlv_api = {
            b'\x12': self.turn_on,
            b'\x13': self.turn_off,
            b'\x20': self.set_color,
        }

    def api(self, method, value=b''):
        if method in self.tlv_api:
            self.tlv_api[method](value)
            self.draw()
        else:
            pass

    def turn_on(self, value=None):
        self.is_on = True
        self.color = (255, 255, 255)

    def turn_off(self, value=None):
        self.is_on = False
        self.color = (0, 0, 0)

    def set_color(self, value=b'\xff\xff\xff'):
        if len(value) == 3:
            self.color = tuple(bytearray(value))

    def draw(self):
        black = '\33[40m'
        red   = '\33[41m'
        green = '\33[42m'
        blue  = '\33[44m'
        end   = '\33[0m'
        if self.is_on:
            print("{}{:3d}{}{:3d}{}{:3d}{}".format(
                red, self.color[0], green, self.color[1], blue, self.color[2], end
            ))
        else:
            print(black + '  O F F  ' + end)

