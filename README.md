# Objective

Explore the API based integration points for autotrader.com by leveraging Python Programming Language.

# Workspace Configuration

## Pre-Requisites

* Make sure that Python3 is installed in your environment
* If using vscode, it would be suggested to install the recommended plugins

## Initial Setup

### Creating and Activating a Python Virtual Environment

From the workspace's root folder, please type the following commands:

```python
python3 -m venv .
source env/bin/activate
```

### Upgrading pip

```python
python3.10 -m pip install --upgrade pip

Requirement already satisfied: pip in /opt/homebrew/lib/python3.10/site-packages (23.0.1)
Collecting pip
Using cached pip-23.1.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
Attempting uninstall: pip
    Found existing installation: pip 23.0.1
    Uninstalling pip-23.0.1:
    Successfully uninstalled pip-23.0.1
Successfully installed pip-23.1.2
```

### Installing the Request Py Library

```python
pip install requests

Collecting requests
Downloading requests-2.31.0-py3-none-any.whl (62 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 1.7 MB/s eta 0:00:00
Collecting urllib3<3,>=1.21.1
Downloading urllib3-2.0.2-py3-none-any.whl (123 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.2/123.2 kB 2.2 MB/s eta 0:00:00
Requirement already satisfied: certifi>=2017.4.17 in /opt/homebrew/lib/python3.10/site-packages (from requests) (2022.12.7)
Collecting charset-normalizer<4,>=2
Downloading charset_normalizer-3.1.0-cp310-cp310-macosx_11_0_arm64.whl (123 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.0/123.0 kB 2.4 MB/s eta 0:00:00
Collecting idna<4,>=2.5
Downloading idna-3.4-py3-none-any.whl (61 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB 3.7 MB/s eta 0:00:00
Installing collected packages: urllib3, idna, charset-normalizer, requests
Successfully installed charset-normalizer-3.1.0 idna-3.4 requests-2.31.0 urllib3-2.0.2
```

### Installing the Request Py Library

```python
pip install flask

Collecting flask
Downloading Flask-2.3.2-py3-none-any.whl (96 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.9/96.9 kB 1.8 MB/s eta 0:00:00
Collecting Werkzeug>=2.3.3 (from flask)
Downloading Werkzeug-2.3.4-py3-none-any.whl (242 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 kB 2.9 MB/s eta 0:00:00
Collecting Jinja2>=3.1.2 (from flask)
Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 2.6 MB/s eta 0:00:00
Collecting itsdangerous>=2.1.2 (from flask)
Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting click>=8.1.3 (from flask)
Downloading click-8.1.3-py3-none-any.whl (96 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 3.7 MB/s eta 0:00:00
Collecting blinker>=1.6.2 (from flask)
Downloading blinker-1.6.2-py3-none-any.whl (13 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
Downloading MarkupSafe-2.1.2-cp310-cp310-macosx_10_9_universal2.whl (17 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.3.4 blinker-1.6.2 click-8.1.3 flask-2.3.2 itsdangerous-2.1.2
```

## References

* [Autotrader.com APIs Specification for developers](https://developers.autotrader.co.uk/api#introduction)