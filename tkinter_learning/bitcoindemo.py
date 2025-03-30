import requests
import matplotlib.pyplot as plt
import time

# Function to fetch live Bitcoin price
def fetch_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    else:
        print("Failed to fetch data.")
        return None

# Initialize lists to store time and price data
timestamps = []
prices = []

# Plot setup
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(10, 6))

# Real-time data fetching and visualization
try:
    for _ in range(50):  # Fetch 50 data points (you can adjust this as needed)
        price = fetch_bitcoin_price()
        if price is not None:
            timestamps.append(time.strftime("%H:%M:%S"))  # Current time
            prices.append(price)
            
            # Clear the plot and redraw
            ax.clear()
            ax.plot(timestamps, prices, label='BTC/USD Price', color='blue')
            ax.set_title('Live Bitcoin Price')
            ax.set_xlabel('Time')
            ax.set_ylabel('Price (USD)')
            ax.legend(loc='upper left')
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            plt.tight_layout()
            plt.pause(1)  # Pause for 1 second to simulate live plotting
        time.sleep(1)  # Fetch new data every second
except KeyboardInterrupt:
    print("\nLive plotting stopped.")
finally:
    plt.ioff()  # Turn off interactive mode
    plt.show()
