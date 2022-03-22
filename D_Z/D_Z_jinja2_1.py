from jinja2 import Template

menu = [
    {"index": "Главная"},
    {"news": "Новости"},
    {"about": "О компании"},
    {"shop": "Магазин"},
    {"contacts": "Контакты"},
]
link = """
<ul>
{% for i in menu: -%}
{%  for k, v in i.items(): -%}
{% if k == "index" -%}   
    <li><a href="/{{k}}" class="active">{{v}}</a></li>
{% else -%}
    <li><a href="/{{k}}">{{v}}</a></li>
{% endif -%}
{% endfor -%}  
{% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(menu=menu)
print(msg)