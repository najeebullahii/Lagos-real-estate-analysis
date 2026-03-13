# Lagos Real Estate Intelligence — Web Scraping & Investment Analysis

**Live Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)

**Data source:** Nigeria Property Centre — 1,993 properties scraped, cleaned, and analysed across Lagos State.

---

## Overview

Lagos real estate data is fragmented and unreliable. If you want to know whether ₦500 million is a fair price for a property in Lekki, or what the typical rent is for a three-bedroom in Ikoyi, there is no straightforward way to find out. Buyers rely on agents, investors rely on hearsay, and renters have no reference point at all.

This project addresses that gap. Using Python to scrape live property listings from Nigeria Property Centre, followed by three rounds of data cleaning and a full Tableau dashboard, it delivers a data-driven picture of the Lagos property market — pricing benchmarks, investment yields, bedroom demand, and geographic concentration — across the city's major neighbourhoods.

The headline finding: investment returns vary by a factor of 30 within the same city, from 9.3% annual yield in Ibeju Lekki to 0.3% in Ikorodu.

---

## What This Project Is About

This is an end-to-end data project — from web scraping raw property listings to building an interactive dashboard that answers real investment questions. The goal was to replace guesswork with data in a market where most people make six and seven figure decisions based on what their agent tells them or what they heard from friends.

The project covers the full pipeline: automated data collection using Python, three rounds of cleaning to produce a reliable dataset, and a Tableau dashboard with 11 visualisations covering pricing benchmarks, investment yields, bedroom demand, and geographic concentration across Lagos.

---
## Dashboard Preview

![Lagos Real Estate Dashboard Overview](https://raw.githubusercontent.com/najeebullahii/Lagos-real-estate-analysis/main/assets/dashboard_overview.png)

*The full interactive dashboard is available on Tableau Public. The screenshot above shows the investment opportunity scatter plot, KPI metrics, and area-level price comparisons.*

---

## Business Questions Answered

The analysis was structured around three distinct user types:

**For investors**
- Which areas deliver the strongest rental yield?
- Where does purchase price outpace rental income to the point of making investment impractical?
- How does the overall market compare in terms of sale-to-rent ratio?

**For buyers**
- Is the asking price for a property in a given area reasonable relative to the market?
- What is the typical price range for a four-bedroom property in Lekki versus Ikoyi?

**For renters**
- What should a three-bedroom apartment in Yaba or Maryland realistically cost?
- Which areas offer the best value for rental accommodation?

---

## Key Findings

**Best investment areas by annual rental yield:**

| Rank | Area | Annual Yield |
|---|---|---|
| 1 | Ibeju Lekki | 9.3% |
| 2 | Yaba | 9.1% |
| 3 | Maryland | 5.2% |

**Areas with the weakest investment case:**

| Rank | Area | Annual Yield | Years to break even |
|---|---|---|---|
| 1 | Ikorodu | 0.3% | 322 years |
| 2 | Surulere | 1.1% | 91 years |
| 3 | Agege | 1.3% | 77 years |

---

## Key Insights

**Geographic inequality is the dominant story.** A 30x difference in investment returns within a single city tells you that location matters far more than property type or size. Two properties with identical bedrooms and finishes can have completely different investment cases depending on which side of Lagos they sit on.

**Premium pricing does not guarantee strong returns.** Ikoyi commands the highest average sale price in the dataset at ₦1.66 billion, yet delivers only 2.2% annual yield. Buyers in that market are paying for prestige and address, not cash flow. Investors chasing returns should be looking at Ibeju Lekki and Yaba instead.

**The market is heavily concentrated.** Lekki accounts for nearly half of all listings in the dataset. Whether this reflects genuine demand depth or an oversaturated supply is a question the listing data alone cannot answer — sales velocity and time-on-market data would be needed to draw that conclusion with confidence.

**Data cleaning changed the story significantly.** Before the final round of outlier removal, average annual rent appeared to be ₦23 million. After removing statistical outliers, it corrected to ₦15 million — a 35% shift. This underscores how sensitive market averages are to extreme values, and why cleaning decisions need to be documented and justified rather than hidden.

---

**Market overview:**

- 1,993 properties analysed — 1,144 for sale, 687 for rent
- Average sale price: ₦580 million
- Average annual rent: ₦15 million
- Lekki accounts for 47% of all listings

**Notable insight:** Ikoyi carries the highest average sale price at ₦1.66 billion but delivers only 2.2% annual yield — one of the weakest in the dataset. The premium reflects prestige, not cash flow.

**Geographic concentration:** A single neighbourhood — Lekki — dominates nearly half of all listings. Whether this reflects genuine demand or market oversaturation cannot be determined from listing data alone; sales velocity data would be required to draw that conclusion.

---

## How It Was Built

### Data Collection

2,138 property listings were scraped from Nigeria Property Centre using Python with Playwright and BeautifulSoup. The scraper extracted listing titles, prices, and addresses for residential properties across Lagos State.

### Data Cleaning

The raw dataset required three rounds of cleaning to produce an analysis-ready file.

| Round | Focus | Key Actions |
|---|---|---|
| Round 1 | Feature engineering | Extracted bedroom counts and property types from titles using regex. Decomposed addresses into neighbourhood, area, and state. Standardised all prices to Nigerian Naira. Categorised listings as Sale, Rent, or Short Let. |
| Round 2 | Outlier removal | Removed mislabelled listings — sale prices under ₦2 million that were clearly rentals. Filtered out commercial properties and implausible bedroom counts. Restricted dataset to Lagos State only. |
| Round 3 | Quality control | Removed extreme rental outliers that would distort area-level averages. Maximum rent dropped from ₦1.5 billion to ₦50 million. Average rent corrected from ₦23 million to ₦15 million — a 35% improvement in accuracy. Final count: 1,993 properties after removing 145 outliers. |

### Dashboard Construction

The Tableau dashboard contains 11 visualisations:

- KPI summary cards for market-level metrics
- Bar charts comparing top neighbourhoods by average sale and rental price
- Bedroom demand distribution analysis
- Investment opportunity scatter plot mapping yield against average price
- Dual-axis chart combining price-to-rent ratios with annual yields

Level of Detail (LOD) expressions were used throughout to calculate area-level aggregates — average prices, rental yields, and price-to-rent ratios — independently of the visualisation's own level of aggregation.

---

## Project Structure
```
Lagos-real-estate-analysis/
├── assets/                        # Screenshots and dashboard images
├── dashboard/                     # Tableau workbook file
├── data/
│   ├── raw/                       # Original scraped data
│   └── cleaned/                   # Analysis-ready dataset
├── scripts/
│   ├── web_scraping.py            # Playwright + BeautifulSoup scraper
│   └── Lagos_data_cleaning.py     # Three-round cleaning pipeline
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Technology Stack

| Component | Technology |
|---|---|
| Web scraping | Python — Playwright, BeautifulSoup |
| Data cleaning | Python — Pandas |
| Analysis and visualisation | Tableau Desktop / Tableau Public |
| Version control | Git and GitHub |

**Python library versions:**
```
pandas==2.0.3
playwright==1.40.0
beautifulsoup4==4.12.2
```

---

## Running the Code Locally

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install Playwright browsers:
```bash
playwright install chromium
```
4. Run the scraper (optional — cleaned data is already included):
```bash
python scripts/web_scraping.py
```
5. Run the cleaning pipeline:
```bash
python scripts/Lagos_data_cleaning.py
```
6. Open the Tableau dashboard locally or view the live version on [Tableau Public](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)

---

## Limitations

This analysis is intentionally transparent about what the data cannot tell us:

- The dataset represents a single point in time, not a longitudinal price trend
- Only listed properties are included — actual transaction prices from the land registry would be more reliable
- There is no way to verify whether listings reflect genuine market prices or aspirational asking prices
- Time-on-market data is unavailable, making it impossible to assess demand or liquidity
- Contextual factors — neighbourhood amenities, infrastructure quality, crime rates, proximity to schools — are not captured

A more complete analysis would track listings over time, incorporate land registry transaction data, and combine property-level data with neighbourhood-level socioeconomic indicators.

---

## License

MIT License — free to use and adapt for your own projects.

---

## Data Source

Nigeria Property Centre: [nigeriapropertycentre.com](https://nigeriapropertycentre.com)

*Last updated: February 2026*
