import requests 
from bs4 import BeautifulSoup
import argparse

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

def get_search_results_count(query):
    url = 'https://google.com/search?q=' + query 
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content, 'html.parser')
    total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False)
    results_num = ''.join([num for num in total_results_text if num.isdigit()])
    return results_num

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get Google search results count.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='+',
                        help='Search query')
    args = parser.parse_args()
    
    query = ' '.join(args.query)
    results_num = get_search_results_count(query)
    print(f"Number of results for '{query}': {results_num}")
