import sys
from pathlib import Path

import pandas as pd

new_iwenciki = pd.read_csv(sys.argv[1], dtype=str)
new_iwenciki.to_csv("iwenciki.csv", mode="a", header=False, index=False)
Path(sys.argv[1]).unlink()