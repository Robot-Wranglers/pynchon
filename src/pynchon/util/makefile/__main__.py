"""pynchon.util.makefile CLI"""

from pynchon.cli import common

import shimport

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)
entry = common.entry_for(__name__)


(
    shimport.wrapper("pynchon.util.makefile")
    .prune(
        exclude_private=True,
        filter_module_origin=True,
        filter_instances=typing.FunctionType,
    )
    .map(lambda k, v: common.create_command(k, v, entry=entry))
)

if __name__ == "__main__":
    entry()
