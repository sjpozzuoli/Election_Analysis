# Analysis and Audit of Election Data Using Python

### This analysis was performed due to an audit request from the election commission. They are requesting further information on the breakdown of the votes cast within different counties in Colorado. Using Python, we can audit the full list of votes cast and their location, creating a chart to print all of the data to make it easier to view. 

## Election-Audit Results

- There were a total of 369,711 votes cast during this election.

  ![Total_Votes](https://user-images.githubusercontent.com/81929616/117553653-c970ff80-b020-11eb-8a22-50007a3b5852.PNG)

- Breaking down the votes by county, we can see Jefferson had a total of 38,855 votes cast, which accounted for 10.5% of the total vote. Denver had 306,055 votes cast, which accounted for 82.8% of the total vote. And Arapahoe had 24,801 votes cast, which account for 6.7% of the total vote.
- Based on this information, Denver had the highest number of votes cast of the counties we examined.

  ![County_Votes](https://user-images.githubusercontent.com/81929616/117553834-bb6fae80-b021-11eb-8a4c-98556092bb02.PNG)

- Now for the cadidates: Charles Casper Stockham received 85,213 votes, which equated to 23% of the total vote. Diana DeGette received 272,892 votes, which equated to 73.8% of the total vote. Raymon Anthony Doane received 11,606 votes, which equated to 3.1% of the total vote.

  ![Candidate_Votes](https://user-images.githubusercontent.com/81929616/117553929-57011f00-b022-11eb-93d0-5e011652cdfe.PNG)

- Finally, after examaning all of this information, it was determined that Diana DeGette won the election with a total of 272,892 votes, or 73.8% of the total votes cast.

  ![Winner_Print](https://user-images.githubusercontent.com/81929616/117553948-80ba4600-b022-11eb-9fc7-299527d68a83.PNG)

## Election-Audit Summary

#### In summation, the scripts we used to analyze the data of this local election can be used for almost any election data, with some minor tweaks. First, there is some other information that is important when looking at the distribution of votes to different candidates. For example, one of those many data points is party affiliation. Adding in Republican, Democrat, Independent, etc. as another data variable could provide the winning candidate more information as to which party base they will have to work harder to "win" over during their time in office, especially if they would like to seek re-election for another term. In order to generate this information using Python, assuming it is contained within our election_results.csv file, we would need to create a new list and dictionary to hold the different party information per voter and incorporate similar for loops and if statements to list this information and print to our text file.

#### Secondly, this script could be used on the federal level as well, like during a presidential election. In this case, individual state's voting information is critical in determining the winner. We could modify the script very similarly to the above to capture and return the winner of each individual state, while also capturing the popular vote. While the winner of the popular vote does not always win the presidential election (it has happened 5 times in the history of the United States), it is important to gauge the total number of voters throughout the country. 
