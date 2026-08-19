"""Folium heatmap over a 311 dataframe, returned as embeddable HTML.

"Show 311 complaints on Washington St" answered as a MAP beats the same
answer as a paragraph — Track B is judged on citizen usability, and
citizens think in places, not row ids.

Use from Streamlit:
    import pandas as pd, streamlit.components.v1 as components
    from track_b_experience.components.map_answer import heatmap_html
    df = pd.read_csv("data/downloads/311-service-requests.csv")
    components.html(heatmap_html(df), height=520)
"""
from __future__ import annotations

import folium
import pandas as pd
from folium.plugins import HeatMap

BOSTON_CENTER = (42.3601, -71.0589)


def heatmap_html(df: pd.DataFrame, lat_col: str = "latitude",
                 lon_col: str = "longitude", max_points: int = 5000) -> str:
    """Render a 311 dataframe as a heatmap and return the map's HTML."""
    cols = {c.lower(): c for c in df.columns}
    lat, lon = cols.get(lat_col.lower()), cols.get(lon_col.lower())
    if lat is None or lon is None:
        raise ValueError(f"Need '{lat_col}'/'{lon_col}' columns; have: {list(df.columns)[:12]}...")
    pts = (df[[lat, lon]].apply(pd.to_numeric, errors="coerce").dropna())
    # Boston's bounding box — drop the (0, 0) rows 311 exports love to include.
    pts = pts[pts[lat].between(42.2, 42.5) & pts[lon].between(-71.3, -70.8)]
    fmap = folium.Map(location=BOSTON_CENTER, zoom_start=12, tiles="cartodbpositron")
    HeatMap(pts.head(max_points).values.tolist(), radius=11, blur=14).add_to(fmap)
    return fmap.get_root().render()
