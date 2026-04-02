# Yepdex Music 🇷🇺 / 🇬🇧

*[🇬🇧 English version below](#-english-version)*

Удобный инструмент для экспорта вашей музыкальной библиотеки из **Яндекс Музыки** в универсальный формат `.csv`. Создан как идеальный компаньон для **Migratify** — выгруженные файлы полностью совместимы и готовы к переносу в YouTube Music.

## 🚀 Особенности

* **Авто-установка зависимостей**: Просто запустите скрипт, он сам установит нужные библиотеки Python.
* **Умная выгрузка**: Сохраняет не только названия, но и точную длительность треков в миллисекундах (для идеального поиска в Migratify).
* **Поддержка плейлистов**: Выгружайте как "Любимые треки", так и любые свои плейлисты.
* **Запоминание токена**: Вам не придется вводить данные при каждом запуске.
* **Кроссплатформенность**: Работает на Windows, Linux и macOS.

---

## 📥 Установка и запуск

**Требования:** Установленный [Python 3.8+](https://www.python.org/downloads/).

1. Скачайте этот репозиторий.
2. Запустите лаунчер в папке проекта:
   * 🪟 Windows: `run.bat`
   * 🐧 Linux / 🍎 Mac: `run.sh`

---

## 🔑 Шаг 1: Получение токена

Для доступа к вашей библиотеке скрипту нужен токен:
1. Перейдите по ссылке (она будет в окне скрипта): [https://clck.ru/34Y6vV](https://clck.ru/34Y6vV)
2. Нажмите **"Разрешить"**.
3. Скопируйте текст из адресной строки после `access_token=`.
4. Вставьте его в терминал и нажмите **Enter**.

---

## 🏎️ Шаг 2: Экспорт

1. Выберите в меню, что именно вы хотите выгрузить (Лайки или Плейлист).
2. Скрипт создаст файл `library.csv` в папке проекта.
3. **Готово!** Просто перенесите этот файл в папку с **Migratify** и запустите миграцию.

---

## 🤝 Благодарности (Acknowledgements)

* **[yandex-music-python](https://github.com/MarshalX/yandex-music-python)** — за отличную библиотеку для работы с API Яндекса.
* **_d1naxu_** — за идею и вдохновение на создание этого скрипта!

---

# 🇬🇧 English Version

A simple and efficient tool to export your **Yandex Music** library to a universal `.csv` format. Designed as the perfect companion for **Migratify** — exported files are 100% compatible and ready for migration to YouTube Music.

## 🚀 Features

* **Auto-install dependencies**: Just run the script, and it handles Python libraries automatically.
* **Smart Export**: Saves track names, artists, and exact duration in ms (for perfect Smart Search in Migratify).
* **Playlist Support**: Export your "Liked Songs" or any custom playlist.
* **Persistent Auth**: Your token is saved securely for future sessions.
* **Cross-platform**: Native support for Windows, Linux, and macOS.

## 📥 Quick Start

**Requirement:** [Python 3.8+](https://www.python.org/downloads/) installed.

1. Download or clone this repository.
2. Launch the script:
   * 🪟 Windows: Double-click `run.bat`
   * 🐧 Linux / 🍎 Mac: Run `run.sh` in terminal

## 🔑 Step 1: Authorization
1. Follow the auth link provided in the script.
2. Click **"Allow"**.
3. Copy the token from your browser address bar (everything after `access_token=`).
4. Paste it into the script window.

## 🏎️ Step 2: Export
1. Select "Liked Songs" or a specific playlist in the menu.
2. The script will generate a `library.csv` file.
3. **Done!** Move this file to your **Migratify** folder and start your migration to YouTube Music.
