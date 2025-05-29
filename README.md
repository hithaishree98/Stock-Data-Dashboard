# Stock-Data-Dashboard

Transform raw historical stock data into an insightful web dashboard. Using Python, Pandas, and Plotly, this project:

- **Cleans & Resamples** your daily OHLCV CSV into monthly summaries  
- **Creates Five Visualizations**  
  1. **Scatter Plot** of trading volume vs. closing price, complete with a regression trendline and annotated peaks  
  2. **Streamgraph**-style stacked area chart of Open/High/Low/Close values over time  
  3. **Monthly Heatmap** showing how average closing prices evolve across years and seasons  
  4. **Sunburst Diagram** breaking out yearly total volume by categories of price gain or loss  
  5. **Rolling Mean & Volatility** chart tracking smoothed price trends and volatility swings, with key extreme‐value markers  
- **Bundles Everything** into a single, dark‐themed HTML dashboard for side-by-side comparison  


## 🚀 Why This Matters

- **Quick Insights:** Instantly spot relationships (e.g. “higher volume often pairs with higher close”), seasonal patterns, and outliers.  
- **No Front-End Work:** All interactivity (hover, zoom, sliders) comes “for free” via Plotly’s HTML export—no web framework needed.  
- **Customizable:** Swap in your own ticker files, adjust aggregation windows, or tweak color schemes in seconds.
