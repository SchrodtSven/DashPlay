from dash import Dash, dcc, html, Input, Output, ctx, register_page, callback
import pandas as pd
import plotly.express as px
from dp.dd import DD 

df_o = pd.read_csv("dta/sessions.csv")
df = df_o[["date", "sess_ctry", "sess_loc", "sessions", "lng", "lat", "iso"]]

# df = pd.read_csv("exporte/sess_loc_non_DE.csv")
# df.to_csv("volcano.csv", index=False)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

str_proj = "natural earth"
register_page(__name__)

fig = px.scatter_geo(
    data_frame=df,
    lat="lat",
    lon="lng",
    size="seess_inst",
    hover_name="sess_loc",
    projection=str_proj,
)


layout = html.Div(
    [
        html.H3(
            "Geo data game",
        ),
        html.Div(
            className="custom-dropdown-style",
            children=[
                dcc.Dropdown(
                    id="geo-dd",
                    options=DD.proj,
                    value=str_proj,
                    multi=False,
                    className="dropdown-class",
                    style={"background-color": "#011213"},
                )
            ],
        ),
        dcc.Graph(id="geo-map", figure=fig),
    ],
    style={"margin": 10, "maxWidth": "500px"},
)


@callback(Output("geo-map", "figure"), Input("geo-dd", "value"))
def sync_input(loc):
    print(loc)
    return px.scatter_geo(
        data_frame=df,
        lat="lat",
        lon="lng",
        size="sessions",
        hover_name="sess_loc",
        projection=loc,
        # scope="europe"
    )
