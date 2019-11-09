# sphinxcontrib-merge

[![PyPI version](https://badge.fury.io/py/sphinxcontrib-merge.svg)](https://badge.fury.io/py/sphinxcontrib-merge)
[![Travis Status](https://travis-ci.org/dgarcia360/sphinxcontrib-merge.svg?branch=master)](https://travis-ci.org/dgarcia360/sphinxcontrib-merge)

Sphinx extension to build documentation from multiple remote sources.

For example, you can use it to produce a consistent documentation site by merging pages hosted in different GitHub repositories.

## Installation

1. Install ``sphinxcontrib-merge`` using pip.

```
pip install sphinxcontrib-merge
```

2. Add the extension to your Sphinx project ``conf.py`` file.

```
extensions = ['sphinxcontrib.merge']
```

## Usage

Use the ``merge`` directive to render the content of a remote file:

```
.. merge:: https://raw.githubusercontent.com/dgarcia360/sphinxcontrib-merge/master/docs/example.rst
```

> Note: At the current moment the extension only works with ``.rst`` files.

## Roadmap

See the [open issues](https://github.com/dgarcia360/sphinxcontrib-merge/issues) for a list of proposed features.

## Contributing

Contributions are welcome and appreciated! Check [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

Copyright (c) 2019 David Garcia ([@dgarcia360](https://davidgarcia.dev>)).

Licensed under MIT license (see [LICENSE.md](LICENSE.md) for details)
