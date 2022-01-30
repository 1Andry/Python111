class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("секунды должны быть числом")
        self.secs = secs % self.__DAY

    def get_format_time(self):
        s = self.secs % 60  # секунды
        m = (self.secs // 60) % 60  # минуты
        h = (self.secs // 3600) % 60  # часы
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, int):
            return ValueError("Значение  должено быть целочисленным")
        s = self.secs % 60  # секунды
        m = (self.secs // 60) % 60  # минуты
        h = (self.secs // 3600) % 60  # часы
        if key == "h":
            self.secs = s + 60 * m + value * 3600
        if key == "m":
            self.secs = s + 60 * value + h * 3600
        if key == "s":
            self.secs = value + 60 * m + h * 3600

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("item должен быть строкой")
        if item == "h":
            return (self.secs // 3600) % 60
        if item == "m":
            return (self.secs // 60) % 60
        if item == "s":
            return self.secs % 60
        return "Не верный ключ"
    # @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)


c1 = Clock(80000)
print(c1.get_format_time())
c1["h"] = 11
print(c1.get_format_time())
print(c1["h"], c1["m"], c1["s"])
