Installation
============

To install `aws_util` locally in a virtual environment, use:

.. code-block:: bash

   source venv.sh

* Now you can use the `ecs_connect` command to run your script.
* **Important:** You need to provide your AWS profile.

.. code-block:: bash

   ecs_connect -p your_aws_profile

* Replace `your_aws_profile` and optionally `your_aws_region` with your actual AWS profile name and region.
* Example:

.. code-block:: bash

   ecs_connect -p my-dev-profile -r us-east-1

