## WQU MScFE Capstone Project: Developing an algorithmic retail trading system

### Setting up the dependencies

```console
pip install -r requirements.txt
```

### Running the trading strategy

```console
lean cloud push 
lean cloud backtest wqu-capstone --open
```
 Note: This requires the appropriate setup for running the LEAN backend on the Quantconnect platform. Kindly refer to the official documentation to get started: https://www.quantconnect.com/docs/v2/lean-cli/key-concepts/getting-started

### Relevant files

Inside the `wqu-capstone` folder you will find the following files of interest: `fundamental_data.py`, `main.py`, `run_config.py`, and `technical_data.py`.

- `fundamental_data.py` contains the FundamentalData class which is responsible to handle fundamental data of stocks.
- `main.py` runs our strategy on the Quantconnect cloud platform.
- `run_config.py` specifies the backtesting parameters.
- `technical_data.py` contains the TechnicalData class which is responsible to handle technical data of stocks.