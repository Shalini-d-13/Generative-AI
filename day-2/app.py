from dash import Dash, html, dcc, Input, Output, State
from openai import OpenAI

# -------- OpenAI Client --------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# -------- Dash App --------
app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f8",
        "height": "100vh",
        "padding": "40px",
        "fontFamily": "Segoe UI, Arial"
    },
    children=[

        html.Div(
            style={
                "maxWidth": "700px",
                "margin": "auto",
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "12px",
                "boxShadow": "0px 4px 12px rgba(0,0,0,0.1)"
            },
            children=[

                html.H2("💻 IT Engineer Assistant",
                        style={"textAlign": "center"}),

                html.P("Ask IT / Computer related questions",
                       style={"color": "#666", "textAlign": "center"}),

                dcc.Textarea(
                    id="user-input",
                    placeholder="Type your question here...",
                    style={
                        "width": "100%",
                        "height": 140,
                        "padding": "12px",
                        "borderRadius": "8px",
                        "border": "1px solid #ccc",
                        "fontSize": "15px"
                    }
                ),

                html.Br(),

                html.Button(
                    "Ask Assistant",
                    id="submit-btn",
                    style={
                        "width": "100%",
                        "padding": "12px",
                        "backgroundColor": "#2d7ff9",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "8px",
                        "fontSize": "16px",
                        "cursor": "pointer"
                    }
                ),

                html.Hr(),

                html.Div(
                    id="bot-output",
                    style={
                        "backgroundColor": "#f9fafb",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "minHeight": "120px",
                        "whiteSpace": "pre-wrap",
                        "border": "1px solid #e0e0e0"
                    }
                )
            ]
        )
    ]
)

# -------- Callback --------
@app.callback(
    Output("bot-output", "children"),
    Input("submit-btn", "n_clicks"),
    State("user-input", "value"),
    prevent_initial_call=True
)
def ask_bot(n, user_input):

    messages = [{
        "role": "system",
        "content": "you are an IT engineers assistant. Answer only IT and Computer related questions. If not related, say sorry."
    }, {
        "role": "user",
        "content": user_input
    }]

    response = client.chat.completions.create(
        model="openai/gpt-4",
        messages=messages,
        max_tokens=150
    )

    return response.choices[0].message.content


# -------- Run --------
if __name__ == "__main__":
    app.run(debug=True)
