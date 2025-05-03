import joblib

# Load the model
model = joblib.load("best_model.pkl")

# Check what kind of object it is
print("Model type:", type(model))

# If it's a Pipeline, show its steps
if hasattr(model, "steps"):
    print("Pipeline steps:")
    for name, step in model.steps:
        print(f" - {name}: {type(step)}")
else:
    print("Not a pipeline. This may be a plain model.")
