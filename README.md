# Google Trends MCP Implementation

This project implements Market Constraint Parameters (MCP) for Google Trends data retrieval, providing a structured way to analyze market trends with specific regional, temporal, and categorical constraints.

## Features

- Configurable market constraints (region, timeframe, category)
- Interest over time analysis with optional normalization
- Related queries retrieval
- Regional interest analysis with multiple resolution options
- Built-in error handling and logging

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/google-trends-mcp.git
cd google-trends-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage Example

```python
from google_trends_mcp import GoogleTrendsMCP

# Initialize with specific market constraints
trends_mcp = GoogleTrendsMCP(
    region="US",
    timeframe="today 12-m",
    category=0  # 0 represents all categories
)

# Get interest over time for specific keywords
keywords = ["artificial intelligence", "machine learning"]
df = trends_mcp.get_interest_over_time(keywords)

# Get regional interest
regional_df = trends_mcp.get_regional_interest(keywords)

# Get related queries
related = trends_mcp.get_related_queries(keywords)
```

## Market Constraint Parameters

- **Region**: Geographic region for analysis (e.g., "US", "GB", "DE")
- **Timeframe**: Time period for analysis (e.g., "today 12-m", "today 3-m", "2022-01-01 2022-12-31")
- **Category**: Google Trends category ID (0 for all categories)
- **Language**: Host language for request (e.g., "en-US", "de-DE")
- **Timezone**: Timezone offset in minutes

## License

MIT License