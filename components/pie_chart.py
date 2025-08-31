# charts.py
import plotly.express as px

def create_pie_chart(yearly_values):
    green_colors = ['#006400', '#228B22', '#32CD32', '#7CFC00']
    fig = px.pie(
        names=yearly_values.keys(),
        values=yearly_values.values(),
        title="Your Carbon Footprint Breakdown",
        color_discrete_sequence=green_colors,
        hole=0.3
    )
    fig.update_traces(textinfo='label+percent', textfont_size=16)
    return fig
