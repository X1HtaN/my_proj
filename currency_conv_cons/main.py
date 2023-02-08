import requests

class Converter:
    currency_list = ["RUB","EUR","GBP","JPY","KZT","KGS","AED","UAH","THB","BYN"]
    currencies = requests.get("https://currate.ru/api/?get=rates&pairs=USDRUB,USDEUR,USDGBP,USDJPY,USDKZT,USDKGS,USDAED,USDUAH,USDTHB,USDBYN&key=90111d5c23a50418a4379a6e54aefb14").json()

    @classmethod
    def calculator(cls, curr, denomination):
        curr = float(curr)
        return curr * denomination

    def get(self, value):
        message = ""
        department = "-------------------------"
        for i in range(len(self.currency_list)):
            curr_list_name = f"_{self.currency_list[i]}"
            message += f"{department}\n{self.currency_list[i]}\n{self.calculator(getattr(Converter, curr_list_name, 0), value)}\n"
        message += f"{department}\n\n####################################\n"
        return message

for i in Converter.currency_list:
    name = "_" + i
    name_currency = "USD" + i
    setattr(Converter, name, Converter.currencies["data"][f"{name_currency}"])

while True:
    request = str(input("введите кол-во USD | для выхода exit\n:/ "))
    if request == "exit": break
    print("####################################\n")
    print(Converter.get(Converter, int(request)))