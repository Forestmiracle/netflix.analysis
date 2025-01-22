from data_processor import process_csv
from data_uploader import upload_to_google_sheets

def main():
    # Путь к  CSV файлу
    csv_file_path = 'C:/Myprojects/netflix_analys_data/netflix_titles.csv'

    # Обработка CSV файла и получение характеристик
    characteristics = process_csv(csv_file_path)

    # Загрузка характеристик в Google Sheets
    upload_to_google_sheets(characteristics)

if __name__ == '__main__':
    main()
