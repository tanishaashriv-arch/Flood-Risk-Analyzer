# Flood Risk Analyzer

# Problem Statement
India faces significant agricultural, economic, and infrastructural risks due to unpredictable and extreme rainfall. Understanding the frequency and intensity of these severe weather anomalies historically requires heavy statistical modeling. There is a clear need for an automated analytical tool capable of parsing over a century of historical weather data to identify true extreme events and determine if these climatic risks are increasing over time.

# Scope of the Project
This project is constrained to analyzing historical annual rainfall data across Indian subdivisions from the years 1901 to 2015. The scope includes extracting relevant data, cleaning missing values, calculating Z-scores to isolate extreme rainfall anomalies (Z-score > 3.0), and applying linear regression to visualize long-term trends. It focuses strictly on historical statistical analysis rather than real-time daily weather forecasting.

# Target Users
* Climate Researchers & Meteorologists: To study historical weather patterns and validate climate change models.
* Urban Planners & Civil Engineers: To design infrastructure and drainage systems capable of withstanding shifting extreme weather events.
* Agricultural Policymakers: To understand regional flood risks and allocate disaster relief or crop insurance resources effectively.
* Data Science Students: To observe how statistical methods (Z-scores, linear regression) are applied to real-world datasets.

# High-Level Features
* Automated Data Pipeline:Extracts, cleans, and transforms raw historical weather records into a workable DataFrame.
* Statistical Anomaly Detection: Utilizes standard deviation and historical means to mathematically isolate severe flood-risk years.
* Trend Analysis Engine: Computes a line of best fit through isolated extreme events to mathematically determine if risk intensity is escalating.
* Automated Visual Reporting: Generates a graphical summary combining scatter plots, trendlines, and a definitive conclusion stamp.