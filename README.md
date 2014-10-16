WearHacks Website
=======


# Dependencies
To install, run:
   
     $ pip install -r requirements.txt

# Tests

To run individual tests, under the pypoker parent folder,

    $ python -m unittest tests.<module name>

To run all the tests, under the pypoker parent folder, just do:

    $ python -m unittest discover tests -v

To run all tests using nose,

    $ nosetests -v tests

To run all tests using nose and coverage,

    $ nosetests -v --with-coverage --cover-package=mooc_aggregator_restful_api --cover-inclusive --cover-erase tests

# Authors

Ahmad Shehaaz Saif - <shehaaz@gmail.com>

Ari Ramdial - <ari.ramdial@gmail.com>

Usman Ehtesham Gul - <uehtesham90@gmail.com>
