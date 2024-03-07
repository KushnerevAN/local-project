#Задача 1. Согласные
import re
#text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
#result = re.findall(r'\b[AEIOUYaeiouy]\w*', text)
#print('Слова на гласную: ', result)
#result_2 = re.findall(r"\b[^aAeEiIoOuUyY\W]\w*", text)
#print("Слова на любой символ, кроме гласной:", result_2)

#Задача 2. Даты
text = "Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"
result = re.findall(r"\d{2}-\d{2}-\d{4}", text)
print(result)