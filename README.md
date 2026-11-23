# Python Training & DSA Practice Repository

A structured repository containing training modules, code implementations, interactive Jupyter notebooks, and hands-on practice across core Python, Object-Oriented Programming (OOP), Data Structures & Algorithms (DSA), Data Science libraries, Databases, and FastAPI development.

---

## 📁 Repository Overview & Folder Structure

```text
.
├── DSA/                    # Data Structures & Algorithms in Python
├── OOPS/                   # Object-Oriented Programming Concepts & Exercises
├── concepts/               # Core Architecture & Software Engineering Concepts
├── fastAPI/                # REST API Development using FastAPI & Pydantic
├── Pandas/                 # Data Analysis and Manipulation with Pandas
├── numpy/                  # Numerical Computing and Array Operations with NumPy
├── mysql/                  # Relational Database Management & SQL Queries
├── src/                    # Source package module (training)
├── pyproject.toml          # Project configuration, dependencies, and metadata
└── uv.lock                 # Lockfile for reproducible dependencies (uv)
```

---

## 📚 Detailed Module Descriptions

### 1. `DSA/` — Data Structures & Algorithms

Focuses on algorithmic problem-solving, complexity analysis, and Pythonic implementations:

- **`list_dsa.ipynb`**: List operations, two-pointer techniques, recursion, moving zeros, frequency count, and sub-problems.
- **`string_dsa.ipynb`**: String manipulation, searching, palindromes, and string algorithm challenges.
- **`time_space_complexity.ipynb`**: Time & Space Complexity (Big-O notation) breakdowns and trade-offs.
- **`testing.ipynb`**: Scratchpad for testing new algorithms and edge cases.

### 2. `OOPS/` — Object-Oriented Programming

Covers design patterns, object modeling, and interview questions:

- **`method_overloading.py`**: Implementation and workarounds for method overloading in Python.
- **`method_overiding.py`**: Inheritance and dynamic method overriding.
- **`decorators.ipynb`**: Custom decorators, wrapper functions, and metadata preservation.
- **`interview_ques.ipynb`**: OOP interview preparation covering Encapsulation, Abstraction, Polymorphism, and Inheritance.

### 3. `fastAPI/` — Backend API Development

Practical implementation of modern, asynchronous RESTful APIs using FastAPI:

- **`todoapp.py`**: Complete CRUD (Create, Read, Update, Delete) Todo application.
- **`getAPI.py`**: Basic routing, query handling, and GET endpoints.
- **`body_path_query.py`**: Path parameters, query parameters, and request body validation.
- **`req_res_model.py` & `nested-pydantic-model.py`**: Data validation using Pydantic models and nested structures.
- **`dependency_injection.py`**: FastAPI dependency injection system (`Depends`).
- **`middleware.py`**: Custom HTTP middleware, timing, logging, and request processing pipelines.

### 4. `Pandas/` — Data Analysis & Manipulation

End-to-end data processing workflows using the Pandas library:

- **`intro_pandas.ipynb`**: Core concepts, installation, and data structures.
- **`series.ipynb`**: Single-dimensional labeled arrays and basic operations.
- **`dataframe.ipynb`**: Tabular data manipulation, slicing, filtering, and indexing.
- **`Data_operation.ipynb`**: Grouping, aggregations, merges, joins, and missing value imputation.
- **`practice.ipynb`**: Real-world dataset problem-solving and analytics.

### 5. `numpy/` — Numerical Computing

- **`intro.ipynb`**: Multi-dimensional NumPy arrays (`ndarray`), broadcasting, vectorization, indexing, and linear algebra operations.

### 6. `mysql/` — Databases & SQL Integration

Database design, query writing, and Python-database connectivity:

- **`db_and_table.sql`**: SQL DDL & DML scripts for creating schemas and tables.
- **`creation.db`**: Local database storage and schemas.
- **`connections_setup.ipynb`**: Connecting Python to MySQL databases.
- **`sql_clause.ipynb`**: Deep dive into SQL clauses (`SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `JOIN`).
- **`sql_pandas_conn.ipynb`**: Executing SQL queries directly into Pandas DataFrames (`pd.read_sql`).

### 7. `concepts/` — Core Engineering Topics

- **`base64.ipynb`**: Binary-to-text encoding and decoding.
- **`stateless.ipynb` & `statefull.ipynb`**: Comparing stateless vs stateful architectures and session handling.
- **`testing.ipynb`**: Prototyping conceptual code.

---

## 🛠️ Environment Setup & Getting Started

This repository uses [**`uv`**](https://github.com/astral-sh/uv), a fast Python package and project manager.

### Prerequisites

- Python >= 3.12
- `uv` installed (`curl -LsSf https://astral.sh/uv/install.sh | sh` or via package manager)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Training
   ```

2. **Sync and create the virtual environment:**

   ```bash
   uv sync
   ```

   This will automatically create a `.venv` directory and install all locked dependencies.

3. **Activate the virtual environment (optional):**
   ```bash
   source .venv/bin/activate
   ```

---

## 🚀 Running the Code

### Running Python Scripts

Use `uv run` to execute scripts directly within the managed environment:

```bash
uv run fastAPI/todoapp.py
```

### Running the FastAPI Development Server

```bash
cd fastAPI
uv run fastapi dev todoapp.py
```

API docs will be available at: `http://127.0.0.1:8000/docs`

### Running Jupyter Notebooks

1. Ensure the kernel package is available:
   ```bash
   uv add ipykernel
   ```
2. Open any `.ipynb` file in your IDE (VS Code / Antigravity).
3. Select the **`.venv`** kernel in the top-right corner of the notebook.
4. Execute cells using `Shift + Enter`.
