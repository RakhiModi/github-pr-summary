# github-pr-summary


Code to use the GitHub API to retrieve a summary of all opened, closed, and in progress pull requests in the 
last week for a given repository and send a summary email to a configurable email address.

To build image: 
``
docker build -t  <REGISTRY_NAME>/<IMAGE_NAME>:<VERSION_TAG> .
``

To run:

``
docker run -d <REGISTRY_NAME>/<IMAGE_NAME>:<VERSION_TAG>
``


Update:
The branch PR-result-export has the solution. 
Currently, the code prints the email content in console/STDOUT.


I was trying to send an email as well, but I was facing issues with authentication and I tried but was not able to fix it before deadline. 
The functions create_html_table() and send_mail() was written as part of that. which is not tested because of the auth issues. 



