# GitHub Actions for Go and CDK Projects

This repository contains a collection of GitHub Actions designed to streamline the CI/CD process for projects using Go and AWS Cloud Development Kit (CDK). It includes actions for setting up environments, linting Go code, colorizing CDK diff outputs, and more.

## Actions Overview

### Setup Actions

- **Setup Node and CDK**: Configures the environment with specific versions of Node.js and AWS CDK. See [setup-cdk/action.yaml](setup-cdk/action.yaml).
- **Setup Go private repository**: Configures git for accessing Go private repositories. See [setup-internal-support/action.yaml](setup-internal-support/action.yaml).

### Linting and Code Quality

- **Lint Go**: Runs golangci-lint on your Go codebase. See [lint-go/action.yaml](lint-go/action.yaml).

### CDK Utilities

- **Colorize CDK Diff Output**: Enhances the readability of CDK diff outputs by colorizing them. See [colorize-diff/action.yaml](colorize-diff/action.yaml).

## Workflows

### CDK Go Workflow

The `CDK Go` workflow is designed for projects using both Go and AWS CDK. It supports various operations such as linting, testing, security checks, and deployment based on the branch context (e.g., master branch or feature branches).

Key features:
- Conditional steps for internal repository support.
- Setup for Go and Node.js based on specified versions.
- CDK operations like `synth`, `diff`, and `deploy`.

See the workflow definition in [.github/workflows/cdk-go.yaml](.github/workflows/cdk-go.yaml).

### Dependabot Configuration

This repository is configured to use Dependabot for keeping GitHub Actions up-to-date. Dependabot checks weekly for updates and creates pull requests for any found updates.

See the Dependabot configuration in [.github/dependabot.yaml](.github/dependabot.yaml).

## Getting Started

To use these actions in your workflow, refer to the `uses` statements in the provided workflow examples. Customize the inputs as necessary for your project's requirements.

## Contributing

Contributions to improve or extend the functionality of these actions are welcome. Please follow the standard GitHub pull request process to propose your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.