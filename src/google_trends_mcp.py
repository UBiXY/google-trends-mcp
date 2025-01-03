from pytrends.request import TrendReq
from datetime import datetime, timedelta
import pandas as pd
from typing import Dict, List, Optional, Union
import logging

class GoogleTrendsMCP:
    """Market Constraint Parameters (MCP) implementation for Google Trends data retrieval"""
    
    def __init__(
        self,
        region: str = "US",
        timeframe: str = "today 12-m",
        category: int = 0,
        hl: str = "en-US",
        timezone: int = 240
    ):
        self.pytrends = TrendReq(hl=hl, tz=timezone)
        self.region = region
        self.timeframe = timeframe
        self.category = category
        self.logger = logging.getLogger(__name__)
        
    def build_payload(self, keywords: List[str]) -> None:
        try:
            self.pytrends.build_payload(
                kw_list=keywords,
                cat=self.category,
                timeframe=self.timeframe,
                geo=self.region
            )
        except Exception as e:
            self.logger.error(f"Error building payload: {str(e)}")
            raise
    
    def get_interest_over_time(
        self,
        keywords: List[str],
        normalize: bool = True
    ) -> pd.DataFrame:
        self.build_payload(keywords)
        try:
            df = self.pytrends.interest_over_time()
            if normalize and not df.empty:
                df = df.apply(lambda x: (x - x.min()) / (x.max() - x.min()) * 100)
            return df
        except Exception as e:
            self.logger.error(f"Error getting interest over time: {str(e)}")
            raise
            
    def get_related_queries(
        self,
        keywords: List[str]
    ) -> Dict[str, Dict[str, pd.DataFrame]]:
        self.build_payload(keywords)
        try:
            return self.pytrends.related_queries()
        except Exception as e:
            self.logger.error(f"Error getting related queries: {str(e)}")
            raise
            
    def get_regional_interest(
        self,
        keywords: List[str],
        resolution: str = 'COUNTRY'
    ) -> pd.DataFrame:
        self.build_payload(keywords)
        try:
            return self.pytrends.interest_by_region(resolution=resolution)
        except Exception as e:
            self.logger.error(f"Error getting regional interest: {str(e)}")
            raise