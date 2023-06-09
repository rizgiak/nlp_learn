import dash
import dash_core_components as dcc
import dash_html_components as html
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64

# Generate wordcloud
text = "hello world this is a test of the wordcloud generator"
wc = WordCloud().generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()

# Convert figure to base64 encoded string
fig = plt.gcf()
fig.canvas.draw()
image_data = base64.b64encode(fig.canvas.tostring_rgb()).decode('utf-8')

# Define Dash app and layout
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        id='wordcloud',
        figure={
            'data': [],
            'layout': {
                'images': [{
                    'source': 'data:image/png;base64,{}'.format(image_data),
                    'xref': 'paper',
                    'yref': 'paper',
                    'x': 0,
                    'y': 1,
                    'sizex': 1,
                    'sizey': 1,
                    'sizing': 'stretch',
                    'layer': 'above'
                }]
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)