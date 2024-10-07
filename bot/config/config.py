from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = "config.txt", env_ignore_empty = True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [1200, 1800]
    START_DELAY: list[int] = [5, 20]
    AUTO_PAINT: bool = True
    AUTO_MINING: bool = True

    X3_POINTS: bool = True
    COLOR_MAP_FILE: str = "https://raw.githubusercontent.com/dedkuzmich/NotPixelBot/refs/heads/master/color_map_x3.json"

    AUTO_TASK: bool = True
    AUTO_UPGRADE: bool = True

    AUTO_UPGRADE_PAINT: bool = True
    AUTO_UPGRADE_RECHARGE: bool = True
    AUTO_UPGRADE_ENERGY: bool = True
    MAX_PAINT_LEVEL: int = 7
    MAX_RECHARGE_LEVEL: int = 4
    MAX_ENERGY_LEVEL: int = 3

    USE_RANDOM_COLOR: bool = True
    OWN_COLOR: str = "#FFFFFF"

    NIGHT_SLEEP: bool = True
    NIGHT_SLEEP_START_TIME: list[int] = [0, 2]
    NIGHT_SLEEP_END_TIME: list[int] = [4, 6]
    REF_ID: str = "f7772533198_s573984"


settings = Settings()
