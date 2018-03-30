#! /usr/bin/env python2

def results(fields, original_query):
    doi_name = fields['~name']
    url = 'https://doi.org/' + doi_name
    html = "<script> setTimeout(function() {{ window.location = '{0}'}}, 500); </script>".format(url)
    return {
            "title": "Go to doi:{0}".format(doi_name),
            "run_args": [doi_name],
            "html": html
            }

def run(doi_name):
    import subprocess
    url = 'https://doi.org/' + doi_name
    subprocess.Popen(['open', url])
    
