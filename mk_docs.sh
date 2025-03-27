#!/bin/bash

# Script to create Sphinx documentation files in the docs/ directory.

# Check if the docs directory exists
if [ -d "docs" ]; then
  echo "docs directory already exists. Skipping creation."
else
  echo "Creating docs directory..."
  mkdir docs
fi

# Navigate to the docs directory
cd docs

# Initialize Sphinx if conf.py doesn't exist
if [ ! -f "conf.py" ]; then
  echo "Initializing Sphinx..."
  sphinx-quickstart --quiet \
    --project="aws_util" \
    --author="Your Name" \
    --release="1.0" \
    --language="en" \
    --sep \
    --ext-autodoc \
    --ext-viewcode \
    --ext-doctest \
    --ext-intersphinx \
    --ext-todo

  # Create index.rst and other rst files
  echo "Creating index.rst..."
  cat <<EOF > index.rst
aws_util Documentation
======================

.. toctree::
   :maxdepth: 2

   installation
   usage
   troubleshooting

Installation
============

To install aws_util...

Usage
=====

How to use aws_util...

Troubleshooting
===============

Common issues and solutions...

EOF

  echo "Creating installation.rst..."
  cat <<EOF > installation.rst
Installation
============

To install \`aws_util\` locally in a virtual environment, use:

.. code-block:: bash

   source venv.sh

* Now you can use the \`ecs_connect\` command to run your script.
* **Important:** You need to provide your AWS profile.

.. code-block:: bash

   ecs_connect -p your_aws_profile

* Replace \`your_aws_profile\` and optionally \`your_aws_region\` with your actual AWS profile name and region.
* Example:

.. code-block:: bash

   ecs_connect -p my-dev-profile -r us-east-1

EOF

  echo "Creating usage.rst..."
  cat <<EOF > usage.rst
Usage
=====

After installation, you can directly execute commands on an ECS container using the \`ecs_connect\` command.

Example:

.. code-block:: bash

   ecs_connect -p your_aws_profile

This will open an interactive bash shell in the selected ECS container.

For more options, check the help message:

.. code-block:: bash

   ecs_connect --help

EOF

    echo "Creating troubleshooting.rst..."
    cat <<EOF > troubleshooting.rst
Troubleshooting
===============

* **\\"command not found: ecs_connect\\"**:
    * Make sure you activated the virtual environment (if you created one).
    * Make sure you ran the \`pip install -e .\` command.
* **\\"ModuleNotFoundError: No module named 'boto3'\\"**:
    * Make sure you activated the virtual environment and ran the \`pip install -e .\` command.
* **\\"Error with AWS credentials\\"**:
    * Make sure your AWS CLI is configured correctly.
    * Make sure the profile you are using is valid.
* **\\"Error with arguments\\"**:
    * Double check that you are using the correct arguments.
    * Double check that you are using the correct values for the arguments.
EOF

  echo "Sphinx documentation files created."

else
  echo "Sphinx configuration (conf.py) already exists. Skipping initialization."
fi

# Build the documentation
echo "Building HTML documentation..."
make html

echo "Documentation build complete. View the docs in _build/html/index.html"
