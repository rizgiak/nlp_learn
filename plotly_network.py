import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# Create some random data
x, y, z = np.random.normal(0, 1, (3, 100))

# Create a graph with 10 nodes and 15 edges
edge_x = [0, 0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8]
edge_y = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 10, 10]
edge_trace = go.Scatter3d(
    x=x[edge_x],
    y=y[edge_x],
    z=z[edge_x],
    mode='lines',
    line=dict(width=2, color='blue'),
)

# Create a scatter plot of the nodes
node_trace = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(size=5, color='red'),
)

# Add the traces to a data list
data = [edge_trace, node_trace]

# Create a layout for the plot
layout = go.Layout(
    title='3D Network Graph',
    showlegend=False,
    margin=dict(l=0, r=0, b=0, t=50),
    hovermode='closest',
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    )
)

# Create the app layout
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='network-graph', figure=dict(data=data, layout=layout)),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
