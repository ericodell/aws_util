# Installing aws_util

This document provides instructions for installing the `aws_util` package using various methods.

## Using `venv` (Recommended)

1.  **Create a Virtual Environment:**

    ```bash
    cd aws_util
    python3 -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    * **Linux/macOS:**

        ```bash
        source venv/bin/activate
        ```

    * **Windows:**

        ```bash
        venv\Scripts\activate
        ```

3.  **Install in Editable Mode (Recommended for Development):**

    ```bash
    pip install -e .
    ```

    Or, for a regular installation:

    ```bash
    pip install .
    ```

4.  **Install Dependencies (if needed):**

    ```bash
    pip install boto3
    ```

5.  **Verify Installation (Optional):**

    ```bash
    pip list | grep aws_util
    python3 -c "import aws_util.ecs_utils"
    ```

6.  **Run Tests (Optional but Recommended):**

    ```bash
    python3 -m unittest discover
    ```

7.  **Deactivate the Virtual Environment (When Finished):**

    ```bash
    deactivate
    ```

## Using `pipenv`

1.  **Navigate to the `aws_util` directory:**

    ```bash
    cd aws_util
    ```

2.  **Initialize `pipenv`:**

    ```bash
    pipenv install
    ```

    This creates a `Pipfile` and `Pipfile.lock` and a virtual environment.

3.  **Install Dependencies (if needed):**

    ```bash
    pipenv install boto3
    ```

4.  **Enter the `pipenv` Shell:**

    ```bash
    pipenv shell
    ```

5.  **Install the Package in Editable Mode (Recommended):**

    ```bash
    pip install -e .
    ```

    Or, for a regular installation:

    ```bash
    pip install .
    ```

6.  **Verify Installation (Optional):**

    ```bash
    pip list | grep aws_util
    python3 -c "import aws_util.ecs_utils"
    ```

7.  **Run Tests (Optional but Recommended):**

    ```bash
    python3 -m unittest discover
    ```

8.  **Exit the `pipenv` Shell:**

    ```bash
    exit
    ```

## Regular Installation (Without Virtual Environments)

**Warning:** Installing packages globally without virtual environments can lead to dependency conflicts. It's highly recommended to use `venv` or `pipenv`.

1.  **Navigate to the `aws_util` directory:**

    ```bash
    cd aws_util
    ```

2.  **Install the Package in Editable Mode (Recommended for Development):**

    ```bash
    pip install -e .
    ```

    Or, for a regular installation:

    ```bash
    pip install .
    ```

3.  **Install Dependencies (if needed):**

    ```bash
    pip install boto3
    ```

4.  **Verify Installation (Optional):**

    ```bash
    pip list | grep aws_util
    python3 -c "import aws_util.ecs_utils"
    ```

5.  **Run Tests (Optional but Recommended):**

    ```bash
    python3 -m unittest discover
    ```
