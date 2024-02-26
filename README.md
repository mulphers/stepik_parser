## Parsing script

Script for parsing data from the site https://stepik.org/

#### 1. Project structure:

````
stepik_parser/
├── src/
│   ├── common/
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── parser/
│   │   ├── __init__.py
│   │   └── stepik.py
│   ├── storage/
│   │   └── result.json
│   ├── __init__.py
│   └── __main__.py
├── .gitignore
├── README.md
└── requirements.txt
````

### 2. How to copy a project:

````
git clone https://github.com/mulphers/stepik_parser.git
````

### 3. Install packages:

````
pip install -r requirements.txt
````

### 4. Run a scripts:

Go to your working directory and enter the command

````
python -m src
````

### 5. Results:

The obtained data is in src/storage/result.json

The file has this structure

````
[
    {
        "title": "...",
        "url": "...",
        "price": ...
        "learners_count": ...,
        "with_certificate": ...
    },
    ...
]
````
