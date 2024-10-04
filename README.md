[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f7772533198)

# AUTO FARM FOR NotPixel 🚀

![start-notpx](https://github.com/user-attachments/assets/5dbba427-4bd6-4a51-8dd2-458d215523af)

## Features

| Feature                               | Supported |
|---------------------------------------|:---------:|
| Multithreading                        |    ✔️     |
| Proxy binding to session              |    ✔️     |
| User-Agent binding to session         |    ✔️     |
| Support for tdata / pyrogram .session |    ✔️     |
| Registration in bot                   |    ✔️     |
| Auto-paint                            |    ✔️     |
| Auto-tasks                            |    ✔️     |
| Auto-claim mining rewards             |    ✔️     |
| Auto-upgrade boosters                 |    ✔️     |
| Night sleep mode                      |    ✔️     |
| Analytics game events                 |    ✔️     |

## [Settings](https://github.com/dedkuzmich/NotPixelBot/blob/master/example_config.txt/)

> :warning: **Warning:** Device type and country-specific headers can be changed under comment `# GLOBAL SETTINGS` in `bot/core/headers.py`.

| Settings                   |                           Description                            |
|----------------------------|:----------------------------------------------------------------:|
| **API_ID / API_HASH**      |       Platform data from which to run the Telegram session       |
| **SLEEP_TIME**             |    Delay (seconds) between cycles (by default - [3000, 8000])    |
| **START_DELAY**            | Delay (seconds) between sessions at start (by default - [5, 60]) |
| **AUTO_PAINT**             |                Auto painting (by default - True)                 |
| **AUTO_UPGRADE**           |            Auto upgrade boosters (by default - True)             |
| **AUTO_MINING**            |           Auto claim mining reward (by default - True)           |
| **AUTO_TASK**              |                  Auto tasks (by default - True)                  |
| **AUTO_UPGRADE_PAINT**     |          Auto upgrade paint reward (by default - True)           |
| **MAX_PAINT_LEVEL**        |           Max level for paint booster (by default - 7)           |
| **AUTO_UPGRADE_CHARGE**    |         Auto upgrade recharge speed (by default - True)          |
| **MAX_CHARGE_LEVEL**       |         Max level for recharge booster (by default - 4)          |
| **AUTO_UPGRADE_ENERGY**    |          Auto upgrade energy limit (by default - True)           |
| **MAX_ENERGY_LEVEL**       |          Max level for energy booster (by default - 3)           |
| **USE_RANDOM_COLOR**       |          Use random color from game (by default - True)          |
| **OWN_COLOR**              |  Own color if USE_RANDOM_COLOR is False (by default - #FFFFFF)   |
| **NIGHT_SLEEP**            |             Extra sleep at night (by default - True)             |
| **NIGHT_SLEEP_START_TIME** |     Time (hour) when Night mode starts (by default - [0, 2])     |
| **NIGHT_SLEEP_END_TIME**   |      Time (hour) when Night mode ends (by default - [5, 7])      |
| **REF_ID**                 |                  Reference ID for registration                   |

## Prerequisites

**Tested on Python 3.12.7**

Before you begin, make sure you have the following installed:

- Python [3.12](https://www.python.org/downloads/release/python-3120/) or [latest](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/) & [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for Python 3.12
- Dev packages (Linux only).

### Quick setup on Linux:

Install Python 3.12:

```shell
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update && sudo apt install python3.12
```

Install pip & poetry:

```shell
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
curl -sSL https://install.python-poetry.org | python3.12 -
nano ~/.bashrc
    # Add the following line to the end of "~/.bashrc"
    export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc
```

Install dev packages:

```shell
sudo apt install build-essential python3.12-dev
```

## Obtaining and setting API Keys

1. Go to [**my.telegram.org**](https://my.telegram.org/auth) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the `config.txt` file.
4. Set values in `config.txt`:

```dotenv
API_ID=123
API_HASH=abc
```

## Installation

You can download the [**repository**](https://github.com/dedkuzmich/NotPixelBot) by cloning it to your system and installing the necessary dependencies:

```shell
git clone https://github.com/dedkuzmich/NotPixelBot.git
cd NotPixelBot
cp example_config.txt config.txt
notepad/nano config.txt  # Here you set API_ID and API_HASH
poetry shell
poetry install
python main.py
```

## Usage

When you first launch the bot, create a session for it using the `Creates a session` command. It will create a `sessions` folder in which all accounts will be stored, as well as a file `accounts.json`
with configurations.

If you already have sessions, simply place them in a folder `sessions` and run the clicker. During the startup process you will be able to configure the use of a proxy for each
session. User-Agent is created automatically for each account.

Here is an example of what `accounts.json` should look like:

```shell
[
  {
    "session_name": "name_example",
    "user_agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
    "proxy": "type://user:pass:ip:port"  # "proxy": "" - if you dont use proxy
  }
]
```

## Changes Compared to the [Original Project](https://github.com/BlackJkee/NotPixelBot)

This fork introduces several improvements:

1. Migrated from `Pip` to `Poetry`.
2. Simplified project structure.
3. Implemented a header to mimic the English-language Telegram Desktop clients, specifically for use in the Portable version with `TDATA` auth.