"""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# -*- coding: utf-8 -*-
# pylint: disable=C0116, W0621, W1203, C0103, C0301, W1201
# C0116: Missing function or method docstring
# W0621: Redefining name %r from outer scope (line %s)
# W1203: Use % formatting in logging functions and pass the % parameters as arguments
# C0103: Constant name "%s" doesn't conform to UPPER_CASE naming style
# C0301: Line too long (%s/%s)
# W1201: Specify string format arguments as logging function parameters

# Author : James Sawyer
# Maintainer : James Sawyer
# Version : 1.0
# Status : Production
# Copyright : Copyright (c) 2024 James Sawyer

import json
import logging
import random

import requests

# Set the base URL of our trading simulation platforms
BASE_URL = "http://tradesim.jamessawyer.co.uk:5000"
ALT_BASE_URL = "http://mktmayhem.jamessawyer.co.uk:5000"

# Enhance logging output for better clarity
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def pretty_print_json(data):
    """Makes JSON data pretty and readable."""
    return json.dumps(data, indent=4, sort_keys=True)

def test_place_order():
    """Places a random order and logs the response."""
    url = f"{BASE_URL}/place_order"
    # Randomly decide between buy and sell, then set quantity and price
    side = random.choice(["buy", "sell"])
    quantity = random.randint(1, 10)
    price = round(random.uniform(90, 150), 2)  # Prices between 90 and 150
    
    order = {"side": side, "quantity": quantity, "price": price}
    response = requests.post(url, json=order)
    
    logger.info("Placing Order Test:")
    logger.info(f"Response: {pretty_print_json(response.json())}")
    
    if response.status_code == 201:
        logger.info("Order placed successfully!")
        return response.json().get("order_id")
    else:
        logger.info("Order placement failed.")

def test_check_order(order_id):
    """Checks the status of a specific order."""
    url = f"{BASE_URL}/check_order?order_id={order_id}"
    response = requests.get(url)
    
    logger.info("Checking Order Test:")
    logger.info(f"Response: {pretty_print_json(response.json())}")
    
    if response.status_code == 200:
        logger.info("Order check successful!")
    else:
        logger.info("Order check failed.")

def test_order_depth():
    """Checks the depth of the order book."""
    url = f"{BASE_URL}/order_depth"
    response = requests.get(url)
    
    logger.info("Order Depth Test:")
    logger.info(f"Response: {pretty_print_json(response.json())}")
    
    if response.status_code == 200:
        logger.info("Order depth check successful!")
    else:
        logger.info("Order depth check failed.")

def test_last_traded_prices():
    """Retrieves the last traded prices."""
    url = f"{BASE_URL}/last_traded_prices"
    response = requests.get(url)
    
    if response.status_code == 200:
        logger.info("Last Traded Prices Test: PASSED")
        logger.info(f"Response: {pretty_print_json(response.json())}")
    else:
        logger.info("Last Traded Prices Test: FAILED")

if __name__ == "__main__":
    # Loop to continuously test the API
    order_id = test_place_order()
    if order_id:
        test_check_order(order_id)
    logger.info("=-=-=-=-=-=-=-=-=-=")  # Separator for readability

    # Uncomment the following lines if you want to test additional functionalities
    # test_order_depth()
    # test_last_traded_prices()

