from typing import Any

def bind_to_self(method):
    """
    Takes method(self, arg) and converts to method(arg)(obj).
    Binds obj to self argument.
    """
    def wrapped(_, *args):
        def caller(*obj):
            return method(*obj, *args)
        return caller
    return wrapped

class underscore:
    @bind_to_self
    def __getattr__(self, attr) -> Any:
        res = getattr(self, attr)
        return res() if callable(res) else res

    def __call__(self, obj):
        return obj

    @bind_to_self
    def __mul__(self, value):
        return self * value

    @bind_to_self
    def __rmul__(self, value):
        return value * self

    @bind_to_self
    def __neg__(self):
        return -self

    @bind_to_self
    def __pos__(self):
        return +self

    @bind_to_self
    def __sub__(self, value):
        return self - value

    @bind_to_self
    def __rsub__(self, value):
        return value - self

    @bind_to_self
    def __add__(self, value):
        return self + value

    @bind_to_self
    def __radd__(self, value):
        return value + self

    @bind_to_self
    def __truediv__(self, value):
        return self / value

    @bind_to_self
    def __rtruediv__(self, value):
        return value / self

    @bind_to_self
    def __floordiv__(self, value):
        return self // value

    @bind_to_self
    def __rfloordiv__(self, value):
        return value // self

    @bind_to_self
    def __xor__(self, value):
        return self ^ value

    @bind_to_self
    def __rxor__(self, value):
        return value ^ self

    @bind_to_self
    def __or__(self, value):
        return self | value

    @bind_to_self
    def __ror__(self, value):
        return value | self

    @bind_to_self
    def __and__(self, value):
        return self & value

    @bind_to_self
    def __rand__(self, value):
        return value & self

    @bind_to_self
    def __lshift__(self, value):
        return self << value

    @bind_to_self
    def __rlshift__(self, value):
        return value << self

    @bind_to_self
    def __rshift__(self, value):
        return self >> value

    @bind_to_self
    def __rrshift__(self, value):
        return value >> self

    @bind_to_self
    def __pow__(self, value):
        return self ** value

    @bind_to_self
    def __rpow__(self, value):
        return value ** self

    @bind_to_self
    def __mod__(self, value):
        return self % value

    @bind_to_self
    def __rmod__(self, value):
        return value % self

    @bind_to_self
    def __matmul__(self, value):
        return self @ value

    @bind_to_self
    def __rmatmul__(self, value):
        return value @ self

    @bind_to_self
    def __invert__(self):
        return ~self

    @bind_to_self
    def __lt__(self, value):
        return self < value

    @bind_to_self
    def __le__(self, value):
        return self <= value

    @bind_to_self
    def __eq__(self, value):
        return self == value

    @bind_to_self
    def __ne__(self, value):
        return self != value

    @bind_to_self
    def __gt__(self, value):
        return self > value

    @bind_to_self
    def __ge__(self, value):
        return self >= value

_ = underscore()
