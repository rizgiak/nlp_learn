import dash
import dash.dependencies as dd
import dash_core_components as dcc
import dash_html_components as html

from io import BytesIO

import pandas as pd
from wordcloud import WordCloud
import base64

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

font_path_ = "C:\\Users\\dc13208\\AppData\\Local\\Microsoft\\Windows\\Fonts\\TakaoPGothic.ttf"
app = dash.Dash(__name__) #, external_stylesheets=external_stylesheets)

dfm = pd.DataFrame({'word': ['ポリマー', 'エタノール', '酸性', '試薬', 'アルコール'], 'freq': [10,15,6,3,9]})

app.layout = html.Div([
    html.Img(id="image_wc"),
])

def plot_wordcloud(data):
    d = {a: x for a, x in data.values}
    wc = WordCloud(background_color='black', width=480, height=360, font_path=font_path_)
    wc.fit_words(d)
    return wc.to_image()

@app.callback(dd.Output('image_wc', 'src'), [dd.Input('image_wc', 'id')])
def make_image(b):
    img = BytesIO()
    plot_wordcloud(data=dfm).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

if __name__ == '__main__':
    app.run_server(debug=True)