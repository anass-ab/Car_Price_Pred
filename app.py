import flask
import joblib
import pandas as pd

app = flask.Flask(__name__, template_folder='.')

# Initialize cache
cache = {}

# Load the model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    print("Error: model.pkl not found. Make sure the model file is in the same directory as app.py.")
    exit()
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

@app.route('/', methods=['GET'])
def home():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the form
    Brand = flask.request.form['Brand']
    Model = flask.request.form['Model']
    Year = flask.request.form['Year']
    Engine_Size = flask.request.form['Engine_Size']
    Fuel_Type = flask.request.form['Fuel_Type']
    Transmission = flask.request.form['Transmission']
    Mileage = flask.request.form['Mileage']
    Doors = flask.request.form['Doors']
    Owner_Count = flask.request.form['Owner_Count']

    # Create cache key
    cache_key = (Brand, Model, Year, Engine_Size, Fuel_Type, Transmission, Mileage, Doors, Owner_Count)

    # Check if prediction is cached
    if cache_key in cache:
        print("Using cached prediction")
        return flask.render_template('index.html', prediction=cache[cache_key])

    # Handle empty input fields and type validation
    try:
        Year = 0 if Year == '' else float(Year)
        Engine_Size = 0 if Engine_Size == '' else float(Engine_Size)
        Mileage = 0 if Mileage == '' else float(Mileage)
        Doors = 0 if Doors == '' else float(Doors)
        Owner_Count = 0 if Owner_Count == '' else float(Owner_Count)
    except ValueError:
        return flask.jsonify({'error': 'Invalid input: Please enter numeric values for Year, Engine Size, Mileage, Doors, and Owner Count.'})

    # Calculate Age
    Age = 2025 - Year

    # Create a DataFrame from the data
    data = {'Brand': [Brand], 'Model': [Model], 'Year': [Year], 'Engine_Size': [Engine_Size],
            'Fuel_Type': [Fuel_Type], 'Transmission': [Transmission], 'Mileage': [Mileage],
            'Doors': [Doors], 'Owner_Count': [Owner_Count], 'Age': [Age]}
    df = pd.DataFrame(data)

    # One-hot encode categorical features
    df = pd.get_dummies(df, columns=['Brand', 'Model', 'Fuel_Type', 'Transmission'])

    # Ensure all columns are present (handle unseen categories)
    expected_columns = ['Year', 'Engine_Size', 'Mileage', 'Doors', 'Owner_Count', 'Age',
                        'Brand_Audi', 'Brand_BMW', 'Brand_Ford', 'Brand_Honda', 'Brand_Mercedes-Benz', 'Brand_Nissan', 'Brand_Toyota',
                        'Model_3 Series', 'Model_A4', 'Model_Altima', 'Model_Camry', 'Model_C-Class', 'Model_Civic', 'Model_F-150',
                        'Fuel_Type_CNG', 'Fuel_Type_Diesel', 'Fuel_Type_Gasoline', 'Fuel_Type_Hybrid', 'Fuel_Type_Petrol',
                        'Transmission_Automatic', 'Transmission_CVT', 'Transmission_Manual', 'Transmission_Semi-Automatic']
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_columns]  # Ensure correct column order

    # Make the prediction
    try:
        prediction = model.predict(df)
    except Exception as e:
        return flask.jsonify({'error': f'Model prediction error: {str(e)}'})

    # Store prediction in cache
    cache[cache_key] = prediction[0]

    # Return the prediction as JSON
    return flask.jsonify({'prediction': str(prediction[0])})
