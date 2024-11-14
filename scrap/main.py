from scrap.utils import fetch_url, parse_html, extract_data, write_to_csv
from scrap.config import load_config, load_cache, choose_source, save_cache, DATA_DIR
from pathlib import Path

def main():
    config = load_config()
    cache = load_cache()

    if cache is None:
        selection = choose_source(config)
        save_cache(selection)
    else:
        selection = cache

    url = selection['url']
    csv_file = Path(DATA_DIR).joinpath( selection['csv'] )

    html_content = fetch_url(url)
    soup = parse_html(html_content)

    structure = {
        'section_tag': 'div',
        'section_class': 'schedule-section',
        'items': [
            {'tag': 'h2', 'class': None},  # Day
            {'tag': 'span', 'class': 'time'},  # Time
            {'tag': 'span', 'class': 'activity-name'}  # Activity
        ]
    }

    data = extract_data(soup, structure)
    write_to_csv(csv_file, ["Jour", "Heure", "Activité"], data)
    print(f"Extraction completed, data saved to '{csv_file}'")

if __name__ == "__main__":
    main()