# End-to-End Testing Documentation

## Overview

This directory contains comprehensive documentation for E2E testing between doc2-api and DocFlow services.

## Documentation Structure

### 📚 Available Guides

1. **[E2E Kafka Testing](E2E_KAFKA_TESTING.md)**
   - Complete guide to Kafka-based E2E testing
   - Message formats and test flows
   - Webhook endpoints documentation
   - Performance metrics and monitoring

2. **[Cross-Repository E2E Testing](CROSS_REPO_E2E_TESTING.md)**
   - Guide for testing between doc2-api and DocFlow
   - Environment configuration and URL discovery
   - Running cross-repo tests
   - CI/CD integration

## Quick Start

### Local Testing
```bash
# Start both services
cd doc2-api && uvicorn api:app --port 8080 &
cd DocFlow && uvicorn api:app --port 8500 &

# Run cross-repository tests
python run_cross_repo_e2e_tests.py
```

### Environment Testing
```bash
# Set environment URLs
export DOC_FLOW_URL="https://dev-docflow.docbits.com/"
export API_URL="https://dev-api.docbits.com/"

# Run tests
cd doc2-api && pytest tests/e2e/test_cross_repo_kafka.py -v
cd DocFlow && pytest tests/e2e/test_cross_repo_kafka.py -v
```

## Key Features

- ✅ **Bidirectional Testing**: Tests communication in both directions
- ✅ **Environment Aware**: Automatically uses correct URLs per environment
- ✅ **Webhook-Based**: Uses E2E endpoints for cross-service testing
- ✅ **Realistic Messages**: ~95% identical to production messages
- ✅ **Comprehensive Coverage**: Tests happy paths, errors, and edge cases

## Test Infrastructure Status

### doc2-api
- **Status**: ✅ Deployed to dev branch
- **E2E Endpoints**: Enabled
- **Cross-repo Tests**: Available
- **Environment Support**: DOC_FLOW_URL

### DocFlow
- **Status**: ✅ Deployed to dev branch
- **E2E Endpoints**: Enabled
- **Cross-repo Tests**: Available
- **Environment Support**: API_URL

## Support

For questions or issues:
- Check the detailed guides in this directory
- Review test logs for URL configuration
- Ensure both services are running
- Verify environment variables are set correctly