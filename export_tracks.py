# === Auto-install dependencies ===
import sys
import subprocess
import os
import time

REQUIRED = ["yandex-music", "colorama", "tqdm", "requests"]

def _ensure_deps():
    import importlib
    missing = []
    for pkg in REQUIRED:
        mod_name = pkg.replace("-", "_")
        try:
            importlib.import_module(mod_name)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"[Yepdex] Missing packages: {', '.join(missing)}. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
        print("[Yepdex] Done! Restarting...\n")
        os.execv(sys.executable, [sys.executable] + sys.argv)

_ensure_deps()
# === End auto-install ===

import csv
from typing import List
from yandex_music import Client, Track
from colorama import init, Fore, Style
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(BASE_DIR, "token.txt")

LOGO = fr"""{Fore.RED}{Style.BRIGHT}
 __     __              _              __  __           _      
 \ \   / /             | |            |  \/  |         (_)     
  \ \_/ /__ _ __   __| | _____  __    | \  / |_   _ ___ _  ___ 
   \   / _ \ '_ \ / _` |/ _ \ \/ /    | |\/| | | | / __| |/ __|
    | |  __/ |_) | (_| |  __/>  <     | |  | | |_| \__ \ | (__ 
    |_|\___| .__/ \__,_|\___/_/\_\    |_|  |_|\__,_|___/_|\___|
           |_|                                                 
"""

LANG_DATA = {
    "en": {
        "welcome": f"{Fore.YELLOW}>>> Yandex Music to CSV Exporter <<<",
        "compat": f"{Fore.CYAN}(Formatted for Migratify Compatibility)",
        "auth_title": "YANDEX MUSIC AUTHORIZATION",
        "need_token": "To work, the script needs your personal Yandex token.",
        "how_to_get": "Method 1: Open https://music.yandex.ru/api/v2.1/token and copy 'token'.",
        "step1": "Method 2: If Method 1 fails, go to music.yandex.ru -> F12 -> Application -> Cookies.",
        "step2": "Find 'Session_id' and copy its value.",
        "step3": "Paste either Token or Session_id below.",
        "enter_token": "Paste Token or Session_id: ",
        "token_err": "Error: You didn't enter a token. Script cannot continue.",
        "token_saved": "Token saved to '{0}' for future runs.",
        "auth_err": "Authorization Error: {0}\nToken might be invalid or expired.",
        "profile": "[Profile]: {0} (@{1})",
        "choose_action": "Choose action:",
        "action_likes": "1. Export all LIKED tracks",
        "action_playlist": "2. Choose one of your PLAYLISTS",
        "action_exit": "0. Exit",
        "choice_prompt": "Your choice: ",
        "loading": "Loading track data ({0} pcs.)...",
        "done": "Done! File saved: {0}",
        "tip": "Tip: Place this file in your Migratify folder and run migrate.py!",
        "pl_empty": "You have no playlists.",
        "pl_list": "Your playlists:",
        "pl_select": "Select number (1-{0}): ",
        "invalid_num": "Invalid number.",
        "enter_num": "You must enter a number.",
        "retry": "Do another export? (y/n): "
    },
    "ru": {
        "welcome": f"{Fore.YELLOW}>>> Yandex Music to CSV Exporter <<<",
        "compat": f"{Fore.CYAN}(Оптимизировано для работы с Migratify)",
        "auth_title": "АВТОРИЗАЦИЯ ЯНДЕКС МУЗЫКИ",
        "need_token": "Для работы скрипта нужен ваш персональный токен.",
        "how_to_get": "Способ 1: Открой https://music.yandex.ru/api/v2.1/token и скопируй 'token'.",
        "step1": "Способ 2: Если первый не сработал, зайди на music.yandex.ru -> F12 -> Application -> Cookies.",
        "step2": "Найди 'Session_id' и скопируй его значение.",
        "step3": "Вставь сюда либо Токен, либо Session_id.",
        "enter_token": "Вставьте Токен или Session_id: ",
        "token_err": "Ошибка: Вы не ввели токен. Работа скрипта невозможна.",
        "token_saved": "Токен сохранен в '{0}' для будущих запусков.",
        "auth_err": "Ошибка авторизации: {0}\nСкорее всего, токен неверный или устарел.",
        "profile": "[Профиль]: {0} (@{1})",
        "choose_action": "Выберите действие:",
        "action_likes": "1. Выгрузить все ЛЮБИМЫЕ треки",
        "action_playlist": "2. Выбрать один из ваших ПЛЕЙЛИСТОВ",
        "action_exit": "0. Выход",
        "choice_prompt": "Ваш выбор: ",
        "loading": "Загружаем данные о треках ({0} шт.)...",
        "done": "Готово! Файл сохранен: {0}",
        "tip": "Совет: Положите этот файл в папку с Migratify для переноса в YouTube Music!",
        "pl_empty": "У вас нет плейлистов.",
        "pl_list": "Ваши плейлисты:",
        "pl_select": "Выберите номер (1-{0}): ",
        "invalid_num": "Неверный номер.",
        "enter_num": "Нужно ввести число.",
        "retry": "Сделать еще одну выгрузку? (д/н): "
    }
}

def get_language():
    """Select language with animated logo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in LOGO.split("\n"):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.001)
        print()
    
    print("\nChoose your language / Выберите язык:")
    print("1. English")
    print("2. Русский")
    choice = input("> ").strip()
    return 'ru' if choice == '2' else 'en'

def get_token(t) -> str:
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            token = f.read().strip()
            if token:
                return token

    print("\n" + "=" * 45)
    print(f"      {Fore.YELLOW}{t['auth_title']}{Style.RESET_ALL}")
    print("=" * 45)
    print(f"\n{t['need_token']}")
    print(t['how_to_get'])
    print(t['step1'])
    print(t['step2'])
    print(t['step3'])
    print("\n" + "-" * 45)

    token = input(f"{Fore.WHITE}{t['enter_token']}{Style.RESET_ALL}").strip()

    if not token:
        print(f"\n{Fore.RED}[!] {t['token_err']}")
        sys.exit(1)

    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        f.write(token)

    print(f"\n{Fore.GREEN}[+] {t['token_saved'].format(os.path.basename(TOKEN_FILE))}")
    return token

def get_client(t) -> Client:
    import requests
    token = get_token(t)
    
    # Try using as token first
    try:
        # Clean token
        clean_token = token.replace('OAuth ', '').strip().strip('"').strip("'")
        if ":" in clean_token and len(clean_token) > 50: # Likely a Session_id
            print(f"{Fore.CYAN}[Wait] Attempting to exchange Session_id for Token...")
            r = requests.get('https://music.yandex.ru/api/v2.1/token', cookies={'Session_id': clean_token})
            if r.status_code == 200:
                clean_token = r.json().get('token', clean_token)
            
        client = Client(clean_token).init()
        # Save working token if it was transformed from Session_id
        if clean_token != token:
             with open(TOKEN_FILE, "w", encoding="utf-8") as f:
                f.write(clean_token)
        return client
    except Exception as e:
        print(f"\n{Fore.RED}[!] {t['auth_err'].format(e)}")
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
        print(f"\n{Fore.WHITE}Press Enter to exit...{Style.RESET_ALL}")
        input()
        sys.exit(1)

def format_track(track: Track) -> List[str]:
    title = track.title
    if track.version:
        title = f"{title} ({track.version})"
    artists = ", ".join([artist.name for artist in track.artists if artist.name])
    album = track.albums[0].title if track.albums else "Single"
    duration_ms = track.duration_ms
    return [title, artists, album, duration_ms]

def save_to_csv(tracks: List[Track], output_file: str, t):
    if not tracks:
        print(f"{Fore.RED}{t['invalid_num']}")
        return

    if output_file == "yandex_likes.csv" or output_file == "library.csv":
        output_file = "library.csv"

    clean_filename = "".join([c for c in output_file if c.isalnum() or c in (' ', '.', '_')]).strip()
    if not clean_filename.endswith(".csv"):
        clean_filename += ".csv"

    print(f"\n{Fore.CYAN}{t['loading'].format(len(tracks))}")

    try:
        full_tracks = tracks.fetch_tracks() if hasattr(tracks, 'fetch_tracks') else tracks
    except Exception:
        full_tracks = tracks

    with open(clean_filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Track Name', 'Artist Name(s)', 'Album', 'Track Duration (ms)'])

        for track in tqdm(full_tracks, desc="Export", colour="yellow"):
            if track:
                writer.writerow(format_track(track))

    print(f"\n{Fore.GREEN}✅ {t['done'].format(clean_filename)}")
    print(f"{Fore.YELLOW}💡 {t['tip']}")

def export_menu(client: Client, t):
    # Short logo for repetition
    print(LOGO)
    print(t['welcome'])
    print(t['compat'])
    
    try:
        user = client.account_status().account
        print(f"\n{t['profile'].format(Fore.YELLOW + user.display_name + Style.RESET_ALL, user.login)}")
    except Exception:
        pass

    print(f"\n{Style.BRIGHT}{t['choose_action']}")
    print(f"{t['action_likes']}")
    print(f"{t['action_playlist']}")
    print(f"{t['action_exit']}")

    choice = input(f"\n{Fore.WHITE}{t['choice_prompt']}{Style.RESET_ALL}").strip()

    if choice == "1":
        likes = client.users_likes_tracks()
        save_to_csv(likes.tracks, "library.csv", t)

    elif choice == "2":
        playlists = client.users_playlists_list()
        if not playlists:
            print(f"{Fore.RED}{t['pl_empty']}")
            return

        print(f"\n{Fore.CYAN}{t['pl_list']}")
        for idx, pl in enumerate(playlists, 1):
            print(f"{idx}. {pl.title} ({pl.track_count} tracks)")

        try:
            pl_idx = int(input(f"\n{t['pl_select'].format(len(playlists))}")) - 1
            if 0 <= pl_idx < len(playlists):
                selected_pl = playlists[pl_idx]
                full_pl = selected_pl.fetch_tracks()
                tracks = [pt.track for pt in full_pl]
                save_to_csv(tracks, f"library_{selected_pl.title}.csv", t)
            else:
                print(f"{Fore.RED}{t['invalid_num']}")
        except ValueError:
            print(f"{Fore.RED}{t['enter_num']}")

    elif choice == "0":
        sys.exit(0)

if __name__ == "__main__":
    lang_code = get_language()
    t = LANG_DATA[lang_code]
    
    client = get_client(t)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        export_menu(client, t)
        
        retry_prompt = t['retry']
        if input(f"\n{retry_prompt}").lower() not in ('д', 'да', 'y', 'yes'):
            break
