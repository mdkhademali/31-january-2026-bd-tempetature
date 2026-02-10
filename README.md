## Division-wise Temperature Mapping of Bangladesh using GeoPandas

This project demonstrates how to create division-level thematic maps of **maximum** and **minimum temperature** for Bangladesh using **Python**, **GeoPandas**, and **Matplotlib**. Spatial data (GeoJSON) is merged with tabular temperature data to visualize spatial temperature variation across the country.

---

## Project Objectives
- Visualize division-wise temperature distribution in Bangladesh
- Demonstrate attribute joining between GeoJSON and tabular data
- Create side-by-side choropleth maps using GeoPandas
- Provide a simple, practical GIS + Python example for students and beginners

---

## Output
- **Maximum Temperature (°C)** — 31 January
- **Minimum Temperature (°C)** — 31 January
- Division names labeled at polygon centroids
- Two thematic maps displayed side-by-side using different color scales

---


## Requirements
Python 3.8 or higher is recommended.

```bash
pip install geopandas pandas matplotlib
```

**Note:** Installing GeoPandas may require GDAL, Fiona, and PyProj dependencies. Using **Anaconda** is recommended for easier setup.

---

## Data Description

### 1️. Spatial Data
- **File:** `bangladesh_divisions.json`
- **Format:** GeoJSON
- **Key Attribute:** `name` (Division name)

### 2️. Temperature Data
The temperature values are hard-coded for demonstration purposes.

| Division       | MaxTemp (°C) | MinTemp (°C) |
|---------------|--------------|--------------|
| Barisal       | 28           | 17           |
| Chittagong    | 30           | 17           |
| Dhaka         | 27           | 13           |
| Khulna        | 28           | 15           |
| Rajshahi      | 29           | 14           |
| Rangpur       | 28           | 13           |
| Sylhet        | 25           | 14           |
| Mymensingh    | 27           | 15           |

---

## Methodology / Workflow
1. Load the Bangladesh division boundaries from a GeoJSON file
2. Create a Pandas DataFrame containing temperature data
3. Merge spatial and tabular data using division names
4. Generate side-by-side choropleth maps for maximum and minimum temperature
5. Add division name labels using polygon centroids

---

## Learning Outcomes
- Handling spatial data with GeoPandas
- Performing attribute joins between spatial and non-spatial datasets
- Creating choropleth maps in Python
- Integrating GIS concepts with data visualization

---

## Future Improvements
- Use real meteorological datasets (e.g., BMD, ERA5, NOAA)
- Add time-series or seasonal temperature analysis
- Extend the analysis to district or upazila level
- Create interactive web maps using Folium or Plotly

© mdkhademali