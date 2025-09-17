import random
import math

# Step 1: Generate stock data
def generate_stocks(num_stocks=5):
    stocks = []
    for i in range(num_stocks):
        symbol = f"STK{i+1}"
        open_price = round(random.uniform(100, 500), 2)
        close_price = round(open_price * random.uniform(0.9, 1.1), 2)  # -10% to +10%
        change = round(((close_price - open_price) / open_price) * 100, 2)
        stocks.append({
            'symbol': symbol,
            'open': open_price,
            'close': close_price,
            'change': change
        })
    return stocks

# Step 2: Sort using built-in sorted()
def sort_stocks_builtin(stocks):
    return sorted(stocks, key=lambda x: x['change'], reverse=True)

# Step 3: Heap Sort implementation
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l]['change'] > arr[largest]['change']:
        largest = l
    if r < n and arr[r]['change'] > arr[largest]['change']:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(stocks):
    n = len(stocks)
    for i in range(n//2 - 1, -1, -1):
        heapify(stocks, n, i)
    for i in range(n-1, 0, -1):
        stocks[0], stocks[i] = stocks[i], stocks[0]
        heapify(stocks, i, 0)
    return stocks[::-1]  # Reverse for descending order

# Step 4: Build a search dictionary
def build_stock_map(stocks):
    return {stock['symbol']: stock for stock in stocks}

# Step 5: Main function
def main():
    # Generate 5 sample stocks
    stocks = generate_stocks(5)

    print("Original Stock Data:")
    for stock in stocks:
        print(f"{stock['symbol']}: Open = {stock['open']}, Close = {stock['close']}, Change = {stock['change']}%")

    # Sort using built-in
    print("\nSorted by % Change (Built-in):")
    sorted_builtin = sort_stocks_builtin(stocks.copy())
    for stock in sorted_builtin:
        print(f"{stock['symbol']}: {stock['change']}%")

    # Sort using heap sort
    print("\nSorted by % Change (Heap Sort):")
    sorted_heap = heap_sort(stocks.copy())
    for stock in sorted_heap:
        print(f"{stock['symbol']}: {stock['change']}%")

    # Build search dictionary
    stock_map = build_stock_map(stocks)

    # Search example
    symbol_to_search = "STK3"
    print(f"\nSearching for {symbol_to_search}:")
    result = stock_map.get(symbol_to_search)
    if result:
        print(f"Found {symbol_to_search} -> Open: {result['open']}, Close: {result['close']}, Change: {result['change']}%")
    else:
        print("Stock not found.")

if __name__ == "__main__":
    main()
