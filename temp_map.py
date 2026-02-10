import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# ১) Load the GeoJSON
gdf = gpd.read_file("bangladesh_divisions.json")

# ২) Temperature data — make sure names match GeoJSON 'name' property
temperature_data = {
    "Division": ["Barisal", "Chittagong", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Sylhet", "Mymensingh"],
    "MaxTemp": [28, 30, 27, 28, 29, 28, 25, 27],
    "MinTemp": [17, 17, 13, 15, 14, 13, 14, 15]
}
temp_df = pd.DataFrame(temperature_data)

# ৩) Merge on the matching name field
gdf = gdf.merge(temp_df, left_on="name", right_on="Division", how="left")

# ৪) Plot side‑by‑side
fig, axes = plt.subplots(1, 2, figsize=(18, 10))

gdf.plot(column='MaxTemp', cmap='hot', linewidth=0.8, edgecolor='black', legend=True, ax=axes[0])
axes[0].set_title("Maximum Temperature (°C) — 31 January")
axes[0].axis('off')

gdf.plot(column='MinTemp', cmap='cool', linewidth=0.8, edgecolor='black', legend=True, ax=axes[1])
axes[1].set_title("Minimum Temperature (°C) — 31 January")
axes[1].axis('off')

# Add labels at centroids
for ax in axes:
    for idx, row in gdf.iterrows():
        if pd.notna(row["MaxTemp"]):
            plt.text(row.geometry.centroid.x, row.geometry.centroid.y, row["name"],
                     horizontalalignment="center", fontsize=9)

plt.tight_layout()
plt.show()