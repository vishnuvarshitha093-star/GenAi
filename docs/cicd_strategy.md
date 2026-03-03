# CI/CD Strategy
1. Trigger on PR: lint, unit test, OpenAPI validation, SAST.
2. Build artifacts: backend image, frontend image, agent image.
3. Deploy to staging with smoke tests.
4. Manual approval gate for production.
5. Post-deploy synthetic monitoring and rollback hooks.
