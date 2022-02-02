#!/usr/bin/python3
from brownie import PriceFeedConsumer
import csv

def predictionDataWriter(inputFromBot):
    with open('PriceFeed.csv', 'a', newline='') as deepLearningTrainer:
      trainer = csv.writer(deepLearningTrainer)
      try:
        if len(str(inputFromBot))>1 and float(inputFromBot)==True:
          trainer.writerow([inputFromBot])
        else:
          trainer.writerow([inputFromBot])
      except ValueError:
        if len(inputFromBot)>1:
          trainer.writerow([])

def main():
    price_feed_contract = PriceFeedConsumer[-1]
    print(f"Reading data from {price_feed_contract.address}")
    predictionDataWriter(price_feed_contract.getLatestPrice())
    print(price_feed_contract.getLatestPrice())
    return
