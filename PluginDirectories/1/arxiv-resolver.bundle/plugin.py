#! /usr/bin/env python2

def results(fields, original_query):
    doi_name = fields['~name']
    html = """
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
<title> Arxiv.org </title>
<link rel="stylesheet" type="text/css" media="screen" href="https://arxiv.org/css/arXiv.css?v=20170424" />
<script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
</head>
<body>
    <div id="arxiv"></div>
    <script>
var base = $('<base href="https://arxiv.org/">');
var mathjax_config = $('<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [["$","$"]]}});<\/script>');
var mathjax_js = $('<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML"><\/script>');
$("head").append(base);
$("#arxiv").load('https://arxiv.org/search #content', {query: '%s', searchtype: 'all'}, function() {$(".extra-services").remove(); $(".leftcolumn").css("margin-right", "0"); $("head").append(mathjax_config); $("head").append(mathjax_js); MathJax.Hub.Queue(["Typeset",MathJax.Hub,"arxiv"]);});
    </script>
</body>
</html>""" % doi_name
    return {
            "title": "Search for {0} on arxiv.org".format(doi_name),
            "run_args": [doi_name],
            "html": html
            }

def run(doi_name):
    import os, pipes, urllib
    url = 'https://arxiv.org/search?' + urllib.urlencode([('query', doi_name), ('searchtype', 'all')])
    os.system('open {0}'.format(pipes.quote(url.encode('utf8'))))
    
