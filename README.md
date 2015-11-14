
## Setup local env

* As admin `npm install -g gulp`
* In the project folder `npm install`, `bower install`
* Make a virtual environment with `virtualenv -p` and activate it
* `pip install -r requirements_dev.txt` (use requirements.txt for production)
* create `settings_local.py` for altering predefined settings

## Gulp

* `gulp index` - build index.html
* `gulp autoprefix` - run autoprefixer against all css
* `gulp build` - run both tasks

## Run tests

`py.test -v`