from importlib.metadata import version

import logic


def test_installed_package() -> None:
    assert logic.__name__ == "logic"
    assert version("logic") == "0.1.0"
