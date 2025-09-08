"""pynchon.codemod.docstrings.javadoc"""

from pynchon.util import lme

import libcst as cst

from .base import base

LOGGER = lme.get_logger(__name__)


class module(base):
    DESCRIPTION: str = """\n\tAdds or updates javadoc for Modules"""


class function(base):
    DESCRIPTION: str = """\n\tAdds or updates javadoc for Functions"""

    def leave_FunctionDef(
        self,
        original_node: cst.FunctionDef,
        updated_node: cst.FunctionDef,
    ) -> cst.FunctionDef:
        # LOGGER.critical(original_node)
        return original_node
