#!/usr/bin/env bash
set -xeuo pipefail
python -m gripe ls
pynchon python-libcst gen docstrings --help
pynchon --help
pynchon init --help
python -mpynchon --help
python -mpynchon.util.files --help
python -mpynchon.util.text --help
python -mpynchon.util.text.loadf --help
python -mpynchon.util.text loadf --help
python -mpynchon.util.text.render --help
python -mpynchon.util.text render --help
pynchon raw | jq .config_files
pynchon plugins list | jq .
pynchon cfg
pynchon src cfg
pynchon src plan
pynchon j list
pynchon jinja list
pynchon jinja plan
pynchon jinja sh -c'self.logger.debug("hello world")'
pynchon docs list | jq .
pynchon docs plan | jq .
pynchon git cfg | jq .
pynchon pandoc cfg  | jq .
pynchon pattern new --help
pynchon py --help
pynchon src plan | jq .
pynchon src sorted --help
pynchon makefile parse --help
pynchon makefile parse Makefile | jq . > /dev/null
pynchon parse markdown --help
pynchon markdown parse --help
pynchon markdown to-pdf --help
pynchon markdown normalize --help
pynchon parse markdown README.md --codeblocks | jq .
pynchon markdown show README.md
pynchon drawio --help
pynchon draw --help
pynchon draw ls --help
pynchon draw render --help
pynchon plugins schema jinja --markdown \
  | pynchon markdown preview /dev/stdin
pynchon github open --help
