from pyzillow import pyzillow
API_KEY="X1-ZWz1exje6lr66j_agge7"
zillow_data = pyzillow.ZillowWrapper(API_KEY)
address= raw_input('ENTER ADDRESS --- ')
zipc = raw_input('ENTER ZIP CODE --- ')

result = zillow_data.get_deep_search_results(address,zipc)
#result = zillow_data.get_deep_search_results('6333 Large St','19149')
data = pyzillow.GetDeepSearchResults(result)
print 'ADDRESS             --- ',address
print 'ZIP CODE            --- ',zipc
print 'ZILLOW ID           --- ',data.zillow_id
print 'HOME ID             --- ',data.home_type
print 'LAST SOLD PRICE     ---$ ',data.last_sold_price
print 'LAST SOLD DATE      --- ',data.last_sold_date
print 'NUMBER OF BEDROOMS  --- ',data.bedrooms
print 'NUMBER OF BATHROOMS --- ',data.bathrooms
print 'ZESTIMATE AMOUNT    ---$ ',data.zestimate_amount
print 'ZILLOW LAST UPDATED --- ',data.zestimate_last_updated
print 'ZILLOW VALUE CHANGE ---$ ',data.zestimate_value_change
print 'ZILLOW PERCENTILE   --- ',data.zestimate_percentile
print 'YEAR HOUSE BUILT    --- ',data.year_built
print 'HOUSE TAX VALUE     --- ',data.tax_value
