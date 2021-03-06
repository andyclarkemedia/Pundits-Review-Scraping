<img src="https://i.ibb.co/ZXVNVY5/pr-logo-plain-opauq.png" width="7.5%" height="7.5%">

# Pundits Review Scraping Process
Development of the scraping process used to collect data for the Pundits Review website - https://www.punditsreview.com/

> Pundits Review scrapes and processes news articles about the Premier League in order to give players and teams a review score each week. Each Monday, the project collects articles, divides them into phrases, identifies the player or club being referred to and then predicts the sentiment of the phrase. See more on how it works <a href="https://www.punditsreview.com/howitworks">here</a>!


## About this repository
This repository shows the progression of the method used to scrape and process football articles from news sites. The directories show the workings involved in each phase of building a solution. Phase One represents the first method used and final solution represents the method eventually integrated into the Pundits Review project. 

__NOTE:__
> Prediction models have been removed from this repository

## Contents

### <a href="https://github.com/andyclarkemedia/Pundits-Review-Scraping/tree/master/phase_one_bs_requests">Phase One</a>
Phase One Method: Combination of Beautiful Soup & Requests libraries used inside of notebook 
#### <a href="https://github.com/andyclarkemedia/Pundits-Review-Scraping/blob/master/phase_one_bs_requests/Scraping_to_Sentiment.ipynb">Show me the Notebook</a>


### <a href="https://github.com/andyclarkemedia/Pundits-Review-Scraping/tree/master/phase_two_scrapy_inside_notebook">Phase Two</a>
Phase Two Method: Scrapy takes place of beautiful soup & requests inside notebook
#### <a href="https://github.com/andyclarkemedia/Pundits-Review-Scraping/blob/master/phase_two_scrapy_inside_notebook/Expanding.ipynb">Show me the Notebook</a>


### <a href="https://github.com/andyclarkemedia/Pundits-Review-Scraping/tree/master/phase_three_pipeline_inside_notebook">Phase Three</a>
Phase Three Method: More functions incorporated into modules. Pipeline takes shape but crawler still called from notebook
#### <a href="https://github.com/andyclarkemedia/Pundits-Review-Scraping/blob/master/phase_three_pipeline_inside_notebook/matchreportscraper/trigger.ipynb">Show me the Notebook</a>


### <a href="https://github.com/andyclarkemedia/Pundits-Review-Scraping/tree/master/final_solution_scrapy_crawler_pipeline">Final Solution</a>
Core files used inside Scrapy Spider which was eventually integrated into project



## Associated Repositories

##### <a href="https://github.com/andyclarkemedia/Pundits-Review">Pundits Review</a> - 11/09/2020 - Complete directory for Pundits Review web application.
##### <a href="https://github.com/andyclarkemedia/Pundits-Review-Resources">Resources</a> - Data, images & Python dictionary of Premier League players & teams
##### <a href="https://github.com/andyclarkemedia/Pundits-Review-Entity-Extraction">Entity Extraction</a> - Development of the process used to recognise Premier League player & club entities within a news article
##### <a href="https://github.com/andyclarkemedia/Pundits-Review-Sentiment-Prediction">Sentiment Prediction</a> - Development of the prediction model used to predict the sentiment in football news articles 

##
#### Any Questions ... <a target="_blank" href="mailto:clarkeAJ3@cardiff.ac.uk">Send me an email!</a>
