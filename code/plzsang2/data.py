

def plotdata():
    import seaborn as sns
    from bokeh.plotting import figure
    from bokeh.embed import components
    df=sns.load_dataset()
    data2= df.groupby(['smoker','sex']).mean().tip
    p=figure(x_range=['YES','NO'],plot_width=800, plot_height=550)
    #p.line(df['sepal_width'], df['sepal_length'], color='navy', alpha=0.5)
    p.vbar(x=['YES','NO'], width=0.05, top=data2, legend="팁")
    return components(p)