# Work at Olist

This is an implementation of the [Work at Olist Assignment](https://github.com/olist/work-at-olist).


# Steps

1. Work Environment
2. Import Categories
3. Database Idea
4. API Documentation


# 1.Work Environment

OS - MACOS
IDE - Sublime3 
Run on Terminal BASH

Libraries:
- Those on requirements [README](requirements/production.txt)
- [HTML5 Boilerplate for Django](https://github.com/mattsnider/django-html5-boilerplate) - This is used to provide a good HTML5 template
- [Bootstrap](http://getbootstrap.com/)
- Whitenoise for staticfiles correct loading as in [REST Django Framework DOC](https://devcenter.heroku.com/articles/django-assets)


#2. Import Categories 

This is a *Django Management Command* to import the channels' categories from a CSV(Comma Separated Values) File. 
- The command should receive 2 arguments: channel name (create the channel if it doesn't exists in database) and the name of `.csv` file:

```
$ python manage.py importcategories walmart categories.csv
```

#3 Database Idea

Database was developed with the idea of **CLOSURE TABLEs**. Each Category references all its Ancestors and Descendants as Itself. This make life easy to manage a Tree Like Database as this one. 

#4 API Documentation

Using the GET METHOD, Its possible to get database elements in JSON Representation. The struture is as follows:

- URLS
  - /channels : return a list of Channels
  - /channels/<channel_name> : return a list of <channel_name> Categories
  - /channels/<channel_name>/<category>: return a list of Parent Directories and Subdirectories of the specified <category>
  Example:
``` 
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "subcategories": [
        {
            "id": 2,
            "name": "National Literature",
            "slug": "national-literature",
            "categoryChannel": {
                "id": 1,
                "name": "walmart"
            }
        },
        {
            "id": 3,
            "name": "Science fiction",
            "slug": "science-fiction",
            "categoryChannel": {
                "id": 1,
                "name": "walmart"
            }
        }
    ],
    "parents": [
        {
            "id": null,
            "name": null,
            "slug": null,
            "categoryChannel": null
        }
    ]
}
```

#[serializers.py](work-at-olist/work-at-olist/olistconnect/serializers.py) - This file contains the serialize methods that serializes our Models to a REST Architeture format, in this case, JSON format.





