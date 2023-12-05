# Amazon_Best_Seller_Rank

## Description:
- Analyze the Amazon best-seller ranks for books written by Steven S. Skiena and recommend a book for purchase.

## Install python libraries:
- run make command `make install`

## Run program:
- run make command `make run`

# Technical Report

## Methodology:
- For this project the objective I wanted to analyze the Amazon best-seller ranks for books written by Steven S. Skiena and recommend a book for purchase. So this consist of gathering the data on Amazon then analyze the data using python libraries and with this information I would recommend a book for purchase.

## Data Collection:
- For data collection of Amazon best-seller ranks for books written by Steven S. Skiena. I first tried to create a web scrapper using python that would pull this data from Amazon. This failed due to the Amazon website blocks it's user from using a web scrapper on there website. Due to this I had to manually pull the data from the website then I store the data in a JSON file for later data analysis and visualization.
- Error when trying to web scrap Amazon:
![amazon_blocking_scraper](https://github.com/themnsavage/Amazon_Best_Seller_Rank/assets/60998598/d9d614b1-9189-4501-a2d0-bc971552aff8)

## Data Analysis and Visualization:
- For data analysis and visualization I use the python library matplotlib for creating a bar graph then with this bar graph I could analysis the data.
- Bar graph:
![image](https://github.com/themnsavage/Amazon_Best_Seller_Rank/assets/60998598/75093cc9-c1a4-4d9f-a689-d3549c8941f5)


## Results/Book Recommendation: The Algorithm Design Manual (Texts in Computer Science)
- ### Recommendation Justification:
    - I would recommend this book due to it having the best rank out of all the books I pulled from Amazon 
- ### Suitability as a Gift:
    - This gift would be a suitable gift if the receiver of the gift are interested in learning about algorithms.

## Conclusion:
- In this project, I analyzed Amazon best-seller ranks for Steven S. Skiena's books and recommend "The Algorithm Design Manual" for purchase. After manually collecting data because web scraping was blocked, I used matplotlib to create a bar graph for analysis. This book is the top-ranked and great for those interested in algorithms.
