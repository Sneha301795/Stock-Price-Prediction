"""
Prediction utilities.

This module provides prediction functionality using scikit-learn models.
"""

import logging
import pandas as pd
import numpy as np
from typing import Dict, List, Optional

from backend.advanced_models import run_all_models
from config.settings import settings

logger = logging.getLogger(__name__)


def predict_single_forecast(df: pd.DataFrame, model_path: str = None,
                           horizon: int = 1, ticker: str = None) -> Optional[tuple]:
    """
    Make a single prediction for next N days and return the selected model name.
    
    Parameters
    ----------
    df : pd.DataFrame
        Historical stock data.
    model_path : str
        Path to trained model (if None, uses ticker-specific model).
    horizon : int
        Days ahead to predict (1=next day, 5=next week, etc).
    ticker : str
        Stock ticker to determine which model to use.
        
    Returns
    -------
    Optional[tuple]
        (predicted_price, model_name) or (None, None) on error.
    """
    try:
        logger.info(f"Making prediction for {horizon} day(s) ahead")
        
        # Extract close prices
        if 'close' not in df.columns:
            logger.error("No 'close' column in data")
            return None, None
            
        prices = df['close'].values
        
        if len(prices) < 10:
            logger.error("Not enough data for prediction")
            return None, None
        
        # Run all models and get the best one
        models = run_all_models(prices)
        
        if not models:
            logger.error("No models could be trained")
            return None, None
            
        # Use the best model (first in sorted list by R² score)
        best_model = models[0]
        
        # Use the next_day_prediction for true forecasting
        if 'next_day_prediction' in best_model and best_model['next_day_prediction'] is not None:
            predicted_price = best_model['next_day_prediction']
        else:
            # Fallback to last prediction if next_day_prediction not available
            predicted_price = float(best_model['predictions'][-1])
        
        logger.info(f"Predicted price using {best_model['name']}: ${predicted_price:.2f}")
        return predicted_price, best_model.get('name')
        
    except Exception as e:
        logger.error(f"Error in prediction: {e}")
        return None, None

