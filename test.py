from dash import Dash, html, dcc, callback_context, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd

# Sample data for the table
data = pd.DataFrame({
    "Column 1": ["A", "B", "C"],
    "Column 2": [1, 2, 3],
    "Column 3": ["X", "Y", "Z"]
})

app = Dash(__name__, external_stylesheets=[
    "https://cdn.tailwindcss.com",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
    "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap"
])

# Initial scatter plot data
scatter_data = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    mode="markers",
    marker=dict(size=10, color="blue")
)

# App layout
app.layout = html.Div(className="flex h-screen bg-gray-100 font-inter", children=[
    # Sidebar (left out for brevity, same as above)
    
    # Main Content
    html.Div(className="flex-1 p-6", children=[
        # Analysis Content
        html.Div(className="bg-white p-6 rounded-lg shadow", children=[
            html.H1("Analysis", className="text-2xl font-semibold mb-4"),

            # Scatter Plot with click event
            html.Div(className="bg-gray-100 p-6 rounded-lg", children=[
                html.H2("Key Drivers", className="text-lg font-semibold mb-4"),
                dcc.Graph(
                    id="scatter-plot",
                    figure=go.Figure(data=[scatter_data]),
                    config={"displayModeBar": False}
                )
            ])
        ]),
        
        # Modal for displaying data on click
        dbc.Modal(
            id="popup-modal",
            is_open=False,
            children=[
                dbc.ModalHeader("Data Table"),
                dbc.ModalBody([
                    html.Div(id="data-table-placeholder")
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-modal", className="ml-auto")
                )
            ]
        )
    ])
])

# Callback to open modal and populate with data when a point is clicked
@app.callback(
    [Output("popup-modal", "is_open"), Output("data-table-placeholder", "children")],
    [Input("scatter-plot", "clickData"), Input("close-modal", "n_clicks")],
    [State("popup-modal", "is_open")]
)
def display_data_on_click(click_data, close_click, is_open):
    ctx = callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # If a point is clicked, open modal and populate with data
    if triggered_id == "scatter-plot" and click_data:
        # Retrieve information from the clicked point (e.g., x and y values)
        x_value = click_data["points"][0]["x"]
        y_value = click_data["points"][0]["y"]

        # Create placeholder data table based on click (sample table here)
        table = dbc.Table.from_dataframe(data, striped=True, bordered=True, hover=True)
        
        return True, table
    
    # Close modal if close button is clicked
    elif triggered_id == "close-modal":
        return False, None

    return is_open, None

if __name__ == "__main__":
    app.run_server(debug=True)
