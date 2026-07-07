import os
from pathlib import Path

import pandas as pd
import plotly.express as px
import psycopg2
import dash_bootstrap_components as dbc
from dotenv import load_dotenv
from dash import Dash, Input, Output, dcc, html


ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

app = Dash(
    __name__,
    title="Brazilian E-Commerce Dashboard",
    external_stylesheets=[dbc.themes.DARKLY],
)


TABLES = [
    ("weekday_weekend_pmt", "gold.mart_weekday_weekend_pmt"),
    ("payment_review", "gold.mart_payment_review"),
    ("products_performance", "gold.mart_products_performance"),
    ("seller_performance", "gold.mart_seller_performance"),
    ("shippingdays_review", "gold.mart_shippingdays_review"),
    ("shippingdays_product", "gold.mart_shippingdays_product"),
]


COLOR_SEQUENCE = px.colors.sequential.Plasma
CARD_STYLE = {
    "borderRadius": "1rem",
    "backgroundColor": "#111827",
    "border": "1px solid #1f2937",
    "boxShadow": "0 12px 25px rgba(15, 23, 42, 0.35)",
}


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def fetch_table(table_name: str) -> tuple[pd.DataFrame | None, str | None]:
    if not all(
        [
            os.getenv("DB_HOST"),
            os.getenv("DB_PORT"),
            os.getenv("DB_NAME"),
            os.getenv("DB_USER"),
            os.getenv("DB_PASSWORD"),
        ]
    ):
        return None, "Database connection settings are not configured. Set DB_HOST, DB_PORT, DB_NAME, DB_USER, and DB_PASSWORD to load the mart tables."

    try:
        with get_connection() as conn:
            return pd.read_sql_query(f"SELECT * FROM {table_name};", conn), None
    except Exception as exc:  # pragma: no cover - runtime safeguard
        return None, f"Unable to load {table_name}: {exc}"


def apply_dark_theme(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font=dict(color="white"),
        margin=dict(l=24, r=24, t=64, b=24),
    )
    fig.update_xaxes(showgrid=True, gridcolor="#334155", zerolinecolor="#334155")
    fig.update_yaxes(showgrid=True, gridcolor="#334155", zerolinecolor="#334155")
    return fig


def build_chart_1(df: pd.DataFrame):
    if df is None or df.empty:
        return px.pie(values=[], names=[], title="Payment mix by weekday vs weekend")

    fig = px.pie(
        df,
        names="weekday_weekend",
        values="net_pmt_mil",
        hole=0.55,
        title="Payment mix by weekday vs weekend",
        color_discrete_sequence=COLOR_SEQUENCE,
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="%{label}<br>Revenue: %{value:.2f}M<br>Percent: %{percent}<extra></extra>",
        marker=dict(line=dict(color="#0f172a", width=2)),
        showlegend=False,
    )
    return apply_dark_theme(fig)


def build_chart_2(df: pd.DataFrame):
    if df is None or df.empty:
        return px.box(title="Review score distribution by payment type")

    fig = px.box(
        df,
        x="payment_type",
        y="review_score",
        color="payment_type",
        points="outliers",
        title="Review score distribution by payment type",
        color_discrete_sequence=COLOR_SEQUENCE,
    )
    fig.update_traces(
        hovertemplate="Payment type: %{x}<br>Review score: %{y}<extra></extra>",
    )
    fig.update_layout(showlegend=False)
    return apply_dark_theme(fig)


def build_chart_3(df: pd.DataFrame, category: str | None = None):
    if df is None or df.empty:
        return px.bar(title="Top products by revenue")

    filtered = df.copy()
    if category:
        filtered = filtered[filtered["product_category_name"] == category]

    filtered = filtered.sort_values("net_product_revenue", ascending=False).head(20)
    fig = px.bar(
        filtered,
        x="net_product_revenue",
        y="product_id",
        orientation="h",
        color="net_product_revenue",
        title="Top 20 products by revenue",
        color_continuous_scale="Aggrnyl",
    )
    fig.update_traces(
        hovertemplate="Product: %{y}<br>Revenue: %{x:.2f}<extra></extra>",
    )
    fig.update_layout(showlegend=False)
    return apply_dark_theme(fig)


def build_chart_4(df: pd.DataFrame):
    if df is None or df.empty:
        return px.scatter(title="Seller revenue and review score")

    fig = px.scatter(
        df,
        x="total_revenue",
        y="avg_review_score",
        size="units_sold",
        color="avg_review_score",
        hover_data=["seller_id", "total_revenue", "units_sold", "order_count", "avg_review_score"],
        title="Seller revenue vs average review score",
        color_continuous_scale="Plasma",
        size_max=30,
    )
    fig.update_traces(
        hovertemplate=(
            "Seller: %{customdata[0]}<br>Revenue: %{x:.2f}<br>Units sold: %{marker.size}<br>Order count: %{customdata[3]}<br>Avg review score: %{y:.2f}<extra></extra>"
        )
    )
    return apply_dark_theme(fig)


def build_chart_5(df: pd.DataFrame):
    if df is None or df.empty:
        return px.line(title="Average shipment days by review score")

    sorted_df = df.sort_values("review_score")
    fig = px.line(
        sorted_df,
        x="review_score",
        y="avg_shipment_days",
        markers=True,
        title="Average shipment days by review score",
        color_discrete_sequence=[COLOR_SEQUENCE[2]],
    )
    fig.update_traces(
        hovertemplate="Review score: %{x}<br>Avg shipment days: %{y:.2f}<extra></extra>",
    )
    return apply_dark_theme(fig)


def build_chart_6(df: pd.DataFrame, top_n: int = 10):
    if df is None or df.empty:
        return px.bar(title="Average shipment days by product category")

    top_n = max(1, int(top_n))
    sorted_df = df.sort_values("avg_shipment_days", ascending=False).head(top_n)
    fig = px.bar(
        sorted_df,
        x="avg_shipment_days",
        y="product_category_name",
        orientation="h",
        color="avg_shipment_days",
        title=f"Top {top_n} categories by average shipment days",
        color_continuous_scale="Bluyl",
    )
    fig.update_traces(
        hovertemplate="Category: %{y}<br>Avg shipment days: %{x:.2f}<extra></extra>",
    )
    fig.update_layout(showlegend=False)
    return apply_dark_theme(fig)


def load_dashboard_data():
    datasets = {}
    errors = []
    for key, table_name in TABLES:
        df, error = fetch_table(table_name)
        datasets[key] = df
        if error:
            errors.append(error)
    return datasets, errors


DATASETS, ERRORS = load_dashboard_data()

CATEGORY_OPTIONS = []
if DATASETS.get("products_performance") is not None:
    CATEGORY_OPTIONS = [
        {"label": category, "value": category}
        for category in sorted(DATASETS["products_performance"]["product_category_name"].dropna().unique())
    ]

DEFAULT_CATEGORY = CATEGORY_OPTIONS[0]["value"] if CATEGORY_OPTIONS else None
DEFAULT_TOP_N = 10


def build_card(title: str, body):
    children = [html.H5(title, className="card-title", style={"color": "#e2e8f0"})]
    if isinstance(body, (list, tuple)):
        children.extend(body)
    else:
        children.append(body)

    return dbc.Card(
        dbc.CardBody(children),
        style=CARD_STYLE,
        className="mb-4",
    )


app.layout = dbc.Container(
    fluid=True,
    className="py-4",
    children=[
        dbc.Row(
            dbc.Col(
                [
                    html.H1("Brazilian E-Commerce Dashboard", className="display-4", style={"color": "#f8fafc"}),
                    html.P(
                        "KPIs built using PostgreSQL mart tables",
                        className="lead",
                        style={"color": "#cbd5e1"},
                    ),
                ],
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(build_card("Payment mix by weekday vs weekend", dcc.Graph(figure=build_chart_1(DATASETS["weekday_weekend_pmt"]))), md=6),
                dbc.Col(build_card("Review score distribution by payment type", dcc.Graph(figure=build_chart_2(DATASETS["payment_review"]))), md=6),
            ],
            className="g-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    build_card(
                        "Top products by category",
                        [
                            dcc.Dropdown(
                                id="product-category-dropdown",
                                options=CATEGORY_OPTIONS,
                                value=DEFAULT_CATEGORY,
                                clearable=False,
                                style={"color": "#0f172a"},
                            ),
                            dcc.Graph(
                                id="products-performance-graph",
                                figure=build_chart_3(DATASETS["products_performance"], DEFAULT_CATEGORY),
                            ),
                        ],
                    ),
                    md=6,
                ),
                dbc.Col(build_card("Seller revenue vs review score", dcc.Graph(figure=build_chart_4(DATASETS["seller_performance"]))), md=6),
            ],
            className="g-4",
        ),
        dbc.Row(
            [
                dbc.Col(build_card("Shipment days by review score", dcc.Graph(figure=build_chart_5(DATASETS["shippingdays_review"]))), md=6),
                dbc.Col(
                    build_card(
                        "Top categories by shipping time",
                        [
                            dbc.Row(
                                dbc.Col(
                                    dcc.Input(
                                        id="top-n-categories",
                                        type="number",
                                        min=1,
                                        step=1,
                                        value=DEFAULT_TOP_N,
                                        style={"width": "100%", "padding": "0.5rem", "borderRadius": "0.5rem", "border": "1px solid #334155"},
                                    ),
                                ),
                                className="mb-3",
                            ),
                            dcc.Graph(
                                id="shippingdays-product-graph",
                                figure=build_chart_6(DATASETS["shippingdays_product"], DEFAULT_TOP_N),
                            ),
                        ],
                    ),
                    md=6,
                ),
            ],
            className="g-4",
        ),
        dbc.Row(
            dbc.Col(
                build_card(
                    "Data status",
                    html.Ul(
                        [html.Li(message) for message in ERRORS] if ERRORS else [html.Li("All mart tables loaded successfully.")],
                        style={"color": "#cbd5e1"},
                    ),
                ),
                width=12,
            ),
            className="g-4",
        ),
    ],
)


@app.callback(
    Output("products-performance-graph", "figure"),
    Input("product-category-dropdown", "value"),
)
def update_products_performance(selected_category):
    return build_chart_3(DATASETS["products_performance"], selected_category)


@app.callback(
    Output("shippingdays-product-graph", "figure"),
    Input("top-n-categories", "value"),
)
def update_shippingdays_product(top_n):
    try:
        top_n_value = int(top_n)
    except (TypeError, ValueError):
        top_n_value = DEFAULT_TOP_N
    return build_chart_6(DATASETS["shippingdays_product"], top_n_value)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
