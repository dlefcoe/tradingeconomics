
# import pandas as pd
import tradingeconomics as te
te.login('guest:guest')

#without a client key only a small sample of data will be given.

#Getting indicators data by country and indicator Output type will be pandas dataframe 
mydataUSA = te.getIndicatorData(country = 'United States', indicators = 'gdp')
latestGDPusa = mydataUSA['United States']['GDP'][0]['LatestValue']
print(mydataUSA)

print("===============================================================================================================")


mydataChina = te.getIndicatorData(country = 'China', indicators = 'gdp')
latestGDPchina = mydataChina['China']['GDP'][0]['LatestValue'] 
print(mydataChina)
#print(mydataChina['China']['GDP'])
#print('The latest china GDP value is: ' + str(latestGDPchina))
#print(mydataChina['China']['GDP'][0]['LatestValue'])

print("===============================================================================================================")


print('The latest china GDP value is: ' + str(latestGDPchina))
print('The latest USA GDP value is: ' + str(latestGDPusa))

diffGDP = round(latestGDPusa - latestGDPchina, 2)
print('The latest USA - China GDP value is: ' + str(diffGDP))


print("other countries not available")
#mydata = te.getIndicatorData(country = 'Canada', indicators = 'gdp')
#print(mydata)

print("===============================================================================================================")

