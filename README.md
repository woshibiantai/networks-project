# networks-project
50.012 Networks Project

## Team Members 
Aditya Manikashetti, Jonathan Bei, Monica Nathalia, Ruth Wong


## Our Idea
Create a HTTP proxy server that allows the administrator (who sets up the server) to selectively modify the response message from the internet before returning it to the original requester. A possible use case for this would be when parents want to filter out what their child can see (e.g. censoring vulgarities), or an institution that would like to restrict access to certain websites for their users. (e.g. no memes)

## Our Plan
We will develop a HTTP proxy server in Python, setup to be accessed on localhost or remotely. Upon initiation, the server will take in a JSON file as argument. The JSON file will contain a dictionary that specifies which strings should be modified to what. For example, {“cats”: ”dogs”, “apple”: “samsung”} will modify the keys (“cats” and “apple”) to the corresponding value (“dogs” and “samsung”). The JSON file will also contain a list of strings that specifies which URLs to blacklist. When blacklisted URLs are requested, the proxy will always respond with an 404 error code. 

## Our Deliverables
The proxy server, with a simple GUI or CLI. 
A demonstration on how to setup the proxy server, along with a sample JSON containing the dictionary and a list of blacklisted sites (both of which can be modified by the proxy administrator)  
A demonstration of how our proxy modifies strings to be returned to the user and deals with blacklisted sites, through a web browser or from the terminal.
