from plotly.subplots import make_subplots
from plotting import scatter_plot, stacked_area_plot, heatmap_plot, sunburst_correlation_plot, rolling_mean_volatility_plot
from data_processing import load_and_process_data
import plotly.graph_objects as go
import os


df_resampled = load_and_process_data("AMZN.csv")

fig_scatter = scatter_plot(df_resampled)
fig_streamgraph = stacked_area_plot(df_resampled)
fig_heatmap = heatmap_plot(df_resampled)
fig_corr = sunburst_correlation_plot(df_resampled)
fig_rolling = rolling_mean_volatility_plot(df_resampled)

save_dir = os.path.dirname(os.path.realpath(__file__))

fig_scatter.write_html(os.path.join(save_dir, 'scatter_plot.html'))
fig_streamgraph.write_html(os.path.join(save_dir, 'stacked_area_plot.html'))
fig_heatmap.write_html(os.path.join(save_dir, 'heatmap_plot.html'))
fig_corr.write_html(os.path.join(save_dir, 'sunburst_plot.html'))
fig_rolling.write_html(os.path.join(save_dir, 'rolling_mean_volatility_plot.html'))


combined_fig = make_subplots(
    rows=3, cols=2,  
    subplot_titles=[
        "Scatter Plot", "Streamgraph",
        "Heatmap", "Sunburst Plot",
        "Rolling Mean and Volatility"
    ],
    specs=[
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "heatmap"}, {"type": "domain"}],
        [{"type": "xy"}, None]
    ],
)

combined_fig.add_traces(fig_scatter.data, rows=1, cols=1)
combined_fig.add_traces(fig_streamgraph.data, rows=1, cols=2)
combined_fig.add_traces(fig_heatmap.data, rows=2, cols=1)
combined_fig.add_traces(fig_corr.data, rows=2, cols=2)
combined_fig.add_traces(fig_rolling.data, rows=3, cols=1)

combined_fig.update_layout(
    title="Integrated Visualizations",
    template="plotly_dark",
    height=1200, 
    showlegend=False,
)

combined_fig.write_html(os.path.join(save_dir, 'combined_plots.html'))
print("All plots saved successfully!")
