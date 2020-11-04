import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.models import HoverTool, Title
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.layouts import column, row
from bokeh.models.widgets import Select

# region 1. question a
# set up data
latimes_agency_totals = pd.read_csv("latimes-state-totals.csv")
latimes_agency_totals = latimes_agency_totals[
    (latimes_agency_totals["date"] >= "2020-08-01") & (latimes_agency_totals["date"] <= "2020-08-31")]
latimes_agency_totals['date_time'] = pd.to_datetime(latimes_agency_totals['date'])

# set up plot
p1 = figure(
    tools='crosshair,pan,box_zoom',
    y_axis_label='New Coronavirus cases',
    x_axis_label='datetime',
    x_axis_type='datetime',
    plot_width=1030,
    plot_height=500,
)

p1.title.text = "New Coronavirus Cases in California in August"
p1.title.align = "center"
p1.title.text_font_size = "20px"
p1.align = "center"

p1.add_layout(Title(text="             download data from 'https://github.com/datadesk/california-coronavirus-data' ("
                         "latimes-state-totals.csv) in GitHub", text_font_style="italic"), 'above')
p1.add_layout(Title(text="Source: provided by local public health agencies; published by "
                         "'latimes.com/coronavirustracker'", text_font_style="italic"), 'above')
p1.add_layout(Title(text="Date of last update: 2020-10-15", text_font_style="italic"), 'above')

p1.line('date_time', 'new_confirmed_cases', source=latimes_agency_totals)
p1.circle('date_time', 'new_confirmed_cases', source=latimes_agency_totals, fill_color="blue", size=5)
p1.add_tools(HoverTool(
    tooltips=[
        ('date', '@date_time{%Y-%m-%d}'),
        ('new cases', '@new_confirmed_cases'),
    ],

    formatters={
        '@date_time': 'datetime',
    }))
# endregion


# region 2. question b
data = pd.read_csv("cdph-race-ethnicity.csv")
race_total = data.loc[data['age'] == 'all']
race_total = race_total[["date", "race", "confirmed_cases_percent", "deaths_percent", "population_percent"]]
total = race_total[["date", "race", "confirmed_cases_percent", "deaths_percent", "population_percent"]]
races = sorted(set(total["race"].tolist()))
death = total["deaths_percent"].tolist()
case = total["confirmed_cases_percent"].tolist()
population = total["population_percent"].tolist()
bar2 = ['confirmed_cases', 'population']
bar3 = ['death', 'population']
date = sorted(set(race_total['date']), reverse=True)

# set up data
x2 = [(race, bar) for race in races for bar in bar2]
y2 = sum(zip(case, population), ())

source2 = ColumnDataSource(data=dict(x=x2, y=y2))

# set up plot
p2 = figure(x_range=FactorRange(*x2), plot_height=550,plot_width=1030,
            y_axis_label='percent', x_axis_label='race',
            toolbar_location=None, tools="")
p2.title.text = "Confirmed_case% VS Population%"
p2.title.align = "center"
p2.title.text_font_size = "20px"

p2.add_layout(Title(text="            published by 'latimes.com/coronavirustracker'; download data from "
                         "'https://github.com/datadesk/california-coronavirus-data' (cdph-race-ethnicity.csv) in "
                         "GitHub", text_font_style="italic"), 'above')
p2.add_layout(Title(text="Source: provided by the California Department of Public Health "
                         "'https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx';",
                    text_font_style="italic"), 'above')
p2.add_layout(Title(text="Date of last update: 2020-10-14", text_font_style="italic"), 'above')

r2 = p2.vbar(x='x', top='y', width=0.9, source=source2, line_color="white",
             fill_color=factor_cmap('x', palette=["#c9d9d3", "#718dbf"], factors=bar2, start=1, end=2))


p2.y_range.start = 0
p2.x_range.range_padding = 0.1
p2.xaxis.major_label_orientation = 0.8
p2.xgrid.grid_line_color = None
p2.add_tools(HoverTool(
    tooltips=[
        ('confirmed_case', '@x'),
        ('population', '@y'),
    ]))

# set up widgets
select1 = Select(title="Confirmed case date:", value=date[0], options=date, width=105)


# set up callbacks
def update2(attrname, old, new):
    selected_data = race_total[race_total['date'] == select1.value]
    a = selected_data['confirmed_cases_percent']
    b = selected_data["population_percent"]
    y = sum(zip(a, b), ())
    r2.data_source.data['y'] = y

select1.on_change('value', update2)
# endregion


# region 3. question c
# set up data
x3 = [(race, bar) for race in races for bar in bar3]
y3 = sum(zip(death, population), ())

source3 = ColumnDataSource(data=dict(x=x3, y=y3))

# set up plot
p3 = figure(x_range=FactorRange(*x3), plot_height=550,plot_width=1030,
            y_axis_label='percent',
            x_axis_label='race',
            toolbar_location=None, tools="")
p3.title.text = "Death% VS Population%"
p3.title.align = "center"
p3.title.text_font_size = "20px"

p3.add_layout(Title(text="            published by 'latimes.com/coronavirustracker'; download data from "
                         "'https://github.com/datadesk/california-coronavirus-data' (cdph-race-ethnicity.csv) in "
                         "GitHub", text_font_style="italic"), 'above')
p3.add_layout(Title(text="Source: provided by the California Department of Public Health "
                         "'https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx';",
                    text_font_style="italic"), 'above')
p3.add_layout(Title(text="Date of last update: 2020-10-14", text_font_style="italic"), 'above')

r3 = p3.vbar(x='x', top='y', width=0.9, source=source3, line_color="white",
             fill_color=factor_cmap('x', palette=["#c9d9d3", "#718dbf"], factors=bar3, start=1, end=2))

p3.y_range.start = 0
p3.x_range.range_padding = 0.1
p3.xaxis.major_label_orientation = 0.8
p3.xgrid.grid_line_color = None
p3.add_tools(HoverTool(
    tooltips=[
        ('death', '@x'),
        ('population', '@y'),
    ]))

# set up widgets
select2 = Select(title="Death date:", value=date[0], options=date, width=105)

# set up callbacks
def update3(attrname, old, new):
    selected_data = race_total[race_total['date'] == select2.value]
    a = selected_data['deaths_percent']
    b = selected_data["population_percent"]
    y = sum(zip(a, b), ())
    r3.data_source.data['y'] = y

select2.on_change('value', update3)
# endregion

# set up layouts and add to document
curdoc().add_root(column(p1))
curdoc().add_root(row(p2, select1))
curdoc().add_root(row(p3, select2))


