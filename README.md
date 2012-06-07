Django-Next-Please
==================

Provides a simple decorator to add to **TemplateRepsonse** views to provide pagination.

Django-Next-Please is easier to setup than [Django-Paginagtion](https://github.com/ericflo/django-pagination) and helps you to avoid those [ugly class based views](http://lukeplant.me.uk/blog/posts/djangos-cbvs-were-a-mistake/).

Installation
------------
```
pip install Django-Next-Please
```

Usage
------

**In your view:**
```python
from NextPlease import pagination

@pagination('latest_news')
def topic_front (request, slug):
  topic = get_object_or_404(Topic, slug=slug)
  
  c = {
    'topic': topic,
    'latest_news': NewsItem.published.filter(topics__topic=topic),
  }
  return TemplateResponse(request, 'taxo/topic_front.html', c)
```


**In your template:**
```html
<ul>
  {% for n in paginator.current_list %}
  <li>{{ n.headline }}</li>
  {% endfor %}
</ul>
<div>
  {% if paginator.has_previous %}<a href="?{{ paginator.previous_qs }}">&lt; Previous</a> | {% endif %}
  Page {{ paginator.number }}
  {% if paginator.has_next %} | <a href="?{{ paginator.next_qs }}">Next &gt;</a>{% endif %}
</div>
```

Options
-------
```
pagination(
  object_list_var,
  per_page=PER_PAGE,
  page_param='page',
  output_var='paginator',
  orphans=0,
  allow_empty_first_page=True
)
```

**Required:**

object\_list\_var: Context variable name that contains the data to be paginated.


**Optional:**

per\_page: Defaults to 10, override globally with settings.PER\_PAGE

page\_param: Defaults to _page_, the request query string parameter used to determine the current page.

output\_var: Defaults to _paginator_, context variable the pagination will be in.

orphans: See https://docs.djangoproject.com/en/1.4/topics/pagination/#s-optional-arguments

allow\_empty\_first\_page: See https://docs.djangoproject.com/en/1.4/topics/pagination/#s-optional-arguments

More Info
---------

Django Next Please is based off the [Django Paginator Class](https://docs.djangoproject.com/en/1.4/topics/pagination/).  The Next Please paginator class adds the following methods.

**def current (self)**

Returns the current page object.


**def current_list (self)**

Returns an object list for the current page.


**def number (self):**

Returns the current page number.


**def has_previous (self)**

Returns True if the current page has a page before it.


**def has_next (self)**

Returns True if the current page has a page after it.


**def previous_qs (self)**

Returns a query string for the previous page.


**def next_qs (self)**

Returns a query string for the next page.

