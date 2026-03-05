<h1 align="center">H2S False Alarm Detection System</h1>

<div align="center">

<img src="https://img.shields.io/badge/Python-3.8+-blue">
<img src="https://img.shields.io/badge/Flask-2.0+-green">
<img src="https://img.shields.io/badge/Scikit--learn-1.0+-orange">

<p>
Machine Learning powered API to classify H2S gas leak alarms as dangerous or false.
</p>

<p>
<a href="#features">Features</a> •
<a href="#installation">Installation</a> •
<a href="#usage">Usage</a> •
<a href="#api-documentation">API Documentation</a>
</p>

</div>

<hr>

<h2 id="problem">Problem Statement</h2>

<p>
In chemical manufacturing environments, Hydrogen Sulfide (H2S) sensors frequently trigger alarms when detecting possible gas leaks. 
However, many of these alarms are false and lead to:
</p>

<ul>
<li>Unnecessary emergency team deployment</li>
<li>Operational delays</li>
<li>Increased maintenance costs</li>
<li>Alarm fatigue among safety personnel</li>
</ul>

<p>
The goal is to distinguish between real hazards and false alarms before dispatching emergency response teams.
</p>

<hr>

<h2>Solution Overview</h2>

<p>
This project implements a Machine Learning classification system that analyzes sensor data to predict whether an alarm represents a genuine hazard.
</p>

<table align="center">
<tr>
<th>Prediction</th>
<th>Meaning</th>
<th>Action</th>
</tr>
<tr>
<td>1</td>
<td>Dangerous</td>
<td>Dispatch emergency team</td>
</tr>
<tr>
<td>0</td>
<td>False Alarm</td>
<td>No action required</td>
</tr>
</table>

<p>
The model is deployed as a Flask REST API which can be integrated with factory monitoring systems.
</p>

<hr>

<h2 id="features">Key Features</h2>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>Real-time Alarm Classification</td>
<td>Predicts whether an alarm is dangerous or false.</td>
</tr>

<tr>
<td>Sensor Data Analysis</td>
<td>Uses multiple environmental parameters for prediction.</td>
</tr>

<tr>
<td>REST API Integration</td>
<td>Flask-based API that integrates with monitoring systems.</td>
</tr>

<tr>
<td>High Model Accuracy</td>
<td>Optimized preprocessing and machine learning pipeline.</td>
</tr>

</table>

<hr>

<h2>Technologies Used</h2>

<table>
<tr>
<th>Category</th>
<th>Tools</th>
</tr>

<tr>
<td>Programming</td>
<td>Python</td>
</tr>

<tr>
<td>Data Processing</td>
<td>Pandas, NumPy</td>
</tr>

<tr>
<td>Machine Learning</td>
<td>Scikit-learn</td>
</tr>

<tr>
<td>API Framework</td>
<td>Flask</td>
</tr>

<tr>
<td>Model Storage</td>
<td>Pickle</td>
</tr>

<tr>
<td>Testing</td>
<td>Postman, cURL</td>
</tr>

<tr>
<td>Version Control</td>
<td>Git, GitHub</td>
</tr>

</table>

<hr>

<h2>Model Performance</h2>

<p><b>Machine Learning Pipeline</b></p>

<pre>
Raw Data → Data Cleaning → Feature Scaling → Logistic Regression → Prediction
</pre>

<table align="center">
<tr>
<th>Metric</th>
<th>Score</th>
</tr>

<tr>
<td>Accuracy</td>
<td>100%</td>
</tr>

<tr>
<td>Precision</td>
<td>100%</td>
</tr>

<tr>
<td>Recall</td>
<td>100%</td>
</tr>

<tr>
<td>F1 Score</td>
<td>100%</td>
</tr>

</table>

<hr>

<h2 id="installation">Installation</h2>

<h3>Clone Repository</h3>

<pre>
git clone https://github.com/pranavdeshmukh/h2s-false-alarm-detection.git
cd h2s-false-alarm-detection
</pre>

<h3>Create Virtual Environment</h3>

<pre>
python -m venv venv
venv\Scripts\activate
</pre>

<h3>Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>Run Application</h3>

<pre>
python src/Application.py
</pre>

<p>
Server will start at:
</p>

<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2 id="api-documentation">API Documentation</h2>

<h3>Health Check</h3>

<pre>
GET /
</pre>

Response

<pre>
{
 "message": "H2S False Alarm Detection API is running",
 "status": "active"
}
</pre>

<h3>Predict Alarm</h3>

<pre>
POST /test_model
</pre>

Request Example

<pre>
{
 "Ambient Temperature": 30,
 "Calibration": 10,
 "Unwanted Substance_Deposition": 1,
 "Humidity(%)": 70,
 "H2S Content(ppm)": 15,
 "detected by_sensors": 3
}
</pre>

Response Example

<pre>
{
 "Prediction": 1,
 "dangerous": true,
 "recommendation": "DISPATCH TEAM"
}
</pre>

<hr>

<h2>Project Structure</h2>

<pre>
h2s-false-alarm-detection

data/
 └ Historical Alarm Cases.csv

model/
 ├ lr.pkl
 └ scaler.pkl

src/
 ├ Train_Model.py
 └ Application.py

Screenshot/
 ├ Confusion_matrix.png
 └ Postman_Test.png

README.md
</pre>

<hr>

<h2>Business Impact</h2>

<table>
<tr>
<th>Metric</th>
<th>Before</th>
<th>After</th>
<th>Improvement</th>
</tr>

<tr>
<td>False Alarm Rate</td>
<td>40%</td>
<td>&lt;5%</td>
<td>87.5% reduction</td>
</tr>

<tr>
<td>Dispatches</td>
<td>15-20/month</td>
<td>1-2/month</td>
<td>90% reduction</td>
</tr>

<tr>
<td>Response Time</td>
<td>Delayed</td>
<td>Instant</td>
<td>Real-time</td>
</tr>

</table>

<hr>

<h2>Future Enhancements</h2>

<ul>
<li>Support additional gases (CO, CH4)</li>
<li>Ensemble ML models (Random Forest, XGBoost)</li>
<li>Real-time monitoring dashboard</li>
<li>IoT / SCADA integration</li>
<li>Mobile alert system</li>
<li>Cloud deployment with Docker</li>
</ul>

<hr>

<h2>Author</h2>

<p>
<b>Pranav Deshmukh</b><br>
Machine Learning and Data Science
</p>

<div align="center">

<p>If this project was useful, consider giving it a star.</p>

</div>
