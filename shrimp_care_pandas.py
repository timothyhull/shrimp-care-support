#!/usr/bin/env python3
""" Constants values for Shrimp Care Pandas DataFrame. """

# Imports - Third-Party
import pandas as pd

# Imports - Local
import constants as con

# Create a Pandas DataFrame object
df = pd.DataFrame(
    {
        "inventory": con.INVENTORY,
        "crab_affection": con.CRAB_AFFECTION,
        "crab_nutrition": con.CRAB_NUTRITION,
    }
)

# Replace the default numeric indices with the "inventory" values
df.set_index(
    keys="inventory",
    inplace=True
)
