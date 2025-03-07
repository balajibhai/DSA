import csv
from translate import Translator

with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()

d = {}
words = content.split()
unique_words = []

for word in words:
    lowercase = word.lower()
    if lowercase in d:
        d[lowercase] += 1
    else:
        d[lowercase] = 1

for word in d:
    if d[word] == 1:
        unique_words.append(word)

translator = Translator(to_lang="fr")
translated_dict = {}
count = 0
total_unique_words = len(unique_words)
for key in d.keys():
    try:
        translated_dict[key] = translator.translate(key)
        count+=1
        print("Translating:", key)
        print("count/Total words:", count, total_unique_words)
        print(translated_dict[key])
    except Exception as e:
        translated_dict[key] = "Error translating"

with open("recordings.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Key", "Value", "Translated"])
    for key, value in d.items():
        writer.writerow([key, value, translated_dict.get(key, "N/A")])

print("Processing complete. Data written to 'recordings.csv'.")
