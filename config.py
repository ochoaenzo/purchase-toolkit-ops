import tomllib
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.toml"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"No se encontró {CONFIG_PATH}. Ver config.example.toml.")
    with CONFIG_PATH.open("rb") as f:
        return tomllib.load(f)
