import requests
import json
import time

deck_of_cards_api_url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
insights_api_url = "https://insights-collector.newrelic.com/v1/accounts/<ACCOUNT ID>/events"
insights_key = "<PASTE YOUR INSIGHTS KEY>"
eventName = "DeckOfCardsAPI"

def get_api_response(url):
      response = requests.get(url)
      return response.json()

def send_data_to_new_relic():
      
      h = {
            "Content-Type" : "application/json",
            "Api-Key" : insights_key
      }
      
      api_response = get_api_response(deck_of_cards_api_url)
      api_response["eventType"] = eventName
      d = api_response
      
      response = requests.post(
            url= insights_api_url,
            headers = h,
            data = json.dumps(d)
      )
      
      if response.status_code == 200:
            print("DATA SENT SUCCESSFULLY TO NEW RELIC")
      else:
            print("ERROR WHILE SENDING DATA TO NEW RELIC")
            

while True:
      send_data_to_new_relic()
      time.sleep(5)