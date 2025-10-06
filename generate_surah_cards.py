import requests
import csv
import sys

def parse_surah_input(input_str):
    """Parse input like '110-114' or '1,78,110-114' into sorted unique list of ints (1-114)."""
    numbers = set()
    parts = input_str.split(',')
    for part in parts:
        part = part.strip()
        if '-' in part:
            start, end = map(int, part.split('-'))
            for n in range(start, end + 1):
                if 1 <= n <= 114:
                    numbers.add(n)
        else:
            n = int(part)
            if 1 <= n <= 114:
                numbers.add(n)
    return sorted(list(numbers))

def fetch_surah_data(surah_num):
    """Fetch Surah data from Al-Quran Cloud API using multi-edition endpoint."""
    url = f"https://api.alquran.cloud/v1/surah/{surah_num}/editions/quran-uthmani,en.yusufali,en.transliteration"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching Surah {surah_num}: {response.status_code}")
        return None
    
    api_data = response.json()
    if 'data' not in api_data:
        print(f"Invalid response for Surah {surah_num}")
        return None
    
    editions = api_data['data']  # List of 3 editions: [arabic, translation, transliteration]
    if len(editions) != 3:
        print(f"Unexpected editions count for Surah {surah_num}: {len(editions)}")
        return None
    
    # Metadata from first edition (same across)
    surah_data = editions[0]
    english_name = surah_data['englishName']
    meaning = surah_data['englishNameTranslation']
    
    arabic_ayahs = editions[0]['ayahs']
    trans_ayahs = editions[1]['ayahs']
    translit_ayahs = editions[2]['ayahs']
    
    arabic_lines = [ayah['text'] for ayah in arabic_ayahs]
    translit_lines = [ayah['text'] for ayah in translit_ayahs]
    
    # Translation with numbering; add Bismillah for most surahs
    translation_lines = []
    bismillah_added = False
    for i, ayah in enumerate(trans_ayahs):
        verse_num = arabic_ayahs[i]['numberInSurah']
        trans_text = ayah['text'].strip()
        
        if verse_num == 1 and surah_num != 9:  # Add Bismillah except for Surah 9
            translation_lines.append("1. In the name of Allah, Most Gracious, Most Merciful.")
            # Adjust verse num for first actual verse
            next_num = 2
            translation_lines.append(f"{next_num}. {trans_text}")
            bismillah_added = True
        else:
            translation_lines.append(f"{verse_num}. {trans_text}")
    
    # Add Bismillah to transliteration if not present (check first line)
    if surah_num != 9 and not translit_lines[0].startswith("Bismillaahir"):
        translit_lines.insert(0, "Bismillaahir Rahmaanir Raheem")
    
    arabic = '<br>'.join(arabic_lines)
    transliteration = '<br>'.join(translit_lines)
    translation = '<br>'.join(translation_lines)
    
    return {
        'RomanizedTitle': english_name,
        'ChapterInfo': f"Chapter {surah_num}, {meaning}",
        'Arabic': arabic,
        'Transliteration': transliteration,
        'Translation': translation
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_surah_cards.py '1,78,110-114'")
        sys.exit(1)
    
    input_str = sys.argv[1]
    surah_numbers = parse_surah_input(input_str)
    if not surah_numbers:
        print("No valid Surah numbers provided (must be 1-114).")
        sys.exit(1)
    
    print(f"Generating cards for Surahs: {', '.join(map(str, surah_numbers))}")
    
    with open('surahs.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['RomanizedTitle', 'ChapterInfo', 'Arabic', 'Transliteration', 'Translation'])
        writer.writeheader()
        
        for num in surah_numbers:
            data = fetch_surah_data(num)
            if data:
                writer.writerow(data)
                print(f"Added Surah {num}: {data['RomanizedTitle']}")
    
    print("CSV generated: surahs.csv. Import into Anki!")

if __name__ == "__main__":
    main()