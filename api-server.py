from flask import Flask, request, jsonify
from datetime import datetime
import pandas as pd
import json

app = Flask(__name__)

class GeneDataProcessor:

    def __init__(self):
        # Load data from the CSV file at initialization
        self.df = pd.read_csv('sample-data.csv')
        self.df['date'] = pd.to_datetime(self.df['date'], format='%m-%d-%Y')
    
    def healthCheck(self):
        """
        Health check endpoint to verify if the API is running fine.
        Returns: Tuple[Dict[str, Any], int]: A tuple containing a dictionary with the response data and an 
        HTTP status code.
        """
        response = {'status': 'success', 'message': 'API is running fine'}
        return jsonify(response), 200

    def getData(self):
        """
        API endpoint to process data based on the specified timestamp.
        Returns:
        Tuple[Dict[str, Any], int]: A tuple containing a dictionary with the response data and an HTTP status code.
        The response data dictionary contains the following keys:
            - 'status' (str)
            - 'message' (str)
            - 'data' (list of dict)
        """
        # Get the JSON data from the request
        data = request.get_json()

        # validate incoming structure
        if not self.validate_getData(data):
            return jsonify({"status": 'error', "message": "Invalid data structure"}), 400
        
        # extract time_stamp
        time_stamp = data["timestamp"]

        # process request based on timestamp
        result = self.processData(time_stamp)
        return jsonify(result)

    def processData(self, time_stamp):
        """
        Processes incoming request from source data
        Args: time_stamp: str
        Returns: Tuple[Dict[str, Any], int]
        """
        # filter source data based on request timestamp
        specific_date = pd.to_datetime(time_stamp, format='%m-%d-%Y')
        filtered_data = self.df[self.df['date'] == specific_date].to_dict(orient='records')
        
        # build response dictionary
        response = {
            'status': 'success',
            'message': 'Data processed successfully.',
            'data': filtered_data
        }
        
        return response, 200

    def validate_getData(self, data):
        """
        Validates the getData() response data structure and the timestamp format.
        Args: data (dict): The response data as a dictionary. 
        Returns: bool: True if the data structure is valid and the timestamp has the correct format, 
        False otherwise.
        """
        # validate the data structure
        if not isinstance(data, dict):
            return False

        # validate key
        if 'timestamp' not in data:
            return False
        date_format = "%m-%d-%Y"
        date_string = data['timestamp']
        # validate date_format
        try: 
            datetime.strptime(date_string, date_format)
            return True
        except ValueError as e:
            print('Error:', {e})
            return False
        
        return False

data_processor = GeneDataProcessor()

# added rules to map specified urls to the class methods
app.add_url_rule('/health', 'healthCheck', data_processor.healthCheck, methods=['GET'])
app.add_url_rule('/getData', 'getData', data_processor.getData, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
