"""
"""

import json

# from pynchon.api import render
from pynchon.abcs import visitor


def test_traversed():
    # visited=[]
    def visit(value=None, path=None):
        print(f"[{path}: {value}]")
        # visited.append([path,value])
        return value

    obj = dict(foo=dict(bar="bar", baz=dict(boom="bonk", list=["a", "b", "c"])))
    traversed = visitor.traverse(obj, visitor=visit)
    paths = traversed["paths"]
    assert paths == [
        ".foo",
        ".foo.bar",
        ".foo.baz",
        ".foo.baz.boom",
        ".foo.baz.list",
        ".foo.baz.list.0",
        ".foo.baz.list.1",
        ".foo.baz.list.2",
    ]
    print(json.dumps(traversed.visits, indent=2))


# def test_visit_kls():
#     obj = visitor.JinjaDict(
#         bonk="bonk{{dot}}",
#         dot="3",
#         docs_root="docs",
#         jinja={"includes": ["{{docs_root}}/includes"]},
#     )
#     traversed = obj.traversal
#     # expected = ['.docs_root', '.jinja', '.jinja.includes', '.jinja.includes.0']
#     # assert traversed.paths==expected
#     assert set(obj.unresolved) == {".jinja.includes.0", ".bonk"}
#     obj.render()
#     assert not obj.unresolved
#     assert obj["jinja"]["includes"] == ["docs/includes"]
#
#     # print(json.dumps(traversed,indent=2))
