import re

text = "Карта map и объект bitmap - разные вещи"
text_2 = "еда,победа,беда"
text_3 = "Еда,победа,беду"
text_4 = "Мне сейчас 21 год , но уже скоро мне будет22(пишу без пробела)"

match = re.findall(r"\bmap\b", text)

match_2 = re.findall("еда", text_2)

match_3 = re.findall(r"[еЕ]д[ау]", text_3)

match_4 = re.findall("[0-9]", text_4)

match_4_2 = re.findall(r"\d{2}", text_4)

if __name__ == '__main__':
    print(match)
    print(match_2)
    print(match_3)
    print(match_4)
    print(match_4_2)
