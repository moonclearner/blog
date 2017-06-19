# Blog for django

![blog](https://github.com/moonclearner/blog/blob/master/markdownimage/QQ%E6%88%AA%E5%9B%BE20170429195835.png?raw=true)

## requirement
- django 1.9.5 or up
- markdown2
- pygments
- django-uuslug
- pytz
- Pillow

## example
It run on tencent server ubuntu 14.04 my blog site: **moonclearner.cn**
- first need init ngnix service(had provided ngnix conf)
- cd blog/
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py collectstaic
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

### 2017/5/18 星期四 9:41:04
- version 1.0 finished
- next version
	- change markdown paser
	- change pagination use ListView
### 2017/5/18 星期四 22:05:02
![pic](https://github.com/moonclearner/blog/blob/master/markdownimage/add%20some%20label.png?raw=true)
mainly add some function for search article
change markdown paser method and change model of article

### 2017/5/19 星期五 19:43:49
![pic](https://github.com/moonclearner/blog/blob/master/markdownimage/QQ%E6%88%AA%E5%9B%BE20170519154814.png?raw=true)
- add real time show markdown when writing markdown
- change writing css to bootstrap
- next target:
	- add Rss function
	- add archive
	- add search

### 2017/5/21 星期日 22:26:50
**web app deploy in server has an problem: admin manage page no css, cannot load css file**
Solution:
```markdown
1. set STATIC_ROOT
	STATIC_ROOT and STATICFILES_DIRS cannot has same dir look for my setting.py
2. python manange collectstaic
	add admin css js to your STATIC_ROOT
```

### 2017/5/22 星期一 22:18:28
BUG:
- category or paper title cannot have space
- manytomanyfields save has BUG, cannot save modification or new writing

### 2017/5/23 星期二 22:56:09
have solve yesterday BUG :)

### 2017/5/30 星期二 16:03:31
Because The Dragon Boat Festival and My job, I cannot update frequently recently sorry :)
- restore writing new article cannot load mult tag
- restore some font color

TODO:
- response formula
- scroll to display like PPT via [site](http://www.dowebok.com/77.html)

### 2017/5/31 星期三 21:52:27
- scroll to display like ppt  OK!
- response formula OK!

TODO:
- response web

### 2017/6/19 星期一 11:53:30
- swtich my databases to postgresql and redis for cache

## license
WTFPL
