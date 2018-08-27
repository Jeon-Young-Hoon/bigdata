from bokeh.embed import components
from bokeh.models import ColumnDataSource


def plotdata():
    import pandas as pd
    import seaborn as sns
    from bokeh.plotting import figure
    from bokeh.embed import components
    df = pd.read_csv('final2.csv')
    df.date = pd.to_datetime(df.date)
    print(df.info())
    df2 = df.groupby('date').count()
    time2 = df2.loc['2004-03-03':'2018-08-12']
    time3 = time2.reset_index()
    p = figure(x_axis_type="datetime",title="게시글, 댓글 수", plot_height = 350, plot_width=800)
    p.xgrid.grid_line_color = None
    p.xaxis.axis_label = 'Time'
    p.yaxis.axis_label = 'Value'
    source = ColumnDataSource(time3)
    p.line('date', 'content',line_width =2, source=source )

    return components(p)


def plotdata2():
    from bokeh.plotting import figure
    fig = figure()
    fig.sizing_mode = 'scale_width'
    fig.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
    return components(fig)