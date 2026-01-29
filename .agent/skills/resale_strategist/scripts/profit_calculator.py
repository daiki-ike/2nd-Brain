import argparse

def calculate_profit(purchase_price, selling_price, fba_fee=0, shipping_cost=0):
    """
    Calculates profit and margin.
    Simple logic: Profit = Selling - (Purchase + Fees + Shipping)
    *Note: Tax calculation simplified for now.
    """
    # Amazon Referral Fee (Category dependent, approx 10% average)
    referral_fee = selling_price * 0.10
    
    total_cost = purchase_price + referral_fee + fba_fee + shipping_cost
    profit = selling_price - total_cost
    margin = (profit / selling_price) * 100 if selling_price > 0 else 0
    break_even = total_cost / 0.9 # Very rough estimate assuming 10% fee

    return {
        "purchase": purchase_price,
        "selling": selling_price,
        "fees": referral_fee + fba_fee + shipping_cost,
        "profit": profit,
        "margin": margin,
        "break_even": break_even
    }

def main():
    parser = argparse.ArgumentParser(description="Calculate Resale Profit")
    parser.add_argument("--buy", type=int, required=True, help="Purchase Price")
    parser.add_argument("--sell", type=int, required=True, help="Estimated Selling Price")
    parser.add_argument("--fba", type=int, default=500, help="FBA/Shipping Fee (Default: 500)")
    
    args = parser.parse_args()
    
    result = calculate_profit(args.buy, args.sell, fba_fee=args.fba)
    
    print(f"--- Profit Calculation ---")
    print(f"Buy:  ¥{result['purchase']:,}")
    print(f"Sell: ¥{result['selling']:,}")
    print(f"Fees: ¥{result['fees']:,.0f} (Referral+FBA)")
    print(f"--------------------------")
    print(f"Profit: ¥{result['profit']:,.0f}")
    print(f"Margin: {result['margin']:.1f}%")
    print(f"BreakEven: ~¥{result['break_even']:,.0f}")
    print(f"--------------------------")
    
    if result['margin'] >= 20:
        print("[Judgment] ✅ GO (High Margin)")
    elif result['margin'] >= 10:
        print("[Judgment] ⚠️ CAUTION (Check rotation)")
    else:
        print("[Judgment] ❌ NO GO (Low Margin)")

if __name__ == "__main__":
    main()
