"""
We want to create an object with methods for various HTML elements: div, p, span and h1 for the sake of this Kata.

These methods will wrap the passed-in string in the tag associated with each.

format.div("foo")  # returns "<div>foo</div>"
format.p("bar")  # returns "<p>bar</p>"
format.span("fiz")  # returns "<span>fiz</span>"
format.h1("buz")  # returns "<h1>buz</h1>"
We also want to be able to add additional formatting by chaining our methods together.

format.div.h1("FooBar")
# "<div><h1>FooBar</h1><div>"

format.div.p.span("FizBuz")
# "<div><p><span>FizBuz</span></p></div>"
and so on, as deep as we care to use.

Multiple arguments should be concatenated and wrapped in the correct HTML formatting.

format.div.h1("Foo", "Bar")
# "<div><h1>FooBar</h1></div>"
We should be able to store the created methods and reuse them.

wrap_in_div = format.div
wrap_in_div("Foo")    # "<div>Foo</div>"
wrap_in_div.p("Bar")  # "<div><p>Bar</p></div>"

wrap_in_div_h1 = format.div.h1
wrap_in_div_h1("Far")  # "<div><h1>Far</h1></div>"
wrap_in_div_h1.span("Bar")  # "<div><h1><span>Bar</span></h1></div>"
And finally, we should be able to nest calls.

format.div(
    format.h1("Title"),
    format.p(f"Paragraph with a {format.span('span')}.")
)
# returns "<div><h1>Title</h1><p>Paragraph with a <span>span</span>.</p></div>"
"""

class Format:

    def __init__(self, tags=None):
        if tags is None:
            self.tags = []
        else:
            self.tags = tags

    def __getattr__(self, tag):
        tags_atuais = self.tags
        novas_tags = tags_atuais + [tag]
        return self.__class__(tags=novas_tags)

format = Format()

nova_div = format.div.h1

print(nova_div.tags)