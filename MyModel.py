# import pandas as pd
# import pickle


# class Iris:
#     def __init__(self):
#         self.model_name = "Iris"

#         # load the model from disk
#         self.model = pickle.load(open("finalized_model.sav", "rb"))

#     def predict(self, X, features_names):
#         df = pd.DataFrame(data=X, columns=features_names)
        
#         pred = self.model.predict(df)
#         return pred

class MyModel:
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing.................")

    def predict(self,X,features_names):
        """
        Return a prediction.
        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called - will run identity function")
        return X