````markdown
# Trading Bot – Binance Futures Testnet

## Overview

This project is a simplified Python trading bot that interacts with the Binance Futures Testnet (USDT-M). It supports placing market and limit orders using a clean layered architecture with validation, structured logging, and a CLI interface.

The goal is to demonstrate backend engineering skills including API integration, system design, error handling, and production-style Python structure.

---

## Architecture

The system follows a layered design:

CLI Layer → Order Service Layer → API Client Layer → Binance Futures API

Modules:
- bot/cli.py → Command line interface
- bot/orders.py → Business logic layer
- bot/client.py → Binance API wrapper
- bot/validators.py → Input validation
- bot/logging_config.py → Structured logging

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Binance Futures Testnet (USDT-M)
- CLI interface using Typer
- Input validation (side, quantity, price)
- Structured logging to file
- Error handling for API and network failures
- Clean modular architecture

---

## Setup Instructions

### 1. Clone repository
```bash
git clone <your-repo-url>
cd trading_bot
````

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

## Usage

### Check account balance

```bash
python bot/cli.py account
```

### Place MARKET order

```bash
python bot/cli.py market BTCUSDT BUY 0.01
```

### Place LIMIT order

```bash
python bot/cli.py limit BTCUSDT SELL 0.01 30000
```

---

## Logging

All logs are written to:

trading_bot.log

Logs include:

* order requests
* order responses
* errors
* execution status

Example log:

```json
{"timestamp":"2026-06-01T12:10:22","level":"INFO","message":"MARKET ORDER | BTCUSDT | BUY | qty=0.01"}
```

---

## Error Handling

The system handles:

* invalid input validation errors
* Binance API exceptions
* network failures

All errors are logged and shown in CLI output.

---

## Design Decisions

* Layered architecture (CLI → Service → Client)
* Separation of concerns
* Centralized validation layer
* File-based structured logging
* Stateless API client wrapper
* Testnet-only execution for safety

---

## Project Structure

trading_bot/
bot/
cli.py
orders.py
client.py
validators.py
logging_config.py
trading_bot.log
requirements.txt
README.md

---

## Notes

* Uses Binance Futures Testnet only
* No real funds are used
* Designed for technical assessment and portfolio demonstration

---

## Author

Built as a backend engineering project demonstrating:

* API integration
* system design
* observability
* production-grade Python structure

```

---
```
