"""
also does event filtering to get a reasonable date range (today - ~2 weeks from now)
"""

import json
from datetime import datetime, timedelta

import pandas as pd

today = datetime.today()


def _filter_current(df):
    def _in_range(date):
        return (date >= today) & (date <= today + timedelta(14))

    return df[_in_range(df['date'])]


def _format_dates(dates):
    return dates.dt.strftime("%d.%m")


iwenciki = _filter_current(pd.read_csv('iwenciki.csv', dtype=str).astype({"date": "datetime64[s]"}))
iwenciki["date"] = _format_dates(iwenciki["date"])
iwenciki = iwenciki.to_dict('records')
with open('iwenciki.json', 'w') as f:
    json.dump({"event_list": iwenciki}, f, indent=2)