# Python Option
Implementation of Scala Option in Python.

```python
    from option import Option, none, _

    # return option value if it's not empty
    val1 = 1
    opt1 = Option(val1)
    print("value is", opt1.get_or_else("hello"))

    # if Option1 is empty return Option2
    opt2 = Option(1.2)
    opt3 = none.or_else(opt2)
    print(opt3)

    # fold == map + get_or_else
    opt4 = opt3.fold(8, lambda v: v*2)
    opt4_alt = opt3.map(lambda v: v*2).get_or_else(8)
    print(opt4, "==", opt4_alt)

    # map and flat_map
    opt5 = Option("hello")
    print(opt5.flat_map(lambda v: Option(v * 2)))  # Some('hellohello')
    print(opt5.map(lambda v: v * 2))  # Some('hellohello')

    # zip options, convert to list
    opt6 = Option("hi").zip(Option('xx'))
    print(list(opt6))

    # Using underscore object:
    class MyObj:
        hello = "hi"

        def bye(self):
            return "see you"
    opt7 = Option(MyObj())
    print(opt7.fold("", _.hello))  # hi
    print(opt7.fold("", _.bye))  # see you
    print(Option(9).fold(0, 2 * _))  # 18

    # filter option value
    print(Option(9).filter(_ > 50).get_or_else(0))  # 0
```

# See also
- [Is there a Python equivalent for Scala's Option or Either?](https://stackoverflow.com/q/22992433)
- _returns_ [Maybe container](https://github.com/dry-python/returns?tab=readme-ov-file#maybe-container)
