class Config:
    def __init__(self):
        self.api_key = "your_api_key_here"
        self.data_sources = ["TurboTax", "QuickBooks"]
        self.model_path = "models/tax_optimization_model.h5"
        self.log_level = "INFO"

    def get_api_key(self) -> str:
        return self.api_key

    def get_data_sources(self) -> list:
        return self.data_sources