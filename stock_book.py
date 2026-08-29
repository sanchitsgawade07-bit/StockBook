import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_icon="📈",page_title="Welcome to stock book")

st.title("📈 StockBook")
st.caption("To know about application visit sidebar which located at top left corner (>>).")
st.caption("Enter stock ticker,If information not found or N/A shown it means ticker is incorrect check it again.")
st.caption("In comparison tab for better evaluation and understanding switch to desktop view")
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
        st.text("To compare two stocks one should evaluate the terms like\n1)Valuation ratios \n2)Profitability & Performance \nFinancial Health & Risk \n4)Dividend & Returns \n5)Price Performance & HIstory")
        
tab1,tab2=st.tabs(["About stock","Compare two stock"])
with tab1:
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

with tab2:
    col_1,col_2=st.columns(2)
    col_3,col_4=st.columns(2)
    with col_1:
        stock1=st.text_input("Enter the ticker of 1st stock",value=None,placeholder="Enter the stock ticker")
    with col_2:
        stock2=st.text_input("Enter the ticker of 2st stock",value=None,placeholder="Enter the stock ticker")
    compare=st.button("Compare it",type='primary')

    if compare:
        with st.spinner("Loading Data..."):
            if stock1==None or stock2==None:
                st.info("Enter the stock ticker that to be compare")

            elif("error" in stock1 or "error" in stock2):
                st.error("Your input is incorrect check it")

            elif stock1==stock2:
                st.warning("Both ticker are same")

            else:
                stock_1=stock1.strip().upper()
                stock_2=stock2.strip().upper()
                info_1=yf.Ticker(stock_1)
                info_2=yf.Ticker(stock_2)

                dn_1=info_1.info.get("displayName") or info_1.info.get("longName") or info_1.info.get("shortName") or stock_1
                dn_2=info_2.info.get("displayName") or info_2.info.get("longName") or info_2.info.get("shortName") or stock_2
                cs_1=info_1.info.get("symbol",stock_1)
                cs_2=info_2.info.get("symbol",stock_2)
                ind_1=info_1.info.get("industry","N/A")
                ind_2=info_2.info.get("industry","N/A")
                sec_1=info_1.info.get("sector","N/A")
                sec_2=info_2.info.get("sector","N/A")
                con_1=info_1.info.get("country","N/A")
                con_2=info_2.info.get("country","N/A")
                fc_1=info_1.info.get("financialCurrency","N/A")
                fc_2=info_2.info.get("financialCurrency","N/A")
                marcap_1=info_1.info.get("marketCap","N/A")
                marcap_2=info_2.info.get("marketCap","N/A")
                
                if isinstance(marcap_1,(int,float)):
                    marcap=f"{marcap_1:,}"

                if isinstance(marcap_2,(int,float)):
                    marcap=f"{marcap_2:,}"
                st.divider()
                column_1,column_2=st.columns(2)

                st.subheader("🏢 Company Info")
                with column_1:
                    with st.container(border=True):
                        st.subheader(f"▶️ Company Info of {dn_1}")
                        st.write(f"Name of company:-{dn_1}  \nSymbol of stock:-{cs_1}  \nSector:-{sec_1}  \nIndustry:-{ind_1}  \nCountry:-{con_1}  \nFinancial currency:-{fc_1}  \nMarket capital:-{marcap_1}")

                with column_2:    
                    with st.container(border=True):
                        st.subheader(f"▶️ Company Info of {dn_2}")
                        st.write(f"Name of company:-{dn_2}  \nSymbol of stock:-{cs_2}  \nSector:-{sec_2}  \nIndustry:-{ind_2}  \nCountry:-{con_2}  \nFinancial currency:-{fc_2}  \nMarket capital:-{marcap_2}")

                st.divider()
                #valuation ratios
                pe1,fe1=info_1.info.get("trailingPE"),info_1.info.get("forwardPE")
                pe2,fe2=info_2.info.get("trailingPE"),info_2.info.get("forwardPE")
                pb1=info_1.info.get("priceToBook")
                pb2=info_2.info.get("priceToBook")
                peg1=info_1.info.get("pegRatio")
                peg2=info_2.info.get("pegRatio")
                #return of equity
                roe1=info_1.info.get("returnOnEquity")
                roe2=info_2.info.get("returnOnEquity")
                gm1,om1,pm1=info_1.info.get("grossMargins"),info_1.info.get("operatingMargins"),info_1.info.get("profitMargins")
                gm2,om2,pm2=info_2.info.get("grossMargins"),info_2.info.get("operatingMargins"),info_2.info.get("profitMargins")
                eps1=info_1.info.get("trailingEps")
                eps2=info_2.info.get("trailingEps")
                #financial heath and risk
                de1=info_1.info.get("debtToEquity")
                de2=info_2.info.get("debtToEquity")
                cr1=info_1.info.get("currentRatio")
                cr2=info_2.info.get("currentRatio")
                #dividend returns
                dy1=info_1.info.get("dividendYield")
                dy2=info_2.info.get("dividendYield")
                dpr1=info_1.info.get("payoutRatio")
                dpr2=info_2.info.get("payoutRatio")
                #price performance and history
                wh1,wl1=info_1.info.get("fiftyTwoWeekHigh"),info_1.info.get("fiftyTwoWeekLow")                
                wh2,wl2=info_2.info.get("fiftyTwoWeekHigh"),info_2.info.get("fiftyTwoWeekLow")                

                st.subheader("📈 Valuation Ratios")
                colvr1,colvr2=st.columns(2)
                with colvr1:
                    with st.container(border=True):
                        st.subheader(f"Valuation Ratios of {stock_1}")
                        st.metric(label="Price-to-Earnings(P/E)[Trailing]",value=f"{pe1}")
                        st.metric(label="Price-to-Earnings(P/E)[Forward]",value=f"{fe1}")
                        st.metric(label="Price-to_Book",value=f"{pb1}")
                        st.metric(label="PEG Ratio",value=f"{peg1}")

                with colvr2:
                    with st.container(border=True):
                        st.subheader(f"Valuation Ratios of {stock_2}")
                        st.metric(label="Price-to-Earnings(P/E)[Trailing]",value=f"{pe2}")
                        st.metric(label="Price-to-Earnings(P/E)[Forward]",value=f"{fe2}")
                        st.metric(label="Price-to_Book",value=f"{pb2}")
                        st.metric(label="PEG Ratio",value=f"{peg2}")

                st.divider()
                st.subheader("💡 Profitability & Performance")
                colpp1,colpp2=st.columns(2)
                with colpp1:
                    with st.container(border=True):
                        st.subheader(f"Profitability & Perfromance of {stock_1}")
                        st.metric(label="Return of Equity",value=f"{roe1}")
                        st.metric(label="Gross Margins",value=f"{gm1}")
                        st.metric(label="Operate Margins",value=f"{om1}")
                        st.metric(label="Profit Margins",value=f"{pm1}")
                        st.metric(label="Earnings Per Share",value=f"{eps1}")

                with colpp2:
                    with st.container(border=True):
                        st.subheader(f"Profitability & Perfromance of {stock_2}")
                        st.metric(label="Return of Equity",value=f"{roe2}")
                        st.metric(label="Gross Margins",value=f"{gm2}")
                        st.metric(label="Operate Margins",value=f"{om2}")
                        st.metric(label="Profit Margins",value=f"{pm2}")
                        st.metric(label="Earnings Per Share",value=f"{eps2}")

                st.divider()
                st.subheader("⚠️ Financial Health & Risk")
                colfr1,colfr2=st.columns(2)
                with colfr1:
                    with st.container(border=True):
                        st.subheader(f"Financial Health & Risk of {stock_1}")
                        st.metric(label="Debt-to_Equity",value=f"{de1}")
                        st.metric(label="Current Ratio",value=f"{cr1}")

                with colfr2:
                    with st.container(border=True):
                        st.subheader(f"Financial Health & Risk of {stock_2}")
                        st.metric(label="Debt-to_Equity",value=f"{de2}")
                        st.metric(label="Current Ratio",value=f"{cr2}")

                st.divider()
                st.subheader("📍 Dividend & Returns")
                coldr1,coldr2=st.columns(2)
                with coldr1:
                    with st.container(border=True):
                        st.subheader(f"Dividends & Returns of {stock_1}")
                        st.metric(label="Dividend Yield",value=f"{dy1}")
                        st.metric(label="Dvividend Payout Ratio",value=f"{dpr1}")

                with coldr2:
                    with st.container(border=True):
                        st.subheader(f"Dividends & Returns of {stock_2}")
                        st.metric(label="Dividend Yield",value=f"{dy2}")
                        st.metric(label="Dvividend Payout Ratio",value=f"{dpr2}")

                st.divider()
                st.subheader("🔎 Price Performance & History")
                colph1,colph2=st.columns(2)
                with colph1:
                    with st.container(border=True):
                        st.subheader(f"Price Performance & History of {stock_1}")
                        st.metric(label="52-Week of High",value=f"{wh1}")
                        st.metric(label="52-Week of Low",value=f"{wl1}")

                with colph2:
                    with st.container(border=True):
                        st.subheader(f"Price Performance & History of {stock_2}")
                        st.metric(label="52-Week of High",value=f"{wh2}")
                        st.metric(label="52-Week of Low",value=f"{wl2}")
                colg1,colg2=st.columns(2)
                with colg1:
                    with st.container(border=True):
                        st.caption("Last 1 year closing value status")
                        data=info_1.history(period="1y")
                        close_data=data["Close"]
                        st.line_chart(close_data,x_label="Stock Price",y_label="Value in country currency")

                with colg2:
                    with st.container(border=True):
                        st.caption("Last 1 year closing value status")
                        data=info_2.history(period="1y")
                        close_data=data["Close"]
                        st.line_chart(close_data,x_label="Stock Price",y_label="Value in country currency")
                        

                        