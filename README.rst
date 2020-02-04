Flask-Banana
============

Localize your Flask application using the banana_ file format, popularized by
MediaWiki_.

Usage
-----

In your ``app.py``::

    from flask import Flask
    from flask_banana import Banana
    from pathlib import Path

    app = Flask(__name__)
    banana = Banana(app, Path(__file__).resolve().parent / 'i18n')

You can also use the ``init_app`` pattern as well.

In your template the ``_(...)`` function is aliased to ``banana.translate()``::

    <body>
    <p>{{ _('some-message-key') }}</p>
    </body>

To change the language, set the ``banana.language`` property. You might also
want to try the Flask-ULS_ library for better client-side support for changing
the interface language.

Flask-ULS integration
---------------------

Flask-Banana can automatically configure and integrate with Flask-ULS, just
pass the ULS instance to Banana during setup::

    app = Flask(__name__)
    uls = ULS(app)
    banana = Banana(app, Path(__file__).resolve().parent / 'i18n', uls)

Banana will configure ULS to enable all of the languages that have translations
and then default to using the language configured through ULS.

Configuration
-------------

* ``BANANA_DEFAULT_LANGUAGE`` (default: ``'en'``): the language to default to
  if one hasn't been manually set through Banana nor ULS.

License
-------
Flask-Banana is available under the terms of the GPL, version 3 or any later
version.

.. _banana: https://github.com/wikimedia/banana-i18n#banana-file-format
.. _MediaWiki: https://www.mediawiki.org/wiki/MediaWiki
.. _Flask-ULS: https://pypi.org/project/Flask-ULS/
