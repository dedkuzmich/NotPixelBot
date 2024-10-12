from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = "config.txt", env_ignore_empty = True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [3600, 5000]
    START_DELAY: list[int] = [5, 30]
    X3_POINTS: bool = True
    AUTO_PAINT: bool = True
    AUTO_MINING: bool = True
    AUTO_UPGRADE: bool = True

    AUTO_UPGRADE_PAINT: bool = True
    AUTO_UPGRADE_RECHARGE: bool = True
    AUTO_UPGRADE_ENERGY: bool = True
    MAX_PAINT_LEVEL: int = 7
    MAX_RECHARGE_LEVEL: int = 11
    MAX_ENERGY_LEVEL: int = 6

    NIGHT_SLEEP: bool = True
    NIGHT_SLEEP_START_TIME: list[int] = [0, 2]
    NIGHT_SLEEP_END_TIME: list[int] = [4, 6]

    # Legacy
    AUTO_TASK: bool = False
    USE_RANDOM_COLOR: bool = True
    OWN_COLOR: str = "#FFFFFF"
    REF_ID: str = "f7772533198_s573984"


settings = Settings()
