from bokeh.sampledata.glucose import data
(x, y) = (data.ix['2010-10-06'].index.to_series(), data.ix['2010-10-06']['glucose'])

from jinja2 import Template

from bokeh.browserlib import view
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Circle, HoverTool, Callback
from bokeh.resources import Resources
from bokeh.embed import components

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

# Open our custom template
with open('template.jinja', 'r') as f:
    template = Template(f.read())

resources = Resources(mode='relative-dev')
template_variables = {
    'bokeh_js_files': resources.js_files
}
title = "Bokeh - Gapminder Bubble Plot"
script, div = components(p)
html = template.render(
    bokeh_js_files=resources.js_files,
    plot_script=script,
    plot_div=div,
    title=title
)

output_file = 'interactive.html'
with open(output_file, 'w') as f:
    f.write(html)
view(output_file)
