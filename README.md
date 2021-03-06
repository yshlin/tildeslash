tildeslash
==========

tildeslash is a web-based codelog software, i.e. blogware for developers.  
Make use of the powerful [Ace][ace] as [Markdown][markdown] editor.  

tildeslash is named from the pathname of home folder, a.k.a `~/` on Unix/Linux.  
The goal of tildeslash is to give developers a comforting home on the web,  
where they can easily share and teach coding skills for the public.  

tildeslash is based on [Mozilla][mozilla]'s [Playdoh][playdoh-docs],  
which is a web application template based on [Django][django].  

Patches are welcome!  
Feel free to fork and contribute to this project on [github][gh-tildeslash].  


[gh-tildeslash]: https://github.com/yshlin/tildeslash
[django]: http://www.djangoproject.com/
[gh-playdoh]: https://github.com/mozilla/playdoh
[playdoh-docs]: http://playdoh.rtfd.org/
[ace]: http://ace.c9.io/
[markdown]: http://daringfireball.net/projects/markdown/
[mozilla]: http://www.mozilla.org/

Installation
------------

**Prerequisites:**
* [git](http://git-scm.com/) of course.
* [python 2.x](http://www.python.org/)
* [virtualenv](http://www.virtualenv.org/en/latest/) (with [virtualenv wrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) recommendded)
* [lessc](http://lesscss.org/)
* [MySQL Database](http://www.mysql.com/) or other alternatives

**Steps:**

Firstly checkout source code from Github (make sure you use `--recursive`):  
```sh
$ git clone --recursive git://github.com/mozilla/bedrock.git
$ cd bedrock
```

Then create a virtualenv using virtualenv wrapper,  
so that you can install dependencies in a safe and clean environment  
without worrying about version conflict among different projects.  
```sh
$ mkvirtualenv tildeslash                    # create a virtualenv for tildeslash
$ workon tildeslash                          # change current virtualenv to tildeslash
$ pip install -r requirements/compiled.txt   # installs compiled dependencies for playdoh
$ pip install -r requirements/dev.txt        # installs test dependencies for playdoh
$ pip install -r requirements/custom.txt     # installs dependencies for tildeslash
```

If you are on OSX and some of the compiled dependencies fails to compile,  
try explicitly setting the arch flags and try again:  
```sh
$ export ARCHFLAGS="-arch i386 -arch x86_64"
$ pip install -r requirements/compiled.txt
```

Create your database, for non-ascii codeloggers, be aware of encoding settings.
```sql
CREATE DATABASE tildeslash CHARACTER SET utf8 COLLATE utf8_general_ci;
```

Copy sample local setting file:  
```sh
$ cp tildeslash/settings/local.py-dist tildeslash/settings/local.py
```
change db credentials and `HMAC_KEYS`/`SECRET_KEY`,  
give your codelog a cool title using `CODELOG_TITLE` setting.  

Load database schema and initial data with following commands:  
```sh
./manage.py syncdb
./manage.py migrate
```

If your less won't compile automatically,  
add the path to the LESS compiler (found by using `which lessc`)  
to `tildeslash/settings/local.py` with the following line:  
```python
LESS_BIN = '/path/to/lessc'
```

**Make it run:**

To make the server run, make sure you are inside a virtualenv,  
and then run the server:  
```sh
$ ./manage.py runserver
```

Let's it! Now check this URL in your browser:  
[http://localhost:8000/](http://localhost:8000/)  

Features
--------
* Powerful [Ace][ace] Markdown editor, free your hands from mouse when codelogging  
* Github flavored [fenced-code-blocks](https://help.github.com/articles/github-flavored-markdown#fenced-code-blocks)  
* Simple tag support through [django-taggit](https://github.com/alex/django-taggit)  
* Pretty date format through [django-pretty-times](https://github.com/imtapps/django-pretty-times)  
* Clean interface with [Tomorrow-night theme](https://github.com/MozMorris/tomorrow-pygments) as default  

Todos
-------
* Wordcount with asian character support  
* Responsive Design  
* RSS feed  
* L10n (Start from chinese)  
* Author profile  
* Tag cloud  
* Customized admin interface (Currently using default django admin)  
* Mobile-accessible admin interface  
* Inline image upload  

Author
------
I'm Eddie, a Web Developer located in Taipei, Taiwan  
Currently working at Mozilla  

License
-------
This software is licensed under the [New BSD License][BSD].  
For more information, read the file ``LICENSE``.  

[BSD]: http://creativecommons.org/licenses/BSD/  

