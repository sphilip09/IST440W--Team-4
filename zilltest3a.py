from pyzillow import pyzillow
API_KEY="X1-ZWz1exje6lr66j_agge7"
zillow_data = pyzillow.ZillowWrapper(API_KEY)
result = zillow_data.get_deep_search_results('6333 Large St','19149')
data = pyzillow.GetDeepSearchResults(result)
print data.zillow_id
print data.home_type
print data.last_sold_price
