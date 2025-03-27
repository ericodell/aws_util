Installation
============

To install `aws_util` locally in a virtual environment, use:

.. code-block:: bash

   source venv.sh

.. raw:: html

   <button class="copy-button" data-clipboard-text="source venv.sh">Copy</button>

* Now you can use the `ecs_connect` command to run your script.
* **Important:** You need to provide your AWS profile.

.. code-block:: bash

   ecs_connect -p your_aws_profile

.. raw:: html

    <button class="copy-button" data-clipboard-text="ecs_connect -p your_aws_profile">Copy</button>

* Replace `your_aws_profile` and optionally `your_aws_region` with your actual AWS profile name and region.
* Example:

.. code-block:: bash

   ecs_connect -p my-dev-profile -r us-east-1

.. raw:: html

    <button class="copy-button" data-clipboard-text="ecs_connect -p my-dev-profile -r us-east-1">Copy</button>

