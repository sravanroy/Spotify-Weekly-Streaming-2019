# Spotify-Weekly-Streaming-2019
> An interactive tableau dashboard to analyze the music trends in 2019 using Spotify data.

> Play your favorite song inside this dashboard!
https://public.tableau.com/profile/sravan.roy#!/vizhome/SpotifyWeeklyStreaming2019/Dashboard1




## **DATA & CODE**

#### In this section, I will go over the major steps involved in creating this dashboard.  

**Connecting to Spotify data**

1.  Navigate to [https://spotifycharts.com/regional](https://spotifycharts.com/regional) to download data from Spotify’s Top Charts.
2.  Select Top 200 tracks to see the top 200 trending tracks
3.  Use the dropdowns to filter by a specific country or select Global to see all country data. For this analysis, I'm going to focus on entire Global data so I can see listening habits by country. We can also choose to select Daily or Weekly data. For the purpose of this analysis, I chose Weekly data and dates starting from 2019

**Webscraper to extract data**

1.  The above filtering tasks and collecting data in each page would be time consuming and tedious
2.  Inorder to collect the entire data and create a final dataframe, I built a python web scraper parsing each URL at a time
3.  The complete code for the web scaper can be found in my [git repo](https://github.com/sravanroy/Spotify-Weekly-Streaming-2019)

**Bring it into Tableau**

1.  The final dataframe is loaded into tableau as an extract connection
2.  Now, I created all the important sheets for analyzing the music trends such as top songs, top artists, etc..
3.  I created a few calculated fields to match the song URL pattern (extracted by the parser) with that of Spotify's URL pattern for embedding and playing the song within the dashboard
4.  Finally, action filters were appied among all sheets to display information for the selected items in the dashboard
