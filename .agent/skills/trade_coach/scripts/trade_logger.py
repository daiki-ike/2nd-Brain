import argparse
import datetime
import os

def log_trade(symbol, pnl, reason, emotion, log_path):
    """
    Appends trade log to the daily note.
    """
    timestamp = datetime.datetime.now().strftime("%H:%M")
    
    # Format the log entry
    entry = f"""
*   **{timestamp} {symbol} (¥{pnl})**:
    *   **Reason**: {reason}
    *   **Emotion**: {emotion}
"""
    
    # Check if file exists
    if not os.path.exists(log_path):
        print(f"[Error] Log file not found: {log_path}")
        return False
        
    # Append to file
    # Note: In a real agent scenario, we might want to insert this intelligently under a specific header using tool calls,
    # but for a simple script, appending or using file manipulation tools is better.
    # Here, we print the formatted string so the Agent can use its `insert_content` tool capability to place it correctly.
    
    print("--- Formatted Entry ---")
    print(entry)
    print("-----------------------")
    return True

def main():
    parser = argparse.ArgumentParser(description="Log Trade Entry")
    parser.add_argument("--symbol", required=True, help="Stock Symbol")
    parser.add_argument("--pnl", required=True, help="Profit/Loss")
    parser.add_argument("--reason", required=True, help="Entry Reason")
    parser.add_argument("--emotion", required=True, help="Emotional State")
    
    # Daily Note Path (Dynamic based on today)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    log_path = f"c:\\Users\\daiki\\Product\\2nd-Brain\\2nd-Brain\\05_日誌\\{today}.md"
    
    args = parser.parse_args()
    
    log_trade(args.symbol, args.pnl, args.reason, args.emotion, log_path)

if __name__ == "__main__":
    main()
