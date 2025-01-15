from option.option_cls import Option, none
from option.underscore import _
# from typing import Callable, Generic, TypeVar, cast

# A = TypeVar('A')
# B = TypeVar('B')


# class Option(Generic[A]):
#     "Represents optional values."

#     def __init__(self, value: A | None):
#         self.value = value

#     @property
#     def is_defined(self):
#         "Returns False if the option is None, True otherwise."
#         return self.value is not None

#     @property
#     def is_empty(self):
#         "Returns True if the option is None, False otherwise."
#         return self.value is None

#     @property
#     def non_empty(self):
#         "Returns False if the option is None, True otherwise."
#         return self.value is not None

#     def or_else(self, alternative: "Option[B]"):
#         "Returns this Option if it is nonempty, otherwise return `alternative`."
#         return self if self.value is not None else alternative

#     def get_or_else(self, default: B):
#         """
#         Returns the option's value if the option is nonempty,
#         otherwise return `default`.
#         """
#         v = self.value
#         return v if v is not None else default

#     def get(self):
#         "Return value, throw exception if empty."
#         v = self.value
#         if v is None:
#             raise ValueError("Option is empty")
#         return v

#     def fold(self, if_empty: B, f: Callable[[A], B]):
#         """
#         Returns the result of applying `f` to this Option's value
#         if the Option is nonempty.
#         """
#         v = self.value
#         return f(v) if v is not None else if_empty

#     def map(self, f: Callable[[A], B]):
#         """
#         Returns an Option containing the result of applying `f` to this
#         Option's value if this Option is nonempty.
#         """
#         v = self.value
#         return Option(f(v)) if v is not None else cast(Option[B], self)

#     def flat_map(self, f: "Callable[[A], Option[B]]"):
#         """
#         Returns the result of applying `f` to this Option's value if this scala.Option is nonempty.
#         """
#         v = self.value
#         return f(v) if v is not None else cast(Option[B], self)

#     def for_each(self, f: "Callable[[A], None]"):
#         """
#         Apply the given procedure `f` to the option's value, if it is nonempty.
#         """
#         v = self.value
#         if v is not None:
#             f(v)

#     def filter(self, p: "Callable[[A], bool]") -> "Option[A]":
#         """
#         Returns this Option if it is nonempty and applying the predicate `p`
#         to this Option's value returns True.
#         """
#         v = self.value
#         return self if v is not None and p(v) else Option(None)

#     def filter_not(self, p: "Callable[[A], bool]") -> "Option[A]":
#         """
#         Returns this Option if it is nonempty and applying the predicate `p`
#         to this Option's value returns False.
#         """
#         v = self.value
#         return self if v is not None and not p(v) else Option(None)

#     def exists(self, p: "Callable[[A], bool]"):
#         """
#         Returns True if this option is nonempty and the predicate `p` returns
#         True when applied to this Option's value.
#         """
#         v = self.value
#         return v is not None and p(v)

#     def for_all(self, p: "Callable[[A], bool]"):
#         """
#         Returns True if this option is empty or the predicate `p` returns True
#         when applied to this Option's value.
#         """
#         v = self.value
#         return v is None or p(v)

#     def contains(self, elem: B):
#         "Tests whether the option contains a given value as an element."
#         return self.value == elem if elem is not None else False

#     def zip(self, that: "Option[B]") -> "Option[tuple[A, B]]":
#         """
#         Returns an Option formed from this option and another option by
#         combining the corresponding elements in a tuple.
#         """
#         v = self.value
#         v2 = that.value
#         if v is None or v2 is None:
#             return Option(None)
#         return Option((v, v2))

#     def unzip(self):
#         """
#         Converts an Option of a tuple into an Option of the first element and
#         an Option of the second element.
#         """
#         v = self.value
#         if not isinstance(v, tuple) or len(v) != 2:
#             raise ValueError("Option does not contain a tuple of length 2")
#         return Option(v[0]), Option(v[1])

#     def to_list(self):
#         """
#         Returns a list containing the Option's value if it is nonempty,
#         or the empty list if the Option is empty.
#         """
#         v = self.value
#         return [v] if v is not None else []

#     def __iter__(self):
#         v = self.value
#         if v:
#             yield v

#     def __repr__(self):
#         return f"Option({repr(self.value)})"


# if __name__ == '__main__':
#     # v = 1
#     # o = Option(v)
#     # x = o.get_or_else("hello")

#     # o2 = Option(1.2)
#     # x2 = o.or_else(o2)

#     # x3 = x2.fold(8, lambda v: v*2)
#     # print(x3)

#     # print(Option("hello").flat_map(lambda v: Option(v * 2)))
#     # print(Option("hello").map(lambda v: v * 2))
#     o = Option("hi").zip(Option('xx'))
#     print(
#         o
#     )
#     print(list(o))
