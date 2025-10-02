# Run the project

<ol>
    <li>Clone the repository</li>
    <li>Create a new virtual environment with python >= v3.10.</li>
    <li>Install the required packages in the environment using the following commands:
        <pre>pip install -r requirements.txt</pre>
        <pre>pip install -r requirements-dev.txt</pre>
    </li>
    <li>Set up pre-commit hooks using the following command:
        <pre>pre-commit install</pre>
    </li>
    <li>Create a file called '.env' in the root folder with the following information:
        <pre>
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASSWORD=
</pre>
    </li>
    <li>Run the following command to start the server:
        <pre>uvicorn main:app --reload --port 8002</pre>
    </li>
</ol>