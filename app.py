from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        temperature_str = request.form.get("temperature", "").strip()
        conversion_type = request.form.get("conversion")

        # Validation: check if input is numeric
        try:
            temperature = float(temperature_str)
            if conversion_type == "CtoF":
                result = (temperature * 9/5) + 32
                result_text = f"{temperature}°C = {result:.2f}°F"
            else:
                result = (temperature - 32) * 5/9
                result_text = f"{temperature}°F = {result:.2f}°C"
        except ValueError:
            error = "⚠️ Please enter a valid temperature value."

        return render_template("index.html", result=result_text if result else None, error=error)

    return render_template("index.html", result=None, error=None)

if __name__ == "__main__":
    app.run(debug=True)
