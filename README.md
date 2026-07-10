# Yepdex Music

Небольшой Python-экспортёр библиотеки **Яндекс Музыки** в CSV.

Файл из «Любимых треков» сохраняется как `library.csv` и сразу подходит для [Migratify](https://github.com/NoxbaneSudo/Migratify): можно перенести библиотеку в YouTube Music.

[English version](#english-version)

## Что умеет

- экспортировать «Любимые треки»;
- экспортировать любой ваш плейлист;
- сохранять название, исполнителя, альбом и длительность трека;
- автоматически устанавливать нужные Python-пакеты при первом запуске;
- работать на Windows, Linux и macOS.

## Запуск

Нужен [Python 3.8+](https://www.python.org/downloads/).

1. Скачайте или клонируйте репозиторий.
2. Запустите файл для своей системы:

| Система | Запуск |
| --- | --- |
| Windows | Дважды кликните `run.bat` |
| Linux / macOS | В терминале выполните `chmod +x run.sh && ./run.sh` |

При первом запуске скрипт сам установит зависимости.

## Получите токен Яндекса

Токен нужен только для доступа к вашей библиотеке.

1. Откройте [страницу авторизации Яндекса](https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d).
2. Нажмите **«Разрешить»**.
3. Вас может открыть на пустой странице или странице с ошибкой — это нормально.
4. В адресной строке скопируйте текст после `access_token=` и до первого `&`.
5. При первом запуске вставьте токен в окно скрипта.

Токен сохраняется локально в `token.txt`, чтобы не вводить его каждый раз. Не передавайте этот файл другим людям. Он уже добавлен в `.gitignore`.

## Экспорт

После авторизации выберите в меню:

- `1` — экспорт «Любимых треков» в `library.csv`;
- `2` — выберите свой плейлист; файл будет создан с его названием.

CSV содержит столбцы `Track Name`, `Artist Name(s)`, `Album` и `Track Duration (ms)`.

## Перенос в YouTube Music

Для «Любимых треков» ничего переименовывать не нужно: скопируйте `library.csv` в папку [Migratify](https://github.com/NoxbaneSudo/Migratify) и запустите миграцию по его инструкции.

## Благодарности

- [yandex-music-python](https://github.com/MarshalX/yandex-music-python) — библиотека для API Яндекс Музыки.
- _d1naxu_ — идея и вдохновение.

---

# English version

Yepdex Music is a small Python tool that exports your **Yandex Music** library to CSV.

Exports of liked tracks are saved as `library.csv`, ready to use with [Migratify](https://github.com/NoxbaneSudo/Migratify) for a YouTube Music migration.

## Features

- Export liked tracks or any of your playlists.
- Save track title, artist, album, and duration.
- Install required Python packages automatically on the first run.
- Run on Windows, Linux, and macOS.

## Run it

You need [Python 3.8+](https://www.python.org/downloads/).

| System | How to run |
| --- | --- |
| Windows | Double-click `run.bat` |
| Linux / macOS | Run `chmod +x run.sh && ./run.sh` in a terminal |

## Get a Yandex token

1. Open the [Yandex authorization page](https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d).
2. Click **Allow**.
3. A blank or error page is expected.
4. Copy the value after `access_token=` and before the first `&` in the address bar.
5. Paste it into the script when prompted.

The token is saved locally to `token.txt`. Keep it private; the file is excluded from Git.

## Export and migrate

Choose `1` to export liked tracks to `library.csv`, or `2` to export one playlist.

To migrate liked tracks, copy `library.csv` into the [Migratify](https://github.com/NoxbaneSudo/Migratify) folder and follow its instructions.
