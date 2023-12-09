import pandas as pd
from ydata_profiling import ProfileReport
import os

if not os.path.exists('../profiling'):
    os.mkdir('../profiling')

columns = ["cap-shape", "cap-surface", "cap-color", "bruises?", "odor", "gill-attachment", "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", "veil-type", "veil-color", "ring-number", "ring-type", "spore-print-color", "population", "habitat"]

df = pd.read_csv('../data/agaricus-lepiota.data', names=columns,
                              sep=', ', engine='python')

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("../profiling/report.html")