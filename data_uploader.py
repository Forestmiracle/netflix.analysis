# data_uploader.py
import gspread
from google.oauth2.service_account import Credentials
from config import creds_file_path

def upload_to_google_sheets(characteristics):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file(creds_file_path, scopes=scope)
    client = gspread.authorize(creds)

    # Использование ID существующего файла вместо создания нового
    spreadsheet = client.open_by_key('138dLxLNJ6q9Cv93nSSE2jAHxSrIDqlV-WUxQNMSsFgI')
    sheet = spreadsheet.sheet1

    # Загрузка данных в Google Sheets
    characteristics_list = [['Характеристика', 'Значение']]
    for key, value in characteristics.items():
        if isinstance(value, list):  # Если значение является списком списков
            characteristics_list.append([key, ""])
            characteristics_list.extend(value)
        else:
            characteristics_list.append([key, value])

    sheet.update('A1', characteristics_list)

    print('Основные характеристики данных успешно загружены в Google Sheets.')
    print(f"Ссылка на файл: {spreadsheet.url}")






