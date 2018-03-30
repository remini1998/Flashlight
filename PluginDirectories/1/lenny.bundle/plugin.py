def results(parsed, original_query):
    with open('lenny.html','r') as f_open:
        html = f_open.read()
    return {
        "title": 'Le Lenny Face',
        "run_args": [],
        "html": html
    }

def run(url):
    import os, pipes
    os.system('open "{0}"'.format(url))
