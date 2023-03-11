import re

with open("hotline1.txt", "r", encoding='utf-8') as txt_file:
    text = txt_file.read()

phones = re.findall(r"«.* 8\(\d{3}\)\d{3}-\d{2}-\d{2}", text)

print(f'Кол-во номеров, соответствующих шаблону - {len(phones)}')

final_data = re.sub("Горячая линия", "Горячая линия Министерства образования Ростовской области", "\n".join(phones))

with open("new_hotlines.txt", "w", encoding='utf-8') as txt_file:
    txt_file.write(final_data)
