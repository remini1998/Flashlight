import urllib


def results(parsed, original_query):
    if '~query' not in parsed:
        return

    query = parsed['~query']

    # Query is too short
    if len(query) < 2:
        return

    url_template = 'https://warehouse.python.org/search/?q={0}'

    url = url_template.format(urllib.quote_plus(query))
    html = """
    <script>
    setTimeout(function () {
        window.location = '""" + url + """';
    }, 100);
    </script>
    """

    return {
        "title": "Search PyPI for '{0}'".format(query),
        "run_args": [url],
        "html": html,
        "webview_links_open_in_browser": True
    }