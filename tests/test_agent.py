from fastapi.testclient import TestClient
from agentx.main import app
client = TestClient(app)

def test_run_and_refuse():
    payload = client.post("/agent/run", json={"goal": 'highly available app on GCP for 50k users with PostgreSQL and DR', "payload": {}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["proposal"]["db"] == "postgresql"
    refused = client.post("/agent/run", json={"goal": 'terraform apply in the customer project'}).json()
    assert refused["refused"] is True
