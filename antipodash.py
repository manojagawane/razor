from dash import Dash, html, dcc
import dash_bootstrap_components as dbc  # Optional for additional styling
import plotly.express as px
import plotly.graph_objs as go

app = Dash(__name__, 
           external_scripts=[
                "https://cdn.tailwindcss.com"
                    ],
            external_stylesheets=[
                "https://cdn.tailwindcss.com",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
                'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap'
                    ]
)



app.layout = html.Div(className="flex h-screen bg-gray-100 font-inter", children=[
    # Sidebar
    html.Div(className="w-64 bg-white border-r", children=[
        html.Div(className="p-4", children=[
            html.Div(className="flex items-center", children=[
                html.I(className="fas fa-bars mr-2"),
                html.Span("Razor-Group Supply Chain & Logistics", className="font-semibold")
            ])
        ]),
        html.Nav(className="mt-4", children=[
            html.A("Dashboard", href="#", className="flex items-center p-4 text-gray-700 hover:bg-gray-200 border-l-4 border-green-500"),
            html.A("PO Recommendation", href="#", className="flex items-center p-4 text-gray-700 bg-gray-200 border-l-4"),
            html.A("Budget Approved", href="#", className="flex items-center p-4 text-gray-700 hover:bg-gray-200"),
            html.A("Budget Awaiting", href="#", className="flex items-center p-4 text-gray-700 hover:bg-gray-200"),
            html.A("History", href="#", className="flex items-center p-4 text-gray-700 hover:bg-gray-200"),
            # html.A("Distribution", href="#", className="flex items-center p-4 text-gray-700 hover:bg-gray-200"),
            # html.A("Actions", href="#", className="flex items-center p-4 text-gray-700 hover:bg-gray-200"),
        ])
    ]),
    
    # Main Content
    html.Div(className="flex-1 p-6", children=[
        # Header
        html.Div(className="flex justify-between items-center mb-6", children=[
            html.Div(className="flex items-center", children=[
                html.Span("Management Criteria", className="text-lg font-semibold"),
                html.I(className="fas fa-chevron-down ml-2")
            ]),
            html.Div(className="flex items-center space-x-4", children=[
                html.I(className="fas fa-search text-gray-600"),
                html.I(className="fas fa-bell text-gray-600"),
                html.I(className="fas fa-user-circle text-gray-600"),
            ])
        ]),

        # Analysis Content
        html.Div(className="bg-white p-6 rounded-lg shadow", children=[
            html.H1("Analysis", className="text-2xl font-semibold mb-4"),
            # Key Stats Display
            html.Div(className="grid grid-cols-4 gap-4 mb-6", children=[
                html.Div(className="bg-gray-100 p-4 rounded-lg text-center", children=[
                    html.Span("85", className="text-2xl font-semibold text-green-500"),
                    html.P("Primary Strength", className="text-gray-500"),
                    html.P("68,256,55 Records", className="text-gray-500"),
                ]),
                # Add additional cards similarly
            ]),
            
            # Key Drivers (replace this with a Plotly chart for interactivity)
            html.Div(className="bg-gray-100 p-6 rounded-lg", children=[
                html.H2("Key Drivers", className="text-lg font-semibold mb-4"),
                dcc.Graph(figure=go.Figure(data=[
                    go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode="markers")  # Replace with your actual data
                ]))
            ])
        ])
    ])
])



if __name__ == "__main__":
    app.run_server(debug=True)
