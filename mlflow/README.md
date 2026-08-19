# MLflow Experiment Tracking

This directory contains an MLflow tracking setup to log dummy model experiments, hyperparameters, dynamic metrics per epoch, tags, and run artifacts.

---

## How to Run?

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```
### 2. Run the Experiment
```bash
python experiment.py
```

### 3. Launch MLflow UI
To explore tracked runs, parameters, metrics curves, and artifacts in the web browser:
```bash
mlflow ui --port 5000
```
Then visit: [http://localhost:5000](http://localhost:5000)

---

## What is Tracked?
- **Parameters**: `learning_rate`, `batch_size`, `epochs`, `optimizer`, `model_type`, `author`
- **Dynamic Metrics**: `train_loss`, `train_accuracy` across each epoch
- **Final Metrics**: `final_accuracy`, `final_loss`
- **Tags**: `stage`, `assessment`, `framework`
- **Artifacts**: `assessment_summary.txt`
