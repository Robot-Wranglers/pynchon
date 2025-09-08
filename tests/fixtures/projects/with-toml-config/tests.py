""" """

project_config = project_config  # noqa


def test_is_toml_config():
    pynchon = project_config["pynchon"]
    assert pynchon["config_source"].endswith("pynchon.ini")
    assert not project_config["subproject"]
    assert pynchon["plugins"] == "fixme".split()
