from bokeh.sampledata.glucose import data
(x, y) = (data.ix['2010-10-06'].index.to_series(), data.ix['2010-10-06']['glucose'])

from bokeh.plotting import figure, gridplot, output_file, show
from bokeh.models import ColumnDataSource, Circle, HoverTool, Callback

output_file("hover_callback.html", mode='relative-dev')

# Basic plot setup
p = figure(width=600, height=300, x_axis_type="datetime", tools="", toolbar_location=None, title='Hover over points')
p.line(x, y, line_dash="4 4", line_width=1, color='gray')

# Add a circle, that is visible only when selected
source = ColumnDataSource({'x': x, 'y': y})
invisible_circle = Circle(x='x', y='y', fill_color='gray', fill_alpha=0.05, line_color=None, size=20)
visible_circle = Circle(x='x', y='y', fill_color='firebrick', fill_alpha=0.5, line_color=None, size=20)
cr = p.add_glyph(source, invisible_circle, selection_glyph=visible_circle, nonselection_glyph=invisible_circle)

# Add a hover tool, that selects the circle
code = "source.set('selected', cb_data['index']);"
callback = Callback(args={'source': source}, code=code)
hide_tooltip = "<style>.bk-tooltip.bk-tooltip-custom{display:none !important}</style>"
p.add_tools(HoverTool(tooltips=hide_tooltip, callback=callback, renderers=[cr]))

show(p)

