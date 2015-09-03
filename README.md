# Episode-Title-Renamer

This is a tiny Python script to rename/fix episode titles of TV shows at your locale. I have scrapped Wikipedia Page listing episode titles for every season of the TV show.

-------
HOW-TO:
-------
1. For this to run, You will need to install Beautiful Soup (http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

2. Run the renamer.py file from command line as

            python renamer.py
            
To test, I have hardcoded the URL of the desired Wikipedia Page (https://en.wikipedia.org/wiki/List_of_Friends_episodes) and the parent folder of the TV show. 

Optionally we could pass the URL and the path to parent folder as arguements. [TO-DO #1]

3. It will prompt to confirm the rename for individual files (episodes of every season available). [TO-Do #2 - Improve this!]. Type "y" or "yes" or "ye", it will go ahead with the rename.

4. Done!

-----
WHY?:
-----
Confession, I am huge fan of FRIENDS (TV show) and recently, my HDD crashed (~45GB including bloopers and interviews, LOST!). On transfering the entire season from a friend's HDD, the titles were messed up. They had just episode number as the title (argh!). Also, some episodes were missing and it is painstaking to find the missing ones.

This script make it look cleaner and organized :)

-------
TO-DOs:
-------
3. Find missing episodes in every season and also missing seasons
4. Do assignments -_-
5. Organize a list of episodes into different season (Long shot!)

Would love if you could contribute to this project. :D
