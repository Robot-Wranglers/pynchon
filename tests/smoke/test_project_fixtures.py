"""tests for `pynchon` CLI"""

# from pynchon.util import testing
#
# TEST_INFO = testing.get_test_info(__file__)
# PROJECT_FIXTURES = TEST_INFO.fixtures.path / "projects"


# def test_fixtures():
#     project_folders = [d for d in PROJECT_FIXTURES.iterdir() if d.is_dir()]
#     import pyjson5
#
#     for p in project_folders:
#         p = p.absolute()
#         expected = p / "expected.json5"
#         with open(expected) as fhandle:
#             expected = pyjson5.loads(fhandle.read())
#         cmd_t = f"cd {p} && "
#         cmd = cmd_t + "PYNCHON_ROOT=. pynchon project config"
#         cmd = invoke(cmd, load_json=True)
#         assert cmd.succeeded
#         project_config = cmd.json
#         actual = sorted(project_config.items())
#         expected = sorted(expected.items())
#         assert actual == expected, [p, actual, expected]
#         # # raise Exception(data)
#         # for k in expected:
#         #     assert project_config[k]
#         # pynchon = project_config['pynchon']
#         # assert pynchon
#         # # raise Exception(pynchon)
#         # assert pynchon['config_source']
#         # extra_tests = p/"tests.py"
#         # if extra_tests.exists():
#         #     namespace = dict(project_config=project_config)
#         #     with open(extra_tests,'r') as fhandle:
#         #         exec(fhandle.read(), namespace)
#         #     for k,v in namespace.items():
#         #         if k.startswith('test_'):
#         #             v()
