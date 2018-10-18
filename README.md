# Wallhaven-downloader
Download wallpapers from wallhaven.cc.

# Instructions:
1. Run wallhaven-dl.py.
2. Enter username.
3. Enter password.
4. Goto wallhaven.cc and enter the keywords for your search.
5. Set the required options for search.
6. Copy the URL for the final search and paste it in the terminal.
7. Enter the path to the download location.
8. Enter the number of search pages to download.
9. Wait for the images to download.


# To run the script automatically in linux, create a cron job. For example:
`0 */2 * * *  /usr/bin/python /path/to/script &`
The above task runs the script every two hours. 
# Note:
To run the script automatically, edit it and hardcode the variables in it. The variables that need to be filled are:
username, password, searchurl, location, pgid.
