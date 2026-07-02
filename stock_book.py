import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_icon="📈",page_title="Welcome to stock book")

st.title("📈 StockBook")
st.caption("To know about application visit sidebar which located at top left corner (>>).")
st.caption("Enter stock ticker, information not found or N/A shown it means ticker is incorrect check it again.")
side=st.sidebar
if side:
    with st.sidebar:
        st.title("❔What's inside")
        st.write("In this application you can get real time data of particular stock.")
        st.write("To get data of any stock you have to enter ticker of specific stock.")
        st.caption("List of some of the national and international stock ticker.")
        tick={"Company Name":["Microsoft","Amazon","Tesla","TCS","Reliance"],"Ticker":["MSFT","AMZN","TSLA","TCS.NS","RELIANCE.NS"]}
        df=pd.DataFrame(tick)
        df.index=[1,2,3,4,5]
        st.write(df)
        st.text("For indian stocks NSE(National Stock Exchange) and BSE(Bombay Stock Exchange) is use as NS and BS respectively.")

a=st.text_input("Enter ticker of stock",placeholder="Enter ticker (eg.:-MSFT,RELIANCE.NS)")
shows=st.button("Get Stock Info",type="primary")
if shows:
    try:
        with st.spinner("Loading Data..."):
            if a=="":
                st.info("Please enter ticker of stock")

            elif "error" in a:
                st.error("Entered ticker is invalid,enter valid ticker")

            else:
                    stock=a.strip().upper()
                    infor=yf.Ticker(stock)
                    dn=infor.info.get("displayName") or infor.info.get("longName") or infor.info.get("shortName") or stock
                    cs=infor.info.get("symbol",stock)
                    ind=infor.info.get("industry","N/A")
                    sec=infor.info.get("sector","N/A")
                    con=infor.info.get("country","N/A")
                    fc=infor.info.get("financialCurrency","N/A")
                    marcap=infor.info.get("marketCap","N/A")

                    if isinstance(marcap,(int,float)):
                        marcap=f"{marcap:,}"
                    st.subheader("Company Info")
                    st.write(f"Name of company:-{dn}  \nSymbol of stock:-{cs}  \nSector:-{sec}  \nIndustry:-{ind}  \nCountry:-{con}  \nFinancial currency:-{fc}  \nMarket capital:-{marcap}")
                    
                    st.divider()
                    
                    st.subheader(f"{dn} stock data (all value in country currency)")
                    cp=infor.info.get("currentPrice") or infor.info.get("regularMarketPrice") or infor.info.get("previousClose")
                    dh=infor.info.get("dayHigh",cp)
                    dl=infor.info.get("dayLow",cp)
                    op=infor.info.get("open",cp)

                    col1,col2=st.columns(2)
                    with col1:
                        st.metric(label="Current price",value=f"{cp}")
                    with col2:
                        st.metric(label="Today's opening price",value=f"{op}")
                    
                    col3,col4=st.columns(2)
                    with col3:
                        st.metric(label="Today's highest price",value=f"{dh}")
                    with col4:
                        st.metric(label="Today's lowest price",value=f"{dl}")

                    st.divider()
                    st.header("Last one year data of stock(Graphical representation)")
                    st.subheader("Last one year closing value status")
                    st.caption("Here, Close represents closing value or adjusted final value of stock over last one year.")

                    data=infor.history(period="1y")
                    close_data=data["Close"]
                    st.line_chart(close_data,x_label="Stock Price",y_label="Value in country currency")
                    st.divider()
                    st.subheader("Last one year all values status")
                    st.caption("""Here, Open, High, Low, and Close represents daily market values and activity of stock over 
                               last one year.""")
                    
                    all_data=data[["Close","High","Low","Open"]]
                    st.bar_chart(all_data,x_label="Stock all values",y_label="Values in country currency",color=["#004B49","#45B69c","#EE6C4D","#F4E285"])
                    
    except KeyError:
         st.error("Not able to find data")

    