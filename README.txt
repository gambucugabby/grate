Requirements:
Python 2.7.10
pip (so as to install)
Flask
flask_restful
Jsonify
CURL (optional for testing)

----------------------
Did this fast.  Known Issues:
-does not trap errors from post
-No error handling even though Erlog has a function for it
-Same as above for escaping algoritim (I hang my head in shame)
-Service return is JSON-ic, but not perfect.
----------------------

For phase 1:
run:
python main.py
Demonstrates input of the 3 file times, and then all 3 at once.  Uses the included
test data from: CommaDelimited, PipeDelimited and SpaceDelimited

For phase 2:
run:
python GrateRest.py
Starts the webservice using flask.

Navigate to:
http://localhost:1234/people/gender
http://localhost:1234/people/birthday
http://localhost:1234/people/name
To demonstrate JSON formatted return of data as specified.

To demonstrate put use CURL, or whatever, and input the following:
curl -X POST -i http://localhost:1234/people --data '{
"firstname":"Dead",
"lastname":"Pool",
"color":"red",
"gender":"M",
"birthday":"1/1/1972"
}'
