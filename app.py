import streamlit as st

# Configure the page
st.set_page_config(page_title="Kalshi Bet Score Auto-Prompt", page_icon="⚡", layout="centered")

st.title("⚡ Kalshi 15-Min Bet Score Generator")
st.markdown("Enter your live market data below to instantly generate the Master Prompt.")

# Create a clean UI with columns for speed
col1, col2 = st.columns(2)

with col1:
    asset_name = st.text_input("Asset Name", value="HYPE")
    current_price = st.number_input("Current Price ($)", min_value=0.0000, value=38.12, format="%.4f")
    time_remaining = st.number_input("Time Remaining (mins)", min_value=1, max_value=15, value=10)
    
with col2:
    target_strike = st.number_input("Target Strike ($)", min_value=0.0000, value=38.50, format="%.4f")
    contract_price = st.number_input("Kalshi Contract Price ($)", min_value=0.01, max_value=0.99, value=0.45, step=0.01)

st.divider()

# Generate Button
if st.button("Generate Master Prompt", type="primary", use_container_width=True):
    
    # The Backend Prompt Template
    master_prompt = f"""Act as a binary options risk analyst. Evaluate a 15-minute Kalshi Crypto trade for **{asset_name}**.

**Current Context:**
* **Current Price:** ${current_price}
* **Target Strike:** ${target_strike}
* **Time Remaining:** {time_remaining} minutes
* **Kalshi Contract Price (Yes):** ${contract_price}

**Task:**
1. **Calculate the Implied Probability:** Analyze the ${contract_price} contract price vs actual market probability.
2. **Technical Check:** Analyze the 1-min and 5-min EMA and RSI. Is the trend moving toward or away from the strike?
3. **Volatility Check:** Based on the current ATR (Average True Range), is the target hit statistically likely in the remaining time?
4. **Order Book Check:** Are there 'Buy/Sell Walls' blocking the path to the strike?

**Output a 'Bet Score' (1-10) using this rubric:**
* **1-4 (Avoid):** High risk, low probability, or 'theta' (time decay) is too aggressive.
* **5-7 (Speculative):** 50/50 toss-up; requires strong momentum to hit.
* **8-10 (Safe/High Conviction):** Technicals, volume, and time all align with the strike.

**Final Verdict:** Provide the **Bet Score**, a **Yes/No recommendation**, and the **Max Entry Price** I should pay to keep the trade profitable."""
    
    st.success("Prompt Ready! Copy below and paste into your LLM.")
    
    # Display the prompt in a copyable code block
    st.code(master_prompt, language="markdown")
