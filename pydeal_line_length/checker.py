import math
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker


class PydealLineLengthChecker(BaseChecker):
    __implements__ = IRawChecker

    name = "pydeal_line_length"
    msgs = {
        "W2201": (
            "Line too long (%d > %d)",
            "pydeal-line-too-long",
            "Lines must be short enough to fit on an appropriately-rotated programmer's monitor.",
        ),
        "W2202": (
            "File too long",
            "pydeal-file-too-long",
            "Some lines of the file won't be able to fit on a single monitor.",
        ),
    }
    options = (
        (
            "first-line-length",
            {
                "default": 120,
                "type": "int",
                "metavar": "cols",
                "help": "Length of the first (longest) line",
            },
        ),
        (
            "monitor-angle-degrees",
            {
                "default": 22,
                "type": "float",
                "metavar": "degrees",
                "help": "Angle that the target monitor is rotated from horizontal.",
            },
        ),
    )

    def process_module(self, node: nodes.Module) -> None:
        angle_rad = self.config.monitor_angle_degrees * 180.0 / math.pi
        slope = abs(math.tan(angle_rad))
        if slope > 1.0:
            slope = 1.0 / slope
        max_line_length = self.config.first_line_length

        with node.stream() as stream:
            for (lineno, line) in enumerate(stream, start=1):
                # TODO: This counts bytes not characters
                line_length = len(line.rstrip(b"\r\n"))
                if max_line_length <= 0:
                    self.add_message(
                        "pydeal-file-too-long",
                        line=lineno,
                    )
                    break
                if line_length > max_line_length:
                    self.add_message(
                        "pydeal-line-too-long",
                        line=lineno,
                        args=(line_length, max_line_length),
                    )
                max_line_length -= slope


def register(linter):
    linter.register_checker(
        PydealLineLengthChecker(linter)
    )
