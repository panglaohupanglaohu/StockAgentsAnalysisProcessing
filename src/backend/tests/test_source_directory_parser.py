from domain.information_sources.directory_parser import parse_directory


def test_parse_rss_directory_table_and_dedupe():
    html = b'''<table><tr><th>Name</th><th>RSS</th></tr>
    <tr><td>Alpha</td><td><a href="https://alpha.example/feed.xml">feed</a></td></tr>
    <tr><td>Alpha again</td><td><a href="https://alpha.example/feed.xml">feed</a></td></tr>
    <tr><td>Beta</td><td><a href="https://beta.example/atom.xml">atom</a></td></tr></table>'''
    rows = parse_directory(html, "https://directory.example/list", max_items=20)
    assert [row["url"] for row in rows] == [
        "https://alpha.example/feed.xml",
        "https://beta.example/atom.xml",
    ]
    assert rows[0]["name"] == "Alpha"


def test_parse_opml_directory():
    opml = b'''<opml version="2.0"><body><outline text="One" xmlUrl="https://one.example/rss"/><outline title="Two" xmlUrl="https://two.example/atom"/></body></opml>'''
    rows = parse_directory(opml, "https://directory.example/opml", max_items=20)
    assert len(rows) == 2
    assert rows[1]["name"] == "Two"


def test_parse_markdown_directory_without_html_table():
    markdown = b"[AI feed](https://ai.example/rss.xml)\n[World feed](https://world.example/atom.xml)"
    rows = parse_directory(markdown, "https://directory.example/readme", max_items=20)
    assert [row["name"] for row in rows] == ["AI feed", "World feed"]
