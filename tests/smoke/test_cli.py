""" tests for `pynchon` CLI
"""

from pynchon.util import testing

from pynchon.util.os import invoke  # noqa

TEST_INFO = testing.get_test_info(__file__)

TEST_CMDS = [
    # used by ..
    "pynchon cfg | jq . ",
    "python -m pynchon --version",
    # "python -m pynchon shell --help",
    # "pynchon project version --output /dev/stdout",
    # "pynchon render dot ./tests/fixtures/scripts/gen_dot.dot --in-place",
    # "pynchon render dot ./tests/fixtures/graph.dot --in-place",
    # "pynchon gen api toc --package pynchon --output docs/api/README.md",
    # "pynchon gen cli toc --output docs/cli/README.md",
    # "pynchon gen cli all --output-dir docs/cli",
    # "pynchon gen cli main --file src/pynchon/__main__.py --output-dir docs/cli"
]


def test_cmds():
    for cmd in TEST_CMDS:
        out = invoke(cmd)
        assert out.succeeded
