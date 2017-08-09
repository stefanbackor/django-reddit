## Django
- The Web framework
- for perfectionists with deadlines
- Django Reinhart
- 12 years old

(python, multinheritance-mixins, introspection, everything is object, allows functional programming)

## Big names
Django: Instagram, Disqus, Bitbucket, Spotify and Pinterest
Python: Youtube, Dropbox, Google search, Reddit

## Design principles - The Zen of Python
- Explicit is better than implicit (No magic, unless it provides huge convenience)
- Loose coupling (The various layers of the framework shouldn’t “know” about each other unless absolutely necessary.)
- DRY (Redundancy is bad. Normalization is good.)
- Consistency (The framework should be consistent at all levels.)

(https://docs.djangoproject.com/en/1.11/misc/design-philosophies)
(https://www.python.org/dev/peps/pep-0020/)

## MTV
- model, view, template
(Not MVC. Controllers are for event driven apps, not for stateless HTTP.)

## Model
Object related modal layer
- Active Record design pattern (Both data and behaviour)
- SQL efficiency (execute SQL statements as few times as possible; optimize internally;)
- Terse syntax (as little syntax as possible, auto joins, object has access to related and vice versa)

## View
Logic control layer
- Simplicity (function vs class based)
- Loose coupling (non aware of template)
- Explicit http method handling (easy to distinguish between GET and POST data)

## Template
Tool that controls presentation and presentation-related logic
- HTML or not HTML (any text-based formats)
- Assume designer competence (expects template authors are comfortable editing HTML directly.)
- Just enough programming-esque functionality (written by designers, not programmers)
- Safety and security - (out of the box, csrf)
- Extensibility (custom template tags and filter)


## App














