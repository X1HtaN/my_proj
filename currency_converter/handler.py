import requests
from decimal import Decimal

class Converter:
    currencies = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    __USD = currencies["Valute"]["USD"]["Value"] #Доллар
    __EUR = currencies["Valute"]["EUR"]["Value"] #Евро
    __JPY = currencies["Valute"]["JPY"]["Value"] #Японсий йен
    __KZT = currencies["Valute"]["KZT"]["Value"] #Казахстанский тенге
    __CNY = currencies["Valute"]["CNY"]["Value"] #Китайский юань
    __UAH = currencies["Valute"]["UAH"]["Value"] #Украинская гривна
    __PLN = currencies["Valute"]["PLN"]["Value"] #Польский злотый

    @classmethod
    def limiter(cls, rub, item):
        rub = float(rub)
        conv_item = rub / item
        conv_item = Decimal(conv_item)
        conv_item = conv_item.quantize(Decimal("1.00"))
        conv_item = float(conv_item)
        return conv_item

    @classmethod
    def convert(cls, rub):
        conv_USD = cls.limiter(rub, cls.__USD)
        conv_EUR = cls.limiter(rub, cls.__EUR)
        conv_JPY = cls.limiter(rub, cls.__JPY)
        conv_KZT = cls.limiter(rub, cls.__KZT)
        conv_CNY = cls.limiter(rub, cls.__CNY)
        conv_UAH = cls.limiter(rub, cls.__UAH)
        conv_PLN = cls.limiter(rub, cls.__PLN)
        return f"| {conv_USD} USD | {conv_EUR} EUR | {conv_JPY} JPY | {conv_KZT} KZT | {conv_CNY} CNY | {conv_UAH} UAH | {conv_PLN} PLN |"

print(Converter.convert(20.5))