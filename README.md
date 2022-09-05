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
Currently, the code prints the email content in stdout.

