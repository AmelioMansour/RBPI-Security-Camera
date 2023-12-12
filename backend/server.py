from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy import text
from google.cloud.sql.connector import Connector
import pymysql
import os
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)



# Database configuration
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\ameli\\OneDrive\\Desktop\\my-app\\backend\\mansour-priv.json"
INSTANCE_CONNECTION_NAME = 'mansour-4160-f23:us-central1:database2'
DB_USER = 'database2'
DB_PASS = 'apple!'
DB_NAME = 'milestone4'

#test
# Check if the file exists
if os.path.exists(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]):
    print("Credential file found.")
else:
    print("Credential file not found. Path:", os.environ["GOOGLE_APPLICATION_CREDENTIALS"])


# Set up Google Cloud SQL connector
connector = Connector()

def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

# Create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

@app.route('/api/videos', methods=['GET'])
def get_videos():
    try:
        with pool.connect() as conn:
            query = text("SELECT URL FROM Videos")  # Adjust based on your table structure
            result = conn.execute(query)
            
            # Extract URLs from the result
            videos = [row[0] for row in result]
            print(videos)
            # Return the URLs as a JSON response
            return jsonify(videos)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Error fetching video data"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Runs the server on port 5000
