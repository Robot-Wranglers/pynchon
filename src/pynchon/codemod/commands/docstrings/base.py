""" pynchon.codemod.docstrings.base """

import argparse

from libcst.codemod import CodemodContext

from pynchon.util import lme

LOGGER = lme.get_logger(__name__)

from libcst.codemod import ContextAwareTransformer


class base(ContextAwareTransformer):  # VisitorBasedCodemodCommand):
    DESCRIPTION: str = """\n\tAbstract, don't use this directly"""

    def __init__(
        self,
        context: CodemodContext,
        # formatter: str = "black",
        # parameter_count: Optional[int] = None,
        # argument_count: Optional[int] = None,
    ) -> None:
        super().__init__(context)
        # self.parameter_count: int = parameter_count or presets["parameter_count"]
        # self.argument_count: int = argument_count or presets["argument_count"]

    @staticmethod
    def add_args(arg_parser: argparse.ArgumentParser) -> None:  # noqa
        """ """
