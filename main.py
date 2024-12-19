from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
# from src.data.loader import load_transaction_data

DATA_PATH = "./data/transactions.csv"


def main() -> None:

    # load the data and create the data manager
    # data = load_transaction_data(DATA_PATH)
    

    app = Dash(
               external_scripts=[
                # "https://cdn.tailwindcss.com",
                BOOTSTRAP
                    ],
            external_stylesheets=[
                "https://cdn.tailwindcss.com",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
                'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap'
                    ]
               )
    app.title = "SCM Razor-Group SCM"
    # app.layout = create_layout(app, data)
    app.layout = create_layout(app)

    app.run_server(debug=True,port=8051)


if __name__ == "__main__":
    main()