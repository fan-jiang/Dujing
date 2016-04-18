# This Python file uses the following encoding: utf-8

def Convert(content):
    tradtionalToSimplified = {
        u"?":u"“", 
        u"?":u"”",
        u"?":u"‘",
        u"?":u"’",

    }
    for key in tradtionalToSimplified: 
        content = content.replace(key, tradtionalToSimplified[key])
    return content