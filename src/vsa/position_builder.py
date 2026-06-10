from .music import MusicalPosition
from .ast import ScopeNode


class PositionBuilder:
    def __init__(self, document):
        self.document = document

    def build(self):
        result = []

        for node in self.document.nodes:
            if not isinstance(node, ScopeNode):
                continue

            hm = node.height_modifier or ["~"]
            lm = node.length_modifier or ["~"]

            if len(hm) > 1 and len(lm) == 1:
                lm = lm * len(hm)

            if len(lm) > 1 and len(hm) == 1:
                hm = hm * len(lm)

            for ehm, elm in zip(hm, lm):
                result.append(
                    MusicalPosition(
                        text=node.text,
                        ehm=ehm,
                        elm=elm,
                    )
                )

        return result
