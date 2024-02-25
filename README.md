# MarketMayhem API Documentation

**MarketMayhem** offers a simulated trading environment where you can experiment with trading strategies without financial risk. Below you'll find the API endpoints available to interact with this environment.

## API Endpoints

### Place Order

- **Endpoint:** `/place_order`
- **Method:** `POST`
- **Description:** Place a new order. Specify the action (buy/sell), quantity, and price.
- **Payload Example:**
  ```json
  {
    "side": "buy", // or "sell"
    "quantity": 10,
    "price": 100.5
  }
  
## API Endpoints

### Check Order

- **Endpoint:** `/check_order?order_id={order_id}`
- **Method:** `GET`
- **Description:** Retrieve details and status of a specific order by `order_id`.

### Last Traded Prices

- **Endpoint:** `/last_traded_prices`
- **Method:** `GET`
- **Description:** Get the last traded prices for buy and sell orders.

### Order Depth

- **Endpoint:** `/order_depth`
- **Method:** `GET`
- **Description:** Provides an overview of the current order book, detailing the depth of buy and sell orders.

### Delete Order

- **Endpoint:** `/delete_order?order_id={order_id}`
- **Method:** `DELETE`
- **Description:** Remove an existing order from the order book by `order_id`.


## How to Use the API

The **MarketMayhem** API is RESTful, meaning you can interact with it using any REST-based client or automation tool such as Postman, cURL, or programming languages with HTTP client capabilities like Python's `requests` library, JavaScript (using fetch API or Axios), and many others.

### No Rate Limiting or API Keys (For Now)

Currently, there are no rate limits or API keys required to use the **MarketMayhem** API. This setup is designed to encourage exploration and learning. However, please be mindful that this might change as the project evolves, aiming to introduce more realistic trading simulation features.

### Environment

Keep in mind that **MarketMayhem** operates in a completely simulated environment. All trades, price movements, and market dynamics are simulations for educational and testing purposes. This makes it an ideal playground for trying out high-frequency trading (HFT) strategies, market making, or any other trading algorithms you're curious about, without any risk.

### Work in Progress

**MarketMayhem** is a work in progress. We're constantly looking to improve and expand the API's capabilities. As such, we appreciate your feedback and reports on any issues you encounter. Your input is invaluable in making **MarketMayhem** a better tool for everyone.

## Getting Started

To start interacting with the **MarketMayhem** API, choose an endpoint and send a request according to the specified method. Ensure your payload is properly formatted for `POST` requests. For `GET` and `DELETE` requests, parameters should be included in the URL as query strings.

Here's a quick example using cURL to place an order:

```bash
curl -X POST http://localhost:5000/place_order \
     -H "Content-Type: application/json" \
     -d '{"side": "buy", "quantity": 10, "price": 100.5}'```

And here's how you might check an order using Python's requests:

```
import requests

response = requests.get("http://localhost:5000/check_order?order_id=1234")
print(response.json())```


This expanded guide should help new users understand how to get started with the API, the tools they can use, and the nature of the simulated environment, along with encouraging contributions and feedback.

