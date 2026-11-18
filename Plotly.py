import plotly.express as px
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [12000, 15000, 18000, 22000, 25000],
    "Region": ["North", "South", "North", "South", "North"]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Month",
    y="Sales",
    color="Region",
    title="Interactive Sales Dashboard",
    hover_data=["Region"]
)

fig.show()