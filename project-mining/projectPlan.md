## Trading Process

1. Adding funds in trading account
2. Access of funds to the bot
3. Access of live price data to the bot
4. Access to invest (selling and buying) in trading to the bot

## A Simple Bot

Since, I am going to mimick the process of getting the live price data with the process of reading the price values from a file over a fixed interval. So, I am going to use the phrase "reading data from file" in further steps.

1. Reading data from a file
2. Entering it into a function to get necessary data to make decision
	* Check if the data is sufficient
	* If sufficient, calculate the necessary data
	* And return it as json object
3. Act on the decision

## Terms of Generating Data

1. Fixed Term Data
3. Overall Term Data

## Necessary data to take decision

If I start feeding data to a function then what should I expect to make a decision to invest my fund?

What does Maths say, we can get from a number of data?

So, let's try to answer these Questions.

1. A number of data gives the idea of whether the price increasing or decreasing --- Profit or Loss
2. The rate of increasing and decreasing of the price --- the slope
3. Average of data over Fixed Term or Overall Term

## Different Variables and Constants inside the function

### Constants
1. Overall Term (Pseudo Constant)
### Variables
1. Duration of Fixed Term
2. Selling Loss %age
3. Selling Profit %age
4. Loss Buying %age
5. Profit Buying %age (should be in rare for now from my understanding till now)
5. Confidence rate in currency


