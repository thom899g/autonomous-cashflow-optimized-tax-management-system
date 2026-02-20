import logging
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_module import AIEngine
from data_adapter import DataAdapter
from config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TaxData(BaseModel):
    income: float
    expenses: float
    deductions: Optional[float] = None

class TaxManagementSystem:
    def __init__(self, config: Config):
        self.config = config
        self.ai_engine = AIEngine()
        self.data_adapter = DataAdapter()

    def process_tax_data(self, tax_data: TaxData) -> dict:
        """Process and optimize tax data using AI engine."""
        try:
            logger.info("Processing tax data...")
            optimized_data = self.ai_engine.optimize(tax_data.dict())
            return optimized_data
        except Exception as e:
            logger.error(f"Error processing tax data: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    def fetch_financial_data(self) -> dict:
        """Fetch financial data from connected platforms."""
        try:
            logger.info("Fetching financial data...")
            data = self.data_adapter.fetch_data()
            return data
        except Exception as e:
            logger.error(f"Failed to fetch financial data: {e}")
            raise HTTPException(status_code=503, detail=str(e))

    def generate_report(self) -> dict:
        """Generate tax report based on processed data."""
        try:
            logger.info("Generating tax report...")
            report = self.ai_engine.generate_report()
            return report
        except Exception as e:
            logger.error(f"Failed to generate report: {e}")
            raise HTTPException(status_code=500, detail=str(e))

def main():
    app = FastAPI()

    @app.post("/process_tax_data")
    async def process_tax_data_endpoint(tax_data: TaxData):
        tax_system = TaxManagementSystem(Config())
        return tax_system.process_tax_data(tax_data)

    @app.get("/fetch_financial_data")
    async def fetch_financial_data_endpoint():
        tax_system = TaxManagementSystem(Config())
        return tax_system.fetch_financial_data()

    @app.get("/generate_report")
    async def generate_report_endpoint():
        tax_system = TaxManagementSystem(Config())
        return tax_system.generate_report()

    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)

# Example usage:
if __name__ == "__main__":
    main()