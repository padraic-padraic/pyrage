from __future__ import annotations


class Identity:
    @classmethod
    def generate(cls) -> Identity:
        ...

    @classmethod
    def from_str(cls) -> Identity:
        ...

    def to_public(self) -> Recipient:
        ...


class Recipient:
    @classmethod
    def from_str(cls) -> Recipient:
        ...
