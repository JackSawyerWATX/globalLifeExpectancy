import plotly.express as px
df = px.data.gapminder()
figure = px.choropleth(
  df,
  locations = 'iso_alpha',
  color = 'lifeExp',
  hover_name = 'country',
  color_continuous_scale = px.colors.sequential.Plasma,
  title = 'Global Life Expectancy'
)

figure.show()