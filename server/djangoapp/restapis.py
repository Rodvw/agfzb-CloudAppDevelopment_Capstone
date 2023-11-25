import requests
import json
from .models import CarDealer, CarMake, CarModel
from requests.auth import HTTPBasicAuth


#    dealer_doc = dealer




# Create a `get_request` to make HTTP GET requests
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
def post_request(url,json_payload,**kwargs):
    response = requests.post(url, params=kwargs, json=payload)
    return response



# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealers_from_cf(url, **kwargs):    
    results = []    
    # Call get_request with a URL parameter    
    dealers = get_request(url)    
    if dealers:        
        # For each dealer object        
        for dealer in dealers:            
            # Create a CarDealer object with values in dealer dictionary            
            dealer_obj = CarDealer(address=dealer["address"], city=dealer["city"], full_name=dealer["full_name"], id=dealer["id"], lat=dealer["lat"], long=dealer["long"], short_name=dealer["short_name"], st=dealer["st"], zip=dealer["zip"])            
            results.append(dealer_obj)    
    return results


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
    review_obj.sentiment = analyze_review_sentiments(review_obj.review)


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative

def analyze_review_sentiments(dealerreview):
    get_request(url,**kwargs)

