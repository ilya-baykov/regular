import re

text = "Карта map и объект bitmap - разные вещи"
text_2 = "еда,победа,беда"
text_3 = "Еда,победа,беду"

match = re.findall(r"\bmap\b", text)

match_2 = re.findall("еда", text_2)

match_3 = re.findall(r"[еЕ]д[ау]", text_3)

if __name__ == '__main__':
    print(match)
    print(match_2)
    print(match_3)
