import requests
import re
import csv
from collections import defaultdict

WIKI_BASE = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

def fetch_main_categories():
    main_text = requests.get(WIKI_BASE).text
    return sorted(set(re.findall(r'<a[^>]*>([А-Яа-яЁё]{2})</a>', main_text)))

def fetch_animals_from_category(cat):
    url = f"{WIKI_BASE}?from={cat}"
    try:
        text = requests.get(url).text
    except:
        return []
    animals = re.findall(
        fr'<a\s+href="[^"]*"\s+title="({re.escape(cat)}[^"]*)"[^>]*>({re.escape(cat)}.*?)</a>',
        text
    )
    return animals

def count_animals_by_letter(categories):
    animal_counts = defaultdict(int)
    for cat in categories:
        animals = fetch_animals_from_category(cat)
        for animal in animals:
            first_letter = animal[0][0].upper()
            animal_counts[first_letter] += 1
    return animal_counts

def write_to_csv(animal_counts, filename='beasts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Буква', 'Количество животных'])
        for letter in sorted(animal_counts.keys()):
            writer.writerow([letter, animal_counts[letter]])

def main():
    categories = fetch_main_categories()
    animal_counts = count_animals_by_letter(categories)
    write_to_csv(animal_counts)
    print("Результат сохранён в beasts.csv")

if __name__ == "__main__":
    main()
