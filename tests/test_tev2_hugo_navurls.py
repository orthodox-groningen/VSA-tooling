from scripts.tev2_hugo import prefixed_navurl


def test_prefixed_navurl_keeps_local_root_links_root_relative():
    assert (
        prefixed_navurl("http://localhost:1313/terminologie/zangstuk", "/")
        == "http://localhost:1313/terminologie/zangstuk"
    )


def test_prefixed_navurl_adds_publication_prefix():
    assert (
        prefixed_navurl(
            "http://localhost:1313/terminologie/zangstuk",
            "/VSA-tooling/preview/",
        )
        == "http://localhost:1313/VSA-tooling/preview/terminologie/zangstuk"
    )
