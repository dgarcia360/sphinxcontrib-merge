===================
sphinxcontrib-merge
===================

.. image:: https://badge.fury.io/py/sphinxcontrib-merge.svg
    :target: https://badge.fury.io/py/sphinxcontrib-merge
    :alt: PyPi Status

.. image:: https://travis-ci.org/dgarcia360/sphinxcontrib-merge.svg?branch=master
    :target: https://travis-ci.org/dgarcia360/sphinxcontrib-merge
    :alt: Travis Status

Sphinx extension to build documentation from multiple remote sources.

For example, you can use it to produce a consistent documentation site by merging pages hosted in different GitHub repositories.

Installation
============

1. Install sphinxcontrib-merge using pip.

.. code-block:: bash

    pip install sphinxcontrib-merge

2. Add the extension to your Sphinx project ``conf.py`` file.

.. code:: python

  extensions = ['sphinxcontrib.merge']

Usage
=====

Use the ``merge`` directive to render the content of a remote file:

.. code:: restructuredText

    .. merge:: https://raw.githubusercontent.com/dgarcia360/sphinxcontrib-merge/master/docs/example.rst

.. note:: At the current moment the extension only works with ``.rst`` files.

Roadmap
=======

See the `open issues <https://github.com/dgarcia360/sphinxcontrib-merge/issues>`_ for a list of proposed features.

Contributing
============

Contributions are welcome and appreciated! Check `CONTRIBUTING.md  <https://github.com/dgarcia360/sphinxcontrib-merge/blob/master/CONTRIBUTING.md>`_ file.

License
=======

Copyright (c) 2019 David Garcia (`@dgarcia360 <https://davidgarcia.dev>`_).

Licensed under MIT license (see `LICENSE.md <LICENSE.md>`_ for details)