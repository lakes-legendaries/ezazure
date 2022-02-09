##########
Quickstart
##########

#. Install this package:

   .. code-block:: bash

      pip install ezazure

#. Put your Azure connection string and container name in a :code:`.ezazure` file:

   .. code-block:: yaml

      connection_str: AZURE_CONNECTION_STRING
      container: CONTAINER_NAME

#. Run from the command line either of the following:

   .. code-block:: bash

      python -m ezazure --upload FNAME
      python -m ezazure --download FNAME

#. :code:`ezazure` supports regex pattern matching:

   .. code-block:: bash

      python -m ezazure --upload --regex FNAME[0-9]+
      python -m ezazure --download --regex FNAME.*

#. You can also use this package as an API:

   .. code-block:: python

      from ezazure import Azure


      azure = Azure()
      azure.upload(fname)
      azure.download(fname)
