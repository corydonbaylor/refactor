# refactor

### useful commands

In order to see the directory structure:
`tree -I 'venv|__pycache__'`

In order to freeze the requirements:
`pip freeze > requirements.txt`

### Info about this Project

```
.
├── Procfile
├── README.md
├── app
│   ├── __init__.py
│   ├── coding
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates
│   │       └── coding.html
│   ├── main
│   │   ├── __init__.py
│   │   ├── resources
│   │   │   └── css
│   │   │       └── nav.css
│   │   ├── routes.py
│   │   └── templates
│   │       ├── base.html
│   │       └── index.html
│   ├── statistics
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates
│   │       └── statistics.html
│   ├── travel
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates
│   │       └── travel.html
│   ├── tutorials
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates
│   │       └── tutorials.html
│   └── utils
│       └── __init__.py
├── requirements.txt
└── run.py
```
