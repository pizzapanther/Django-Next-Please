Django-Next-Please
==================

Provides a simple decorator to add to **TemplateRepsonse** views to provide pagination.

Django-Next-Please is easier to setup than Django-Paginagtion and helps you to avoid those [ugly class based views](http://lukeplant.me.uk/blog/posts/djangos-cbvs-were-a-mistake/).

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
