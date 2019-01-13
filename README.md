volcanoworld

A web mapping application made with Leaflet.js and Python, pinpointing all the volcanoes in the world, both the holocene and pleistocene ones and providing information for each and one of them. Started making this app while following a tutorial from Udemy on how to create a volcano map for the USA. Wanted to try out what I'd learned and make one that included all countries and all volcanoes. Found the information I needed at the The Smithsonian Global Volcanism Program (https://volcano.si.edu) and wrote a small script (v5_data.py) to read and convert the .xsl files from there and into more appliable .csv files.
Added some extra tilelayers and made a graphic in photoshop to visualize the diffrent levles of elevation represented by colored triangles and added it to the map.

The Smithsonian Global Volcanism Program is at the time of writing closed due to a United States federal government shutdown. Global Volcanism Program staff are out of the office and unable to maintain the site until further notice. I've sent them an email asking for permission to use their data, but I guess no one is there to answer. I therefore added their logo to the map as a small tribute for providing this data.


To try it either download V5.py, GVP2.xls, GVP3.xls, elev.jpg and add them to your working directory and run v5.py, it will then produce 'world_volcanoes.html' in the same directory, which should be able to open and run in your browser, or try it live following this adress: http://www.geocities.ws/ulrikzor/index.html


This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments

Udemy: The Python Mega Course Build 10 Real World Applications
The Smithsonian Global Volcanism Program
