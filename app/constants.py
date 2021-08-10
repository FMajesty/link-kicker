from typing import Any


class Constants:
    """
    A base class for defining a class with a set of constants.
    Implements property "all" to get all values of constants.
    The child class attributes must be set in upper case.
    """

    value_type: Any

    @classmethod
    def all(cls) -> tuple:
        keys = [
            key
            for key, value in cls.__dict__.items()
            if isinstance(value, cls.value_type) and key.isupper()
        ]
        return tuple([getattr(cls, key) for key in keys])


class StrConstants(Constants):
    """
    A base class for defining a class with a set of string constants.

    Examples
    --------
    >>> class ExampleClass(object, metaclass=StrConstants):
    ...     FIRST = 'first'
    ...     SECOND = 'second'
    ...     THIRD = 'third'
    ...
    >>> print(ExampleClass.all())
    ... ('first', 'second', 'third')
    >>> print(ExampleClass.FIRST)
    ... 'first'
    """

    value_type = str


class IntConstants(Constants):
    """
    A base class for defining a class with a set of integer constants.

    Examples
    --------
    >>> class ExampleClass(object, metaclass=IntConstants):
    ...     FIRST = 1
    ...     SECOND = 2
    ...     THIRD = 3
    ...
    >>> print(ExampleClass.all())
    ... (1, 2, 3)
    >>> print(ExampleClass.FIRST)
    ... 1
    """

    value_type = int


class Message(StrConstants):
    READ = "🏄‍♂️ Прочитано!"
    CANCEL = "❌ Отменить"
    SAVED_LINK = "🤘 Ссылку сохранил"
    NOTHING_TO_SEND = "🍻 Все ссылочки уже прочитаны, мне нечего тебе отправить"
    NOTHING_TO_SEND_MAILING = "☹️ Мне тебе нечего отправлять в ежедневной рассылке! Давай-давай, закинь еще ссылочек"
    LINK_DELETED = "🗑 Ссылку удалил"
    LINK_WAS_READ = "🤸‍♀️ Йоу, минус одна непрочитанная ссылка!"
    F_URL = "📤 {}"
    F_URL_MAILING = "📤 Привет! Твоя ссылочка почитать на сегодня: {}"
