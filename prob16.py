# Problem 16

from collections import Counter

def find_trending_stocks(file_path):
    stock_counts = Counter()
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stock = int(line.strip())
                if stock == 0:
                    break
                stock_counts[stock] += 1
    except (ValueError, FileNotFoundError) as e:
        print(f"Error reading file: {e}")
        return
    
    def sort_by_count(item):
        return item[1]
    
    sorted_stocks = sorted(stock_counts.items(), reverse=True, key=sort_by_count)
    
    trending_stock, trending_count = sorted_stocks[0]
    second_place_stock, second_place_count = sorted_stocks[1]
    
    print(f"Trending: {trending_stock} [{trending_count} count]")
    print(f"Second Place: {second_place_stock} [{second_place_count} count]")

# Example usage
find_trending_stocks('input16.txt')

