import mimetypes
from urllib import response
import pandas as pd
import pickle
import numpy as np
import json
from flask import Response

class MyModel:
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing.................")

    def predict_raw(self, request):
        data = request.get("data", {}).get("ndarray")
        if data:
            mult_types_array = np.array(data, dtype=object)
            print(mult_types_array.item((0,0)))
            print(mult_types_array.item((0,1)))
            print(mult_types_array.item((0,2)))
        res = {}
        res["result"] = []
        res["result"].append(mult_types_array.item((0,0)))
        res["result"].append(mult_types_array.item((0,1)))
        res["result"].append(mult_types_array.item((0,2)))

        print(res)
        return res

    def predict(self,X,features_names):
        """X
        Return a prediction.
        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called - will run identity function")

        print("THIS IS FUN ==================================================================================!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(X)
        # print(X[0][0])
        # mult_types_array = np.array(X, dtype=object)
        # print(mult_types_array.item((0,0)))
        # print(mult_types_array.item((0,1)))
        # print(mult_types_array.item((0,2)))

        return mult_types_array

