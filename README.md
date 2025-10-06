# Surah Anki Deck Generator

Generate Anki flashcards for Quran Surahs using the [Al-Quran Cloud API](https://alquran.cloud/api). Creates clean, minimal cards with Arabic (Uthmani), transliteration, and Yusuf Ali translation.

<image-card alt="Front of Al-Fatiha card" src="screenshots/al-fatiha-front.png" ></image-card>
<image-card alt="Back of Al-Fatiha card" src="screenshots/al-fatiha-back.png" ></image-card>

## Features
- **Dynamic Cards**: Pulls Surah data (Arabic, transliteration, translation) via API.
- **Customizable Range**: Generate any Surahs (e.g., `1`, `110-114`, `1,78,112`).
- **Minimal Design**: Large Arabic text (RTL), left-aligned transliteration/translation, title-case Surah names.
- **Anki-Compatible**: Outputs CSV with fields for `RomanizedTitle`, `ChapterInfo`, `Arabic`, `Transliteration`, `Translation`.

## Prerequisites
- **Python 3.8+**: Install from [python.org](https://www.python.org/downloads/).
- **Requests Library**: `pip install requests`.
- **Anki**: Install from [apps.ankiweb.net](https://apps.ankiweb.net).

## Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/surah-anki-deck.git
   cd surah-anki-deck
   ```
2. Install dependency:
    ```bash
    pip install requests
    ```
3. Import the Anki note type:
- In Anki: File > Import > Select surah_cards.apkg.
- Creates "Surah Card" note type with templates.

## Usage
Run the script to generate cards:
    ```bash
    python3 generate_surah_cards.py "110-114"
    ```

- Outputs surahs.csv.
- Import into Anki:
    - File > Import > Select surahs.csv.
    - Set encoding to UTF-8, map fields to RomanizedTitle, ChapterInfo, Arabic, Transliteration, Translation.
    - Choose your deck (e.g., "Quran Surahs").
    - Check "Allow HTML in fields".

## Preview


## Notes
- Arabic font may require "Traditional Arabic" or "Scheherazade" installed.
- API handles Bismillah (included for all Surahs except 9).
- Tested with Surahs 1-114.

## License
MIT License (see LICENSE).

## Contributing
Issues/PRs welcome! Email: syedrayyan.dev@icloud.com


**LICENSE** (MIT, standard open-source):
```text
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.