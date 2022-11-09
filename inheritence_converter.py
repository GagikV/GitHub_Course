class TempMixin:
    '''Conv temp from metric to imperial and reverse'''

    def f_to_c(self, f):
        return (f - 32) / 1.8

    def c_to_f(self, c):
        return (c * 1.8) + 32


class DistanceMixin:
    '''Conv distance'''

    def m_to_km(self, miles):
        return miles * 1.60934

    def km_to_m(self, km):
        return km * 0.6213712


class DigitalStorageMixin:
    """Convert DigitalStorage from mb to gb and reverse"""

    def gb_to_mb(self, gb):
        return gb * 1000

    def mb_to_gb(self, mb):
        return mb / 1000

class Weather(TempMixin, DistanceMixin):
    '''Weather'''

    def __init__(self, celsius, kmph):
        '''Initialise data'''
        self._celsius = celsius
        self._kmph = kmph

    def display(self, metric=True):
        if metric:
            temp = self._celsius
            wind = self._kmph
        else:
            temp = self.c_to_f(self._celsius)
            wind = self.km_to_m(self._kmph)

        print(f'Temp: {temp}, Wind Speed: {wind}')
        print('---- END OF WEATHER ----')


london = Weather(12, 7)
london.display()
london.display(metric=False)


class HardDrive(TempMixin, DigitalStorageMixin):

    def __init__(self, space, celsius):
        self._space = space
        self._celcius = celsius

    def status(self, metric=True):
        if metric:
            temp = self._celcius
            degrees = 'C'
        else:
            temp = self.c_to_f(self._celcius)
            degrees = 'F'
        space = self.mb_to_gb(self._space)

        print(f'Space: {space}Gb, Temp: {temp} {degrees}')
        print('_____ End of HARD DRIVE STATUS _____')

hd = HardDrive(800000, 22)
hd.status()
hd.status(metric=False)
