# toml-env-conf

`pip install toml-env-conf`

A minimal library for environment-specific (dev/prod) application configuration using TOML

Useful if you want different values in some environments (local/test/prod). e.g. all environments use 
the values base_conf.toml, but you only want some values to be different when
`env == "prod"`

As easy as 
```python
import toml_env_conf

toml_env_conf.load_as_dict(path)
# or
toml_env_conf.load_as_dataclass(
    path=path,
    data_class=MyConfigType,
    env="prod"
)
```

Where the path has the following toml files
```
├── base_conf.toml
└── env_prod.toml
```

## Convention
- There ***must*** be a file named `base_conf.toml`
- For environment overrides, the file must be called `env_[name].toml`
e.g. for an environment called `prod`, the file is called `env_prod.toml`.
For an environment called `dev`, the file is called `env_dev.toml`.


## Example

### Step 1: Create some configs

`base_conf.toml`
```toml
name = "Regular name"
hobby_name = "laundry"
is_fun = false
scores = [-10, -20]
```

`env_prod.toml`
```toml
hobby_name = "music"
is_fun = true
```

### Step 2: Load em up

`main.py`
```python
from dataclasses import dataclass
from pathlib import Path
from typing import List

import toml_env_conf


@dataclass(frozen=True)  # freeze for immutability
class MyConfigType:
    name: str
    hobby_name: str
    is_fun: bool
    scores: List[int]
   
if __name__ == "__main__":
    conf_dir_path = Path(__file__).parent.joinpath("/path/to/config")
    
    config: MyConfigType = toml_env_conf.load_as_dataclass(
        conf_dir_path, MyConfigType, env="prod"
    )
    
    print(config)
```