### Aaraj Vij
### 03/26/2022
### This script collects Facebook post data and
### comments from the compiled CrowdTangle data sets

from tkinter import E
import pandas as pd

from facebook_scraper import get_posts

dataDF = pd.read_excel("FILEPATH HERE")

### Add new columns that will be propagated with data
dataDF["Post Text"] = None
dataDF["Post Time"] = None
dataDF["Post Likes"] = None
dataDF["# Post Comments"] = None
dataDF["# Post Shares"] = None
dataDF["Comment Text"] = None


### Iterate through each row of the DataFrame
for index, row in dataDF.iterrows():

    print(row["Link"])
    postURL = row["Link"].split("https://www.facebook.com/", 1)[1] # facebook-scraper library automatically inserts this to the beginning of the URL
    print("CURRENT POST URL IS", postURL)

    commentsDict = {}

    for post in get_posts(postURL, options={"comments": True}, cookies="FILEPATH HERE"):
        dataDF.loc[index, "Post Text"] = post["text"]
        dataDF.loc[index, "Post Time"] = post["timestamp"]
        dataDF.loc[index, "Post Likes"] = post["likes"]
        dataDF.loc[index, "# Post Comments"] = post["comments"]
        dataDF.loc[index, "# Post Shares"] = post["shares"]
        dataDF.loc[index, "Comment Text"] = str(post["comments_full"])


        #Dictionary Format
        # Key: CommenterID;; Comment Text;; Comment DateTime
        dictKey = ""
        dictValue = ""

        # Key is the value of the parent comment
        # Value is the replies to the comment
        for entry in post["comments_full"]:
            dictKey = entry["commenter_id"] + ";;" + entry["comment_text"] + ";;" + (str(entry["comment_time"].timestamp()))
            # print(dictKey)
            
            # Navigate through replies
            for item in entry["replies"]:
                dictValue += item["commenter_id"] + ";;" + item["comment_text"] + ";;" + (str(item["comment_time"].timestamp())) + "!*!"
                
            commentsDict[dictKey] = dictValue
        
        dataDF.loc[index, "Comment Text"] = str(commentsDict)
        dataDF.to_excel("FILE PATH HERE") # Convert to XLSX -- converting to .csv was giving comma separation errors