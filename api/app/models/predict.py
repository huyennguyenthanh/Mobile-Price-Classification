import os
import pickle

class SmartphonePricePredict:

    def __init__(self, model_name) -> None:
        self.model = self.load_model(model_name)
        self.config_label = self.load_config_label()

        

    def load_model(self, model_name):
        """
        model_name:
            DecisionTree
            SoftmaxRegression

        """
        model = pickle.load(os.path.join("weights", model_name+".pkl"))
        return model

    def load_confid_label(self):
        labels = {
            0: "low",
            1: "medium",
            2: "high",
            3: "very high"
        }
        return labels

    def predict(self, data):

        prediction = self.model.predict(data)

        return prediction
