# Blog for django

![blog](https://github.com/moonclearner/blog/blob/master/markdownimage/QQ%E6%88%AA%E5%9B%BE20170429195835.png?raw=true)

## requirement
- django 1.10.5
- markdown2 2.3.3
- pygments 2.2.0

## example
It run on tencent server ubuntu 14.04 my blog site: **moonclearner.cn**
- first need init ngnix service(had provided ngnix conf)
- cd blog/
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- uwsgi --ini myweb_uwsgi.ini

## change log

### 2017/5/1 星期一 22:29:08
- alter admin show image of category
	![admin list](https://raw.githubusercontent.com/moonclearner/blog/master/markdownimage/alteradmin.png)
- add markdown editor
	![markdowneditor](https://raw.githubusercontent.com/moonclearner/blog/master/markdownimage/markdown.png)
	![markdownprevie](https://raw.githubusercontent.com/moonclearner/blog/master/markdownimage/markdownPreview.png)

### 2017/5/16 星期二 21:47:55
- alter css error
	markdown writing

## license
WTFPL
