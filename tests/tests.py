from dataclasses import dataclass
from pathlib import Path
from typing import List

import toml_env_conf


@dataclass(frozen=True)
class TestConf:
    name: str
    hobby_name: str
    is_fun: bool
    scores: List[int]


def test_load_as_dataclass__no_override():
    config = toml_env_conf.load_as_dataclass(
        Path(__file__).parent.joinpath("test_conf"), TestConf
    )

    assert config.name == "Regular name"
    assert config.hobby_name == "laundry"
    assert config.is_fun is False
    assert config.scores == [-10, -20]


def test_load_as_dict__no_override():
    config = toml_env_conf.load_as_dict(Path(__file__).parent.joinpath("test_conf"))

    assert config["name"] == "Regular name"
    assert config["hobby_name"] == "laundry"
    assert config["is_fun"] is False
    assert config["scores"] == [-10, -20]


def test_load_as_dataclass__env_prod():
    config = toml_env_conf.load_as_dataclass(
        Path(__file__).parent.joinpath("test_conf"), TestConf, env="prod"
    )

    assert config.name == "Regular name"
    assert config.hobby_name == "music"
    assert config.is_fun is True
    assert config.scores == [-10, -20]


def test_load_as_dict__env_prod():
    config = toml_env_conf.load_as_dict(
        Path(__file__).parent.joinpath("test_conf"), env="prod"
    )

    assert config["name"] == "Regular name"
    assert config["hobby_name"] == "music"
    assert config["is_fun"] is True
    assert config["scores"] == [-10, -20]
