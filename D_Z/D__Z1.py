class Convert_t:
    count = 0

    @staticmethod
    def to_fahrenheit(value):
        Convert_t.count += 1
        print(f"Конвертация в Фарингейт: {round(((value - 32) / 1.8), 2)}")
        print("Количество подсчетов температуры", Convert_t.count)

    @staticmethod
    def to_celsius(value):
        Convert_t.count += 1
        print(f"Конвертация в Цельсий: {round((value * 1.8 + 32), 2)}")
        print("Количество подсчетов температуры", Convert_t.count)


Convert_t.to_celsius(15)
Convert_t.to_fahrenheit(59)
Convert_t.to_fahrenheit(211)
Convert_t.to_celsius(11)
