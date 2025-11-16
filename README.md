# Global Life Expectancy Visualization

This project provides a simple Python script to visualize global life expectancy data using an interactive choropleth map.

## Description

The script `gle.py` uses the Plotly library to create a world map showing life expectancy by country. The data is sourced from the Gapminder dataset, which includes life expectancy statistics over time.

## Features

- Interactive world map
- Color-coded life expectancy data
- Hover details for each country
- Uses the Plasma color scale for better visualization

## Installation

1. Ensure you have Python installed (version 3.6 or higher recommended).
2. Install the required dependencies:

```bash
pip install plotly
```

## Usage

Run the script to display the interactive map:

```bash
python gle.py
```

This will open a web browser window showing the choropleth map. You can hover over countries to see detailed information.

## Dependencies

- plotly: For creating interactive visualizations

## Data Source

The data is provided by the Gapminder dataset through Plotly's built-in data module.