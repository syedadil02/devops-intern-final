#!/usr/bin/env python3
"""
MLflow Dummy Experiment Tracking Script

Logs parameters, training metrics across epochs, and model tags.
"""

import os
import random
import time
import mlflow

def run_experiment():
    experiment_name = "DevOps_Intern_Dummy_Experiment"
    mlflow.set_experiment(experiment_name)

    print(f"Starting MLflow experiment: '{experiment_name}'...")

    with mlflow.start_run(run_name="dummy_model_v1") as run:
        run_id = run.info.run_id
        print(f"Active Run ID: {run_id}")

        # 1. Log Parameters (Hyperparameters & Metadata)
        params = {
            "learning_rate": 0.01,
            "batch_size": 32,
            "epochs": 5,
            "optimizer": "Adam",
            "model_type": "LogisticRegression",
            "author": "Syed Adil",
            "environment": "DevOps-CI-Pipeline"
        }
        print("Logging parameters...")
        mlflow.log_params(params)

        # 2. Simulate Training and Log Metrics across Epochs
        print("Simulating training epochs...")
        loss = 1.0
        accuracy = 0.50

        for epoch in range(1, params["epochs"] + 1):
            time.sleep(0.5)
            # Simulated progressive improvement
            loss *= random.uniform(0.70, 0.85)
            accuracy += (1.0 - accuracy) * random.uniform(0.20, 0.40)

            print(f"  Epoch {epoch}/{params['epochs']} - Loss: {loss:.4f} | Accuracy: {accuracy:.4f}")
            mlflow.log_metric("train_loss", loss, step=epoch)
            mlflow.log_metric("train_accuracy", accuracy, step=epoch)

        # 3. Log Final Test Metrics
        mlflow.log_metric("final_accuracy", accuracy)
        mlflow.log_metric("final_loss", loss)

        # 4. Log Tags
        mlflow.set_tags({
            "stage": "staging",
            "assessment": "devops-intern-final",
            "framework": "python-standard"
        })

        # 5. Create and Log a Sample Artifact File
        artifact_path = "assessment_summary.txt"
        with open(artifact_path, "w") as f:
            f.write("DevOps Assessment MLFlow Run Summary\n")
            f.write("===================================\n")
            f.write(f"Run ID: {run_id}\n")
            f.write(f"Final Accuracy: {accuracy:.4f}\n")
            f.write(f"Final Loss: {loss:.4f}\n")
            f.write("Status: Completed Successfully\n")

        mlflow.log_artifact(artifact_path)
        if os.path.exists(artifact_path):
            os.remove(artifact_path)

        print(f"\nExperiment complete! Run tracked successfully under Run ID: {run_id}")

if __name__ == "__main__":
    run_experiment()
