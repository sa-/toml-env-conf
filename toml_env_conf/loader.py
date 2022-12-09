from pathlib import Path
from typing import Union, Type, TypeVar

import toml
from mergedeep import merge


def load_as_dict(conf_path: Path, env: Union[str, None] = None) -> dict:
    """env should correspond to a toml file in the directory"""

    base_conf: dict = toml.load(str(conf_path.joinpath("base_conf.toml")))
    if env is not None:
        env_conf: dict = toml.load(str(conf_path.joinpath(f"env_{env}.toml")))
        merge(base_conf, env_conf)

    return base_conf


T = TypeVar("T")


def load_as_dataclass(
    path: Path, data_class: Type[T], env: Union[str, None] = None
) -> T:
    """Note: this doesn't support nested dataclasses"""

    conf_dict = load_as_dict(path, env)
    conf_struct = data_class(**conf_dict)
    return conf_struct
