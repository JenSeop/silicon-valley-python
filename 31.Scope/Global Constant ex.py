# global constant use like this example

HTTP_ENDPOINT = "https://yelp.com"

def print_us_restaurant_url():
    print(f"{HTTP_ENDPOINT}/biz/aryz-steakhouse-palo-alto")
    
def print_kr_restaurant_url():
    print(f"{HTTP_ENDPOINT}/biz/tobang-santa-clara-2")

print_us_restaurant_url()
print_kr_restaurant_url()