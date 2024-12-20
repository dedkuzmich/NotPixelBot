[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f7772533198)

# AUTO FARM FOR NotPixel 🚀

## Changes Compared to the [Original Project](https://github.com/BlackJkee/NotPixelBot)

This fork introduces several improvements:

1. Headers to mimic the English-language [Telegram Desktop](https://desktop.telegram.org/) clients, specifically for use in the Portable version with `TDATA` auth.
2. Auto painting with a [3x PX bonus](https://github.com/vanhbakaa/Notpixel-bot).
3. Migrated from `Pip` to `Poetry` and from `Python 3.10` to `3.12`.

## Features

<details>
<summary>Expand</summary>

| Feature                               | Supported |
|---------------------------------------|:---------:|
| Multithreading                        |    ✔️     |
| Proxy binding to session              |    ✔️     |
| User-Agent binding to session         |    ✔️     |
| Support for tdata / pyrogram .session |    ✔️     |
| Auto-paint                            |    ✔️     |
| Auto-claim mining rewards             |    ✔️     |
| Auto-upgrade boosters                 |    ✔️     |
| Night sleep mode                      |    ✔️     |

</details>

## [Settings](https://github.com/dedkuzmich/NotPixelBot/blob/master/example_config.txt)

> :warning: **Warning:** Device type and country-specific headers can be changed under comment `# GLOBAL SETTINGS` in `bot/core/headers.py`.

| Settings                   |                           Description                            |
|----------------------------|:----------------------------------------------------------------:|
| **API_ID / API_HASH**      |       Platform data from which to run the Telegram session       |
| **SLEEP_TIME**             |    Delay (seconds) between cycles (by default - [3600, 5000])    |
| **START_DELAY**            | Delay (seconds) between sessions at start (by default - [5, 30]) |
| **X3_POINTS**              |     Auto paint specific pixel to get 3x px (default - True)      |
| **AUTO_PAINT**             |                Auto painting (by default - True)                 |
| **AUTO_MINING**            |           Auto claim mining reward (by default - True)           |
| **AUTO_UPGRADE**           |            Auto upgrade boosters (by default - True)             |
| **AUTO_UPGRADE_PAINT**     |          Auto upgrade paint reward (by default - True)           |
| **AUTO_UPGRADE_RECHARGE**  |         Auto upgrade recharge speed (by default - True)          |
| **AUTO_UPGRADE_ENERGY**    |          Auto upgrade energy limit (by default - True)           |
| **MAX_PAINT_LEVEL**        |           Max level for paint booster (by default - 7)           |
| **MAX_RECHARGE_LEVEL**     |         Max level for recharge booster (by default - 11)         |
| **MAX_ENERGY_LEVEL**       |          Max level for energy booster (by default - 6)           |
| **NIGHT_SLEEP**            |             Extra sleep at night (by default - True)             |
| **NIGHT_SLEEP_START_TIME** |     Time (hour) when Night mode starts (by default - [0, 2])     |
| **NIGHT_SLEEP_END_TIME**   |      Time (hour) when Night mode ends (by default - [4, 6])      |

## Prerequisites

**Tested on Python 3.12.7, Windows 10 x64, Ubuntu 22.04 x64**

Before you begin, make sure you have the following installed:

- Python [3.12](https://www.python.org/downloads/release/python-3120/) or [latest](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/) & [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for Python 3.12
- Dev packages (Linux only).

### Quick setup on Ubuntu 22.04 x64:

<details>
<summary>Expand</summary>

Install `Pyenv`:

```shell
curl https://pyenv.run | bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && echo 'eval "$(pyenv init -)"' >> ~/.bashrc && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile && echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile && echo 'eval "$(pyenv init -)"' >> ~/.profile && source ~/.bashrc
sudo apt install -y make build-essential screen libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```

Install `Python 3.12` (`Pip` is built-in):

```shell
pyenv install 3.12 # Process takes ~5 min on AWS t3.micro
pyenv global 3.12.7
```

Install `Poetry`:

```shell
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.prefer-active-python true
```

</details>

## Obtaining API Keys

1. Go to [**my.telegram.org**](https://my.telegram.org/auth) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new app.
3. Save the values of `API_ID` and `API_HASH` in `config.txt`.

```dotenv
API_ID=123
API_HASH=abc
```

## Installation

Clone [**repository**](https://github.com/dedkuzmich/NotPixelBot)  and install the dependencies:

```shell
git clone https://github.com/dedkuzmich/NotPixelBot.git && cd NotPixelBot
cp example_config.txt config.txt
notepad/nano config.txt  # Here you set API_ID and API_HASH
poetry shell
poetry install
python main.py # Test run
deactivate
```

## Usage

When you first launch the bot, create a session for it using the `2. Create session` command.
It will create a `sessions` folder in which all accounts will be stored, as well as a file `accounts.json`
with configurations.

If you already have sessions, simply place them in a folder `sessions` and run the `1. Run clicker`.
During the startup process you can set a proxy for each session (`HTTP`, `SOCKS4`, `SOCKS5` proxy protocols are supported).

Color [map](https://github.com/dedkuzmich/NotPixelBot/blob/master/bot/utils/colors.py) for 3x PX bonus
is updated daily with the latest values from [this](https://github.com/vanhbakaa/notpixel-3x-points) repo.

### Linux only

Linux allow you to work with sessions via `screen`.
Create & detach a session:

```shell
deactivate # Ensure you are outside poetry venv
screen -S npx
source $(poetry env info --path)/bin/activate
python main.py
# Detach session with Ctrl + A + D
```

Attach to the session:

```shell
screen -ls
screen -r npx
deactivate
exit # If you want to kill session completely
```

## Examples

Example of `accounts.json`:

```shell
[
  { # Pattern
    "session_name": "name_example_1",
    "user_agent": "Randomly generated User-Agent",
    "proxy": "type://user:pass:ip:port"  # "proxy": "" - if you dont use proxy
  }
  { # Realistic example
    "session_name": "session_2",
    "user_agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.5821.163 Mobile Safari/537.36",
    "proxy": "socks5://lamer:hacker:13.37.13.37:1337"
  }
]
```