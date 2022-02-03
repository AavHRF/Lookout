from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=False)
class Region:
    name: str
    wfe: str
    numnations: int
    delegate: Optional[str]
    founder: Optional[str]
    delegate_votes: Optional[int]
    embassies: List[str]
    update_time: int
    exec_founder: bool
    exec_delegate: bool
    _founderless: bool
    _passworded: bool
    _minorup: str
    _majorup: str

    @property
    def no_delegate(self) -> bool:
        return self.delegate is None

    @property
    def valid_target(self) -> bool:
        return True if(self.exec_founder is False
                       or self.exec_delegate is True
                       or self._founderless is True) and self._passworded is True else False

    @property
    def founderless(self) -> bool:
        return self._founderless

    @founderless.setter
    def founderless(self, value: bool):
        self._founderless = value

    @property
    def passworded(self) -> bool:
        return self._passworded

    @passworded.setter
    def passworded(self, value: bool):
        self._passworded = value

    @property
    def minorup(self) -> str:
        return self._minorup

    @minorup.setter
    def minorup(self, value: str):
        self._minorup = value

    @property
    def majorup(self) -> str:
        return self._majorup

    @majorup.setter
    def majorup(self, value: str):
        self._majorup = value
