# great recession portfolio analyzer

![80-20 portfolio starting at $1M USD](https://github.com/xMNG/great_recession_portfolio_analyzer/blob/master/images/80-20.png) 


What if you retired right before the great recession? What would your withdrawals look like? This tool backtests your chosen allocation between Vanguard's Total Stock Market Index Fund Admiral Shares (VTSAX) or Vanguard's Total Bond Market Index Fund Admiral Shares (VBTLX). 

This tool was inspired by reddit's r/FIRE, r/leanfire, and r/personalfinance subreddits. Also inspired by a recent post on the bogleheads forums. And lastly, inspired by the recent declines in the market.

![output data](https://github.com/xMNG/great_recession_portfolio_analyzer/blob/master/images/80-20_cmd.PNG) 

### How to use:
1. Clone repo
2. `python portfolio_analysis.py --help` for usage
- `--sb=100000` for 100,000 starting balance
- `--ea=.8` for 80-20 equity to bond weight
- `--wr=.04` for 4% withdrawal rate (Safe withdrawal rate! hotly debated...)
- `--rb` for rebalancing after withdrawal at the beginning of each year

### To do

- Add inflation
- Add quarterly data
- Add csv/openpyxl support
- Add cosmetic improvements
- Anything else that is requested!