# nfl-stats

## Backend strcuture
- It is build with Fastapi + SQLAlchemy (Postgres) 
- Sample [ref](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#project-structure)
'''
server/
├── feature/
│   ├── models.py           # db models
│   ├── schemas.py          # pydantic models
│   ├── routes.py           # core of each module with all the endpoints
│   ├── service.py          # module specific business logic
│   ├── dependencies.py     # router dependencies
│   ├── constants.py        # module specific constants and error code
│   ├── exceptions.py       # module specific exceptions eg PostNotFound, InvalidUserData
│   ├── utils.py            # non business logic functins, eg response normalization, data enrichment,etc
│   └── __init__.py
├── middleware/             # cross-cutting, shared code
│   ├── middelware-1.py
│   └── __init__.py
├── utils/           # cross-cutting, shared code
│   ├── util-1.py
│   ├── util-2.py
│   └── __init__.py
├── exceptions/            # cross-cutting, shared code
│   ├── exceptions-1.py
│   ├── exception-2.py
│   └── __init__.py
├── database.py         # SQLAlchemy engine, session
├── models.py           # import/aggregate all models
├── main.py             # FastAPI app
└── __init__.py

'''