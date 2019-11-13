- In this project I set myself to make an accessible and dynamic dataset generator from youtube videos.

- The way this works is by inputing one or more keywords (if you wanna input more than one keyword then it needs to have a + sign between them with no spaces: keyword1+keyword2).

- When you enter one or more keywords and use all flags available, the program makes requests to youtube via youtube data api v3, then the results are converted to a pandas data frame, printed in the console, then prints number of rows and columns (shape), and finally converts and saves the data frame to a csv file and sends an Email with this file attached through SMTP.

- Because I lacked time I made it in a way that it takes sender and receiver email automatically using environment variables, for the same reason the api always returns 9 columns which are channelId', 'channelTitle', 'categoryId', 'title', videoId, viewCount, likeCount (if available), dislikeCount (if available), commentCount (if available).

- you can tell the program the number of rows to return with the -n flag, if this flag is ignored then the default value is 25 rows.

- the -sac (--showAllCols), -sc (--showColumn), -scvs (--saveCsv), -se (--sendEmail) flags are optional and if ignored they take the default value which is False.

- In the future (if there is time) I will be making all of these flags more flexible, and also will be adding more functionality and modularity.

Enjoy!
