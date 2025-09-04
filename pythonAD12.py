#Real-Time Data Visualization Dashboard with Plotly and Dash

#Write a Python program to build a real-time data visualization dashboard using Plotly and Dash.
# Import necessary libraries

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import random

# Function to generate random data
def generate_data():
    # Create a dictionary with timestamps and random values
    return {
        'timestamp': pd.date_range(start='2022-01-01', periods=100, freq='H'),
        'value': [random.randint(0, 100) for _ in range(100)]
    }

# Create a Dash app instance
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Add a header to the dashboard
    html.H1("Real-Time Data Visualization Dashboard"),
    # Add a Graph component to display the plot
    dcc.Graph(id='real-time-plot'),
    # Add an Interval component to update the plot at regular intervals
    dcc.Interval(
        id='interval-component',
        interval=1000,  # Update every 1000 milliseconds (1 second)
        n_intervals=0  # Initial number of intervals
    )
])

# Define a callback function to update the plot with new data
@app.callback(
    Output('real-time-plot', 'figure'),  # Output is the figure of the Graph component
    Input('interval-component', 'n_intervals')  # Input is the number of intervals
)
def update_plot(n):
    # Generate new data
    data = generate_data()
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)
    
    # Create a line plot using Plotly Express
    fig = px.line(df, x='timestamp', y='value', title='Real-Time Data')
    
    # Return the plot
    return fig

# Run the app server
if __name__ == '__main__':
    # Start the Dash app with debug mode enabled
    app.run(debug=True)  # app.run_server(debug=True)


#Dash is running on http://127.0.0.1:8050/

# * Serving Flask app 'pythonAD12'

 #* Debug mode: on
