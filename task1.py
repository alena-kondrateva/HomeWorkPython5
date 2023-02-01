# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'абв гвоаолНг праабв оогшш офаБВ'
text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))
