# Cross-Repository E2E Testing Guide

## Overview

This guide explains how to run end-to-end tests between doc2-api and DocFlow services, ensuring proper Kafka message flow and webhook communication across repositories.

## Architecture

```
┌─────────────────┐                    ┌─────────────────┐
│    doc2-api     │                    │     DocFlow     │
│                 │                    │                 │
│  E2E Webhook    │◄──── HTTP ────────│  pytest tests   │
│  /e2e/trigger   │                    │                 │
│                 │                    │                 │
│  Kafka Producer │───── Kafka ───────►│ Kafka Consumer  │
│                 │                    │                 │
│  pytest tests   │────── HTTP ───────►│  E2E Webhook    │
│                 │                    │  /e2e/process   │
│                 │                    │                 │
│ Kafka Consumer  │◄───── Kafka ───────│ Kafka Producer  │
└─────────────────┘                    └─────────────────┘
```

## Environment Configuration

### URL Discovery

Services automatically discover each other using environment variables:

| Service | Environment Variable | Purpose | Example |
|---------|---------------------|---------|---------|
| doc2-api | `DOC_FLOW_URL` | Find DocFlow | `https://dev-docflow.docbits.com/` |
| DocFlow | `API_URL` | Find doc2-api | `https://dev-api.docbits.com/` |

### Environment-Specific URLs

#### Development
```bash
export DOC_FLOW_URL="https://dev-docflow.docbits.com/"
export API_URL="https://dev-api.docbits.com/"
```

#### Staging
```bash
export DOC_FLOW_URL="https://stage-docflow.docbits.com/"
export API_URL="https://stage-api.docbits.com/"
```

#### Production
```bash
export DOC_FLOW_URL="https://docflow.docbits.com/"
export API_URL="https://api.docbits.com/"
```

#### Local Testing
```bash
# Default values (no export needed)
# DOC_FLOW_URL defaults to http://localhost:8500/
# API_URL defaults to http://localhost:8080/
```

## Test Files

### doc2-api Repository
- **Location**: `tests/e2e/test_cross_repo_kafka.py`
- **Purpose**: Tests doc2-api → DocFlow communication
- **Key Tests**:
  - `test_workflow_execution_to_docflow()` - Send workflow to DocFlow
  - `test_workflow_error_handling_with_docflow()` - Error handling
  - `test_multiple_workflow_requests_to_docflow()` - Batch processing

### DocFlow Repository
- **Location**: `tests/e2e/test_cross_repo_kafka.py`
- **Purpose**: Tests DocFlow → doc2-api communication
- **Key Tests**:
  - `test_send_response_to_doc2api()` - Send response to doc2-api
  - `test_workflow_status_update_to_doc2api()` - Status updates
  - `test_bidirectional_communication()` - Full round-trip test

## Running Cross-Repository Tests

### Prerequisites

1. **Both services must be running**:
   ```bash
   # Terminal 1 - Start doc2-api
   cd doc2-api
   uvicorn api:app --port 8080
   
   # Terminal 2 - Start DocFlow
   cd DocFlow
   uvicorn api:app --port 8500
   ```

2. **E2E webhooks must be enabled** (enabled by default)

3. **Environment variables must be set** (if not using localhost)

### Quick Start

1. **Verify infrastructure**:
   ```bash
   python verify_cross_repo_e2e.py
   ```

2. **Run all cross-repo tests**:
   ```bash
   python run_cross_repo_e2e_tests.py
   ```

### Individual Test Runs

#### Test doc2-api → DocFlow
```bash
cd doc2-api
pytest tests/e2e/test_cross_repo_kafka.py -v

# Run specific test
pytest tests/e2e/test_cross_repo_kafka.py::test_workflow_execution_to_docflow -v
```

#### Test DocFlow → doc2-api
```bash
cd DocFlow
pytest tests/e2e/test_cross_repo_kafka.py -v

# Run specific test
pytest tests/e2e/test_cross_repo_kafka.py::test_send_response_to_doc2api -v
```

## E2E Webhook Endpoints

### doc2-api Endpoints

#### `/api/v1/e2e/trigger-kafka-test`
- **Method**: POST
- **Purpose**: Trigger Kafka message from doc2-api
- **Called by**: DocFlow tests

Example request:
```json
{
  "test_id": "550e8400-e29b-41d4-a716-446655440000",
  "test_type": "workflow_execution",
  "doc_id": "550e8400-e29b-41d4-a716-446655440001",
  "org_id": "550e8400-e29b-41d4-a716-446655440002",
  "parameters": {
    "workflow_config": {
      "workflow_id": "test-workflow",
      "name": "Test Workflow"
    }
  },
  "expect_response": true,
  "timeout": 30.0
}
```

### DocFlow Endpoints

#### `/api/v1/e2e/process-workflow`
- **Method**: POST
- **Purpose**: Process workflow and send response
- **Called by**: doc2-api tests

Example request:
```json
{
  "test_id": "550e8400-e29b-41d4-a716-446655440000",
  "doc_id": "550e8400-e29b-41d4-a716-446655440001",
  "org_id": "550e8400-e29b-41d4-a716-446655440002",
  "task_id": "550e8400-e29b-41d4-a716-446655440003",
  "workflow_config": {
    "workflow_id": "test-workflow",
    "name": "Test Workflow",
    "parameters": {}
  },
  "simulate_error": false,
  "processing_delay": 0.5
}
```

## Test Scenarios

### 1. Basic Workflow Execution
```python
# doc2-api test calls DocFlow webhook
def test_workflow_execution_to_docflow():
    response = requests.post(
        f"{DOCFLOW_BASE_URL}api/v1/e2e/process-workflow",
        json=request_data
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
```

### 2. Error Handling
```python
# Test error simulation
def test_workflow_error_handling():
    request_data["simulate_error"] = True
    response = requests.post(...)
    assert response.json()["success"] is False
```

### 3. Performance Testing
```python
# Test multiple concurrent messages
@pytest.mark.parametrize("num_messages", [1, 5, 10])
def test_multiple_workflow_requests(num_messages):
    # Send multiple messages and verify processing
```

## Debugging

### Check Service URLs
The tests will log which URLs they're using:
```
🔗 Cross-repo testing: doc2-api will call DocFlow at: https://dev-docflow.docbits.com/api/v1/e2e/process-workflow
   Environment: dev
```

### Common Issues

1. **Connection Refused**
   - Ensure both services are running
   - Check the URLs in environment variables
   - Verify firewall/network settings

2. **404 Not Found**
   - Ensure E2E webhook routers are enabled
   - Check the endpoint paths are correct

3. **Timeout Errors**
   - Increase timeout values in test requests
   - Check Kafka connectivity
   - Verify both services can access Kafka

### Debug Commands

```bash
# Check if services are running
curl http://localhost:8080/health
curl http://localhost:8500/health

# Test E2E endpoints directly
curl -X POST http://localhost:8080/api/v1/e2e/health
curl -X POST http://localhost:8500/api/v1/e2e/health

# Check environment variables
echo $DOC_FLOW_URL
echo $API_URL
```

## CI/CD Integration

### GitHub Actions
Both repositories include E2E tests in their CI pipelines:

```yaml
- name: Run E2E Tests
  env:
    DOC_FLOW_URL: ${{ secrets.DOC_FLOW_URL }}
    API_URL: ${{ secrets.API_URL }}
  run: |
    pytest tests/e2e/test_cross_repo_kafka.py -v
```

### Jenkins/GitLab CI
Set environment variables in your pipeline configuration:

```groovy
environment {
    DOC_FLOW_URL = credentials('doc-flow-url')
    API_URL = credentials('api-url')
}
```

## Best Practices

1. **Always use environment variables** for service URLs
2. **Log test configuration** to aid debugging
3. **Set appropriate timeouts** for cross-service calls
4. **Use test prefixes** to isolate test data
5. **Run tests in both directions** to ensure bidirectional flow
6. **Monitor Kafka topics** during test execution
7. **Clean up test data** after test runs

## Summary

Cross-repository E2E testing ensures that doc2-api and DocFlow can communicate properly through Kafka and webhooks. The tests automatically adapt to different environments using environment variables, making them suitable for local development, CI/CD pipelines, and production validation.