from calendar import monthrange
from dataclasses import dataclass
from datetime import date


@dataclass(order=True)
class Month:
    year: int
    month: int

    def __str__(self):
        return f"{self.year}-{self.month:02}"

    @property
    def first_day(self):
        return date(self.year, self.month, 1)

    @property
    def last_day(self):
        weekday_of_first_date, last_date = monthrange(self.year, self.month)
        return date(self.year, self.month, last_date)
