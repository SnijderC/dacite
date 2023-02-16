from dataclasses import dataclass
from datetime import datetime

import freezegun
from dacite import Config, from_dict
from dateutil.parser import isoparse


@dataclass
class Order:
    creation: datetime


def test_datetime_without_freezing():
    now = datetime.now()
    data = {"creation": f"{now}"}
    order = from_dict(Order, data, config=Config(type_hooks={datetime: isoparse}, check_types=True))
    assert order.creation == now


@freezegun.freeze_time("2022-02-16T15:22:00.000")
def test_datetime_with_freezing():
    now = datetime.now()
    data = {"creation": f"{now}"}
    order = from_dict(Order, data, config=Config(type_hooks={datetime: isoparse}, check_types=True))
    assert order.creation == now
