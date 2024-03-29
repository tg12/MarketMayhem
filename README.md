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

- **Order Notes:** Your order will be rejected if it lacks buy/sell direction, price, and quantity. While the simulation assumes unlimited financial resources for trading, profit and loss still apply. Ensure to verify your order against the current price; orders may also be rejected if no market participants match your specified price. (Error Code: 201)
  
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

The **MarketMayhem** API is RESTful, meaning you can interact with it using any REST-based client or automation tool such as Postman, cURL, or programming languages with HTTP client capabilities like Python's `requests` library, and many others.

### No Rate Limiting or API Keys (For Now)

Currently, there are no rate limits or API keys required to use the **MarketMayhem** API. This setup is designed to encourage exploration and learning. However, please be mindful that this might change as the project evolves, aiming to introduce more realistic trading simulation features.

### Environment

Keep in mind that **MarketMayhem** operates in a completely simulated environment. All trades, price movements, and market dynamics are simulations for educational and testing purposes. This makes it an ideal playground for trying out high-frequency trading (HFT) strategies, market making, or any other trading algorithms you're curious about, without any risk.

### Work in Progress

**MarketMayhem** is a work in progress. We're constantly looking to improve and expand the API's capabilities. As such, we appreciate your feedback and reports on any issues you encounter. Your input is invaluable in making **MarketMayhem** a better tool for everyone.

## Getting Started

To start interacting with the **MarketMayhem** API, choose an endpoint and send a request according to the specified method. Ensure your payload is properly formatted for `POST` requests. For `GET` and `DELETE` requests, parameters should be included in the URL as query strings.

Here's a quick example using cURL to place an order:


```
curl -X POST http://tradesim.jamessawyer.co.uk:5000/place_order \
     -H "Content-Type: application/json" \
     -d '{"side": "buy", "quantity": 10, "price": 100.5}'
```

And here's how you might check an order using Python's requests:

```
import requests

response = requests.get("http://tradesim.jamessawyer.co.uk:5000/check_order?order_id=1234")
print(response.json())
```

# Servers (24/7)

```sh
http://mktmayhem.jamessawyer.co.uk:5000

http://tradesim.jamessawyer.co.uk:5000
```
(Both Servers share the same orderbook)

This expanded guide should help new 
users understand how to get started with the API, the tools they can use, and the nature of the simulated environment, along with encouraging contributions and feedback.

# Challenge: Can You Beat the Market?

**MarketMayhem** isn't just a simulation; it's a challenge. Unlike traditional platforms, we don't simulate trading based on any specific commodity, index, or cryptocurrency. Our market operates 24/7—assuming the server stays up, of course! This continuous, round-the-clock trading environment is your playground to test strategies, refine your trading logic, and truly see if you can outsmart the market.

Our HFT Simulator is designed to challenge the **Efficient Markets Hypothesis (EMH)**, which states that all known information is already reflected in stock prices, making it impossible to consistently outperform the market. 

However, our simulator introduces you to the exciting world of high-frequency trading (HFT). Here's what you can do:

- **Explore Brief Inefficiencies**: Dive into scenarios where the market isn't perfectly efficient and discover opportunities that last only seconds.

- **Test Trading Strategies**: Use our simulator to practice fast-paced trading strategies in a completely risk-free environment.

- **Learn and Understand**: Gain valuable insights into how high-frequency traders might exploit small price differences that others overlook.

This simulator is your gateway to understanding the nuances of the trading world, providing a hands-on experience with the dynamics of high-frequency trading. Whether you're curious about how markets work or looking to develop your trading skills, our platform offers an educational and practical approach to the complexities of the financial markets.

### The Leaderboard

Are you ready to take your trading skills to the next level? We're excited to introduce the **MarketMayhem Leaderboard**, a place where traders can see how they stack up against others in the community. Whether you're a seasoned trader or just starting out, the leaderboard offers a fun and competitive way to see where you stand.

- **Rise to the Top**: Execute smart trades and climb the ranks of the **MarketMayhem Leaderboard**.
- **Learn and Adapt**: Analyze the strategies of top traders. Adapt and refine your approach to trading in our simulated market.

### The Ultimate Challenge

Can you beat the market? With MarketMayhem, you have the unique opportunity to try. Remember, success here doesn't just come from making profitable trades. It's about consistency, strategy, and the ability to adapt to market changes—skills that are invaluable in any trading environment.

Start trading now, keep the server buzzing, and let's see if you can secure your place at the top of the **MarketMayhem Leaderboard**. The challenge is on!



