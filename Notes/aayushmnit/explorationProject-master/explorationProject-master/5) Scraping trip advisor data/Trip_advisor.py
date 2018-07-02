## Importing libraries
import pandas as pd ## Data manipulation
import numpy as np ## Numerical Python - Matrix calculation
from bs4 import BeautifulSoup ## Dealing with HTML syntax
import urllib2 ## Pulling web pages
import argparse ## For argument parsing
import unicodedata ## For converting unicode data type to Ascii


def tripadvisor_scraper(url_path,output_path):
	page = urllib2.urlopen(url_path) ## Download the page
	soup = BeautifulSoup(page) ## Parse HTML code to a soup BeautifulSoup object
	ratings,date,review_header,review = [],[],[],[]
	x = soup.find_all("div",attrs = {'class':'ui_column is-9'}) ## To filter only review section
	for y in x:
		if len(y.find_all("div",attrs = {'class':'rating reviewItemInline'})) == 0: ## Error handling for removing items which are not reviews
			pass
		else:
			z = y.find_all("div",attrs = {'class':'rating reviewItemInline'})[0] 
			
			## Taking star rating out from the text
			ratings.append(z.span.attrs['class'][1][len(z.span.attrs['class'][1])-2]) 
			
			## Getting date of review out
			date.append(z.find_all('span')[1].attrs['title'])			
			
			## Getting the Review header
			z = y.find_all("div",attrs = {'class':'quote'})[0] 
			review_header.append(z.span.get_text()) 
			
			## Getting the review
			z = y.find_all("div",attrs = {'class':'prw_rup prw_reviews_text_summary_hsx'})[0]
			review.append(z.get_text())
	
	## Finding total number of reviews to calculate how many pages we need to load
	x = soup.find("p",attrs = {'class':'pagination-details'})
	number_of_reviews = int(x.get_text().split(' ')[4])
	
	## Auto generating other reviews hyperlink and parsing them
	for counter in range(1,(number_of_reviews // 10)+1):
	
		# Generating a new url path
		new_url = url_path.replace('Reviews','Reviews-or'+str(counter*10))
		page = urllib2.urlopen(new_url) ## Download the page
		soup = BeautifulSoup(page) ## Parse HTML code to a soup BeautifulSoup object
		x = soup.find_all("div",attrs = {'class':'ui_column is-9'}) ## To filter only review section
		for y in x:
			if len(y.find_all("div",attrs = {'class':'rating reviewItemInline'})) == 0: ## Error handling for removing items which are not reviews
				pass
			else:
				z = y.find_all("div",attrs = {'class':'rating reviewItemInline'})[0]
				
				## Taking star rating out from the text
				ratings.append(z.span.attrs['class'][1][len(z.span.attrs['class'][1])-2])
				
				## Getting date of review out
				date.append(z.find_all('span')[1].attrs['title'])
				
				## Getting the Review header
				z = y.find_all("div",attrs = {'class':'quote'})[0]
				review_header.append(z.span.get_text())
				
				## Getting the review
				z = y.find_all("div",attrs = {'class':'prw_rup prw_reviews_text_summary_hsx'})[0]
				review.append(z.get_text())
		
		## Printing the progress after scraping 5 pages(every 50 reviews)
		if counter % 5 == 0:
			print "Percentage completed:{0:.2f}%".format((1+float(counter)*100)/ (number_of_reviews//10))
	
	## Making a pandas dataframe of reviews collected
	df = pd.DataFrame(ratings)
	df.columns = ['ratings']
	df['date'] = date
	df['review_header'] = review_header
	df['review'] = review
	
	## Converting unicode text to ascii for saving it as a csv file
	for i in df.columns:
		if type(df.loc[0,i]) == unicode:
			print "Converting {0} from unicode to ascii lower case format".format(i)
			df.loc[:,i] =  df.loc[:,i].apply(lambda x: unicodedata.normalize('NFKD',x).encode('ascii','ignore').lower())
	
	## Saving the dataframe as csv on specified location
	df.to_csv(output_path,index = False)
	
if __name__ == '__main__':
	## Adding parser arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-output_path', dest='output_path') ## For specifying location to save the file 
	parser.add_argument('-url_path', dest='url_path') ## Home page URL for the restaurant
	args = parser.parse_args()
	
	## Calling the function
	tripadvisor_scraper(args.url_path,args.output_path)
	