# Import our 3 custom modules
import data_processor
import anomaly_detector
import visualizer

def main():
    print("Starting Flood Risk Analyzer...")
    
    # Step 1: Ingest and clean the data
    print("Loading and cleaning data...")
    clean_data = data_processor.data('data/rainfall.csv')#clean_data stores finaldata
    
    # Step 2: Find the extreme outliers using Z-scores
    print("Detecting extreme weather events...")
    anomalies = anomaly_detector.findanomalies(clean_data)
    print(f"Found ({len(anomalies)}) extreme rainfall events.")
    
    # Step 3: Visualize the trend and calculate the slope
    print("Graphing trends and calculating risk...")
    trend_slope = visualizer.plot_trends(anomalies)
    
    # Final Output
    if trend_slope > 0:
        print(f"CONCLUSION: The trendline slope is positive ({trend_slope:.2f}). Flood risk intensity is INCREASING over time.")
    else:
        print(f"CONCLUSION: The trendline slope is negative ({trend_slope:.2f}). Flood risk intensity is DECREASING over time.")

if __name__ == "__main__":
    main()
