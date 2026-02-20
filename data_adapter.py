from typing import Dict, Any
import requests

class DataAdapter:
    def __init__(self):
        self.session = requests.Session()
        self.config = Config()

    def fetch_data(self) -> Dict[str, Any]:
        """Fetch financial data from connected platforms."""
        data = {}
        for source in self.config.get_data_sources():
            if source == "TurboTax":
                data.update(self._fetch_turbotax_data())
            elif source == "QuickBooks":
                data.update(self._fetch_quickbooks_data())
        return data

    def _fetch_turbotax_data(self) -> Dict[str, Any]:
        """Fetch data from TurboTax API."""
        try:
            response = self.session.get("https://api.turbotax.com/financial-data")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error fetching TurboTax data: {e}")
            raise

    def _fetch_quickbooks_data(self) -> Dict[str, Any]:
        """Fetch data from QuickBooks API."""
        try:
            response = self.session.get("https://api.quickbooks.com/financial-data")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error fetching QuickBooks data: {e}")
            raise