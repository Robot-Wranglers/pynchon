"""test_markdown_parser:"""

import shil
import pytest


@pytest.fixture
def markdown_sample_1(fixtures_dir):
    return fixtures_dir / "sample1.md"


@pytest.fixture
def markdown_sample_2(fixtures_dir):
    return fixtures_dir / "sample2.md"


def test_parse_md_file_links(markdown_sample_1):
    resp = shil.invoke(
        f"pynchon markdown parse {markdown_sample_1} --links", load_json=True
    )
    data = resp.data
    links = data[str(markdown_sample_1)]
    assert len(links) == 2 and "foo.md" in links


def test_parse_md_file(markdown_sample_1):
    resp = shil.invoke(f"pynchon markdown parse {markdown_sample_1}", load_json=True)
    data = resp.data
    assert str(markdown_sample_1) in data.keys()


def test_parse_md_files(
    markdown_sample_1,
    markdown_sample_2,
):
    resp = shil.invoke(
        f"pynchon markdown parse {markdown_sample_1} {markdown_sample_2}",
        load_json=True,
    )
    data = resp.data
    assert str(markdown_sample_1) in data.keys()
    assert str(markdown_sample_2) in data.keys()
