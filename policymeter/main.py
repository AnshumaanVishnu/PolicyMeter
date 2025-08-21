from flask import Flask, render_template
from data_collector import fetch_news_data, fetch_public_data
from sentiment_analyzer import analyze_dataset

# Adjust the template folder path
app = Flask(__name__, template_folder='web/templates')

@app.route('/')
def home():
    """
    Main route to display sentiment analysis results.
    """
    # 1. Fetch data
    news_data = fetch_news_data()
    public_data = fetch_public_data()
    all_data = news_data + public_data

    # 2. Analyze sentiment
    results = analyze_dataset(all_data)

    # 3. Render the template with the results
    return render_template('index.html', results=results)

if __name__ == "__main__":
    # Note: In a real production environment, you would use a proper WSGI server.
    # The development server is not suitable for production.
    app.run(debug=True, port=8080)
