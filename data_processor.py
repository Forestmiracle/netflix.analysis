import pandas as pd

def process_csv(file_path):
    # Чтение CSV файла
    df = pd.read_csv(file_path)

    # Вывод названий всех столбцов
    print("Названия столбцов в CSV файле:")
    print(df.columns)

    # Просмотр первых нескольких строк для понимания структуры данных
    print(df.head())

    # Анализ по годам выпуска
    release_years = df['release_year'].value_counts().to_dict()

    # Анализ оценок (приведение к числовым значениям)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    average_rating = df['rating'].mean()

    # Анализ продолжительности
    def parse_duration(duration):
        if isinstance(duration, float):
            return None
        if 'min' in duration:
            return int(duration.split(' ')[0])
        if 'Season' in duration:
            return None  # Пропустить сериалы
        return None

    df['duration'] = df['duration'].apply(parse_duration)
    average_duration = df['duration'].mean()

    # Анализ популярных жанров
    genres = df['listed_in'].str.get_dummies(sep=', ').sum().sort_values(ascending=False).to_dict()

    # Анализ популярных режиссеров
    directors = df['director'].dropna().value_counts().to_dict()

    # Анализ стран
    countries = df['country'].dropna().str.get_dummies(sep=', ').sum().sort_values(ascending=False).to_dict()

    # Анализ актеров
    actors = df['cast'].dropna().str.get_dummies(sep=', ').sum().sort_values(ascending=False).to_dict()

    # Преобразование данных в список списков
    release_years_list = [["Год выпуска", "Количество"]]
    release_years_list.extend([[year, count] for year, count in release_years.items()])

    genres_list = [["Жанр", "Количество"]]
    genres_list.extend([[genre, count] for genre, count in genres.items()])

    directors_list = [["Режиссер", "Количество"]]
    directors_list.extend([[director, count] for director, count in directors.items()])

    countries_list = [["Страна", "Количество"]]
    countries_list.extend([[country, count] for country, count in countries.items()])

    actors_list = [["Актер", "Количество"]]
    actors_list.extend([[actor, count] for actor, count in actors.items()])

    characteristics = {
        'Анализ по годам выпуска': release_years_list,
        'Средняя оценка': None if pd.isna(average_rating) else average_rating,
        'Средняя продолжительность (минуты)': None if pd.isna(average_duration) else average_duration,
        'Популярные жанры': genres_list,
        'Популярные режиссеры': directors_list,
        'Страны': countries_list,
        'Популярные актеры': actors_list
    }

    return characteristics

