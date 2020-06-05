import pprint
from enum import Enum, unique
from typing import Dict, List, Literal, Any


TextStyle: Dict[str, int] = {
    "No_effect": 0,
    "Bold": 1,
    "Underline": 2,
    "Negative1": 3,
    "Negative2": 5,
}


TextColour: Dict[str, int] = {
    "Black": 30,
    "Red": 31,
    "Green": 32,
    "Yellow": 33,
    "Blue": 34,
    "Purple": 35,
    "Cyan": 36,
    "White": 37,
}


BackgroundColour: Dict[str, int] = {
    "Black": 40,
    "Red": 41,
    "Green": 42,
    "Yellow": 43,
    "Blue": 44,
    "Purple": 45,
    "Cyan": 46,
    "White": 47,
}


def schene(ts: str = None, tc: str = None, bg: str = None) -> str:
    """
    Expected three arguments:
    . ts: text style
    . tc: text colour
    . bg: background colour
    """

    colour_set: List[str] = ['0', '37']

    if ts:
        colour_set[0] = str(TextStyle[ts])

    if tc:
        colour_set[1] = str(TextColour[tc])

    if bg:
        colour_set.insert(2, str(BackgroundColour[bg]))

    return ";".join(colour_set)


@unique
class ColourMsg(Enum):

    __order__ = "INFO, SUCCESS, FINISH, WARNING, FAIL, ENDC"

    INFO: str = '\033[%sm' % (schene("Bold", "Cyan"))
    SUCCESS: str = '\033[%sm' % (schene("Bold", "Green"))
    FINISH: str = '\033[%sm' % (schene("Bold", "White"))
    WARNING: str = '\033[%sm' % (schene("Bold", "Yellow"))
    FAIL: str = '\033[%sm' % (schene("Bold", "White", "Red"))
    ENDC: str = '\033[0m'

    @staticmethod
    def get(value):
        """
        Get a single valid item of ColourMsg enum.
        """

        if ColourMsg[value.upper()]:
            return ColourMsg[value.upper()]
        else:
            raise TypeError

    @staticmethod
    def list_all() -> List[Any]:
        """
        List all items of ColourMsg enum.
        """

        return list(map(lambda c: c, ColourMsg))


def show() -> None:
    """
    List all message types.
    """

    for item in ColourMsg:
        if item.name != "ENDC":
            cmsg(item.name.capitalize(), item.name)


def cmsg(message: str, msg_type: str) -> None:
    """
    Print a styled message.
    """

    item = ColourMsg.get(msg_type)
    assert item in ColourMsg.list_all()
    print("{}[ {} ]\033[0m \t{}".format(
        item.value,
        item.name,
        message))


if __name__ == '__main__':
    show()

