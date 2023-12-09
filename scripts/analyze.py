import os
import pandas as pd
import matplotlib.pyplot as plt

if not os.path.exists('../results'):
    os.mkdir('../results')

columns = ["cap-shape", "cap-surface", "cap-color", "bruises?", "odor", "gill-attachment", "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", "veil-type", "veil-color", "ring-number", "ring-type", "spore-print-color", "population", "habitat"]

df = pd.read_csv('../data/agaricus-lepiota.data', names=columns,
                              sep=',', engine='python')

odor_map = {
    "a": "almond",
    "l": "anise",
    "c": "creosote",
    "y": "fishy",
    "f": "foul",
    "m": "musty",
    "n": "none",
    "p": "pungent",
    "s": "spicy"
}
df["odor"].map(odor_map)

df['odor'].map(odor_map).value_counts().plot(kind='bar', figsize=(8, 6))
plt.title("Mushroom Odor Type Frequency Graph")
plt.xticks(rotation=20)
plt.savefig("../results/odor.png")