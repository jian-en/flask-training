import os
import jinja2

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(context)


class Foo:

    def __init__(self, a):
        self.a = a

    def somemethod(self):
        return self.a ** 2


context = {'mydict': {'key': 'template'},
           'mylist': [1, 2, 3, 4, 5],
           'myintvar': 2,
           'myobj': Foo(8),
           # 'user': 'fujian',
           'comments': {'a': 'b', 'c': 'd'}
           }

result = render('./main.j2', context)

print(result)
